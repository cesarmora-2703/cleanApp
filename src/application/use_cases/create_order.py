from dataclasses import dataclass
from typing import List

# Importamos las abstracciones (Protocolos y Entidades), NUNCA la infraestructura (Django)
from src.domain.entities import Order
from src.domain.repositories import OrderRepository, ProductRepository, InventoryRepository, UserRepository
from src.domain.enums import OrderStatus
from datetime import datetime

# Input DTO: Datos necesarios para ejecutar el caso de uso
@dataclass
class OrderItemInput:
    product_id: int
    quantity: int

@dataclass
class CreateOrderInput:
    user_id: int
    items: List[OrderItemInput]

class CreateOrderUseCase:
    # Inyección de Dependencias: Pedimos las interfaces en el constructor
    def __init__(
        self, 
        order_repo: OrderRepository,
        product_repo: ProductRepository,
        inventory_repo: InventoryRepository,
        user_repo: UserRepository
    ):
        self.order_repo = order_repo
        self.product_repo = product_repo
        self.inventory_repo = inventory_repo
        self.user_repo = user_repo

    def execute(self, input_data: CreateOrderInput) -> Order:
        # 1. Validar Usuario
        user = self.user_repo.get_by_id(input_data.user_id)
        if not user:
            raise ValueError(f"Usuario {input_data.user_id} no encontrado")

        # 2. Crear la Entidad Orden (vacía inicialmente)
        order = Order(
            id=None, 
            user_id=user.id, 
            created_at=datetime.now(),
            status=OrderStatus.PENDING
        )

        # 3. Procesar Items (Lógica de Orquestación)
        for item_input in input_data.items:
            # Buscar producto
            product = self.product_repo.get_by_id(item_input.product_id)
            if not product:
                raise ValueError(f"Producto {item_input.product_id} no existe")

            # Verificar Stock (Regla de Negocio)
            if not self.inventory_repo.check_stock(product.id, item_input.quantity):
                raise ValueError(f"Stock insuficiente para {product.name}")

            # Agregar a la orden (Lógica de Dominio)
            # Nota: order.add_product encapsula la creación del OrderItem y cálculos
            order.add_product(product, quantity=item_input.quantity)
            
            # Reducir stock (Efecto secundario)
            self.inventory_repo.reduce_stock(product.id, item_input.quantity)

        # 4. Persistir la Orden
        saved_order = self.order_repo.save(order)
        
        return saved_order