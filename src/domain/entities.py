from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from .enums import OrderStatus, PaymentStatus


# --- 1. ENTIDAD USER (Pura) ---
@dataclass
class User:
    """
    Representación agnóstica del Usuario.
    En Infraestructura se mapeará al 'AbstractUser' de Django.
    """

    id: Optional[int]
    username: str
    email: str
    is_active: bool = True
    is_staff: bool = False

    # Aquí puedes añadir lógica de negocio pura si la necesitas
    def activate(self):
        self.is_active = True


# --- 2. PRODUCTO Y SERVICIO ---
@dataclass
class Product:
    id: Optional[int]
    name: str
    sku: str
    price: float
    description: str = ""

    def update_price(self, new_price: float):
        if new_price < 0:
            raise ValueError("El precio no puede ser negativo")
        self.price = new_price


@dataclass
class Service:
    id: Optional[int]
    name: str
    hourly_rate: float
    description: str = ""


# --- 3. INVENTARIO ---
@dataclass
class Inventory:
    id: Optional[int]
    product_id: int  # Referencia por ID para evitar acoplamiento profundo
    quantity: int
    location: str

    def add_stock(self, amount: int):
        self.quantity += amount

    def remove_stock(self, amount: int):
        if self.quantity < amount:
            raise ValueError("Stock insuficiente")
        self.quantity -= amount


# --- 4. ORDER & ITEMS ---
@dataclass
class OrderItem:
    """Value Object que representa una línea en la orden"""

    product_id: Optional[int]  # Puede ser None si es un Servicio
    service_id: Optional[int]  # Puede ser None si es un Producto
    name: str
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price


@dataclass
class Order:
    id: Optional[int]
    user_id: int
    created_at: datetime
    status: OrderStatus = OrderStatus.PENDING
    items: List[OrderItem] = field(default_factory=list)

    @property
    def total_amount(self) -> float:
        return sum(item.subtotal for item in self.items)

    def add_product(self, product: Product, quantity: int):
        item = OrderItem(
            product_id=product.id,
            service_id=None,
            name=product.name,
            quantity=quantity,
            unit_price=product.price,
        )
        self.items.append(item)

    def add_service(self, service: Service, hours: int):
        item = OrderItem(
            product_id=None,
            service_id=service.id,
            name=service.name,
            quantity=hours,
            unit_price=service.hourly_rate,
        )
        self.items.append(item)


# --- 5. PAGOS ---
@dataclass
class Payment:
    id: Optional[int]
    order_id: int
    amount: float
    status: PaymentStatus = PaymentStatus.PENDING
    transaction_id: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

    def mark_as_paid(self, transaction_id: str):
        self.status = PaymentStatus.COMPLETED
        self.transaction_id = transaction_id
