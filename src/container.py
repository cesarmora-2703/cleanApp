from src.infrastructure.repositories import (
    DjangoInventoryRepository,
    DjangoOrderRepository,
    DjangoPaymentRepository,
    DjangoProductRepository,
    DjangoServiceRepository,
    DjangoUserRepository,
)

class Container:
    """
    Centraliza la creación de objetos.
    Si mañana cambias PostgreSQL por MongoDB, solo cambias esto aquí.
    """
    product_repository = DjangoProductRepository()
    user_repository = DjangoUserRepository()
    service_repository = DjangoServiceRepository()
    inventory_repository = DjangoInventoryRepository()
    order_repository = DjangoOrderRepository()
    payment_repository = DjangoPaymentRepository()