from src.infrastructure.repositories import (
    DjangoInventoryRepository,
    DjangoOrderRepository,
    DjangoPaymentRepository,
    DjangoProductRepository,
    DjangoServiceRepository,
    DjangoUserRepository,
)
from src.application.use_cases.create_order import CreateOrderUseCase

class Container:
    """
    Centraliza la creación de objetos.
    Si mañana cambias PostgreSQL por MongoDB, solo cambias esto aquí.
    """
    # Instanciar repositorios (Singletons)
    product_repository = DjangoProductRepository()
    user_repository = DjangoUserRepository()
    service_repository = DjangoServiceRepository()
    inventory_repository = DjangoInventoryRepository()
    order_repository = DjangoOrderRepository()
    payment_repository = DjangoPaymentRepository()
    
    # 2. Instanciar Casos de Uso (Inyectando los repositorios)
    @staticmethod
    def create_order_use_case() -> CreateOrderUseCase:
        return CreateOrderUseCase(
            product_repository = Container.product_repository,
            user_repository = Container.user_repository,
            service_repository = Container.service_repository,
            inventory_repository = Container.inventory_repository,
            order_repository = Container.order_repository,
            payment_repository = Container.payment_repository
        )