from typing import Optional

from src.domain.entities import Inventory, Order, Payment, Product, Service, User
from src.infrastructure.mappers import (
    InventoryMapper,
    OrderMapper,
    PaymentMapper,
    ProductMapper,
    ServiceMapper,
    UserMapper,
)
from src.infrastructure.models import (
    CustomUser,
    InventoryModel,
    OrderModel,
    PaymentModel,
    ProductModel,
    ServiceModel,
)


class DjangoProductRepository:
    def get_by_id(self, product_id: int) -> Optional[Product]:
        try:
            # 1. Usar el ORM de Django
            model = ProductModel.objects.get(id=product_id)
            # 2. Convertir a Entidad Limpia y retornar
            return ProductMapper.to_domain(model)
        except ProductModel.DoesNotExist:
            return None

    def save(self, product: Product) -> Product:
        # 1. Convertir Entidad a Modelo Django
        model = ProductMapper.to_db(product)
        # 2. Guardar en DB (PostgreSQL)
        model.save()
        # 3. Retornar la entidad actualizada (con ID si era nuevo)
        return ProductMapper.to_domain(model)


class DjangoUserRepository:
    def get_by_id(self, user_id: int) -> Optional[User]:
        try:
            model = CustomUser.objects.get(id=user_id)
            return UserMapper.to_domain(model)
        except CustomUser.DoesNotExist:
            return None

    def save(self, user: User) -> User:
        model = UserMapper.to_db(user)
        model.save()
        return UserMapper.to_domain(model)


class DjangoServiceRepository:
    def get_by_id(self, service_id: int) -> Optional[Service]:
        try:
            model = ServiceModel.objects.get(id=service_id)
            return ServiceMapper.to_domain(model)
        except ServiceModel.DoesNotExist:
            return None

    def save(self, service: Service) -> Service:
        model = ServiceMapper.to_db(service)
        model.save()
        return ServiceMapper.to_domain(model)


class DjangoInventoryRepository:
    def get_by_id(self, inventory_id: int) -> Optional[Inventory]:
        try:
            model = InventoryModel.objects.get(id=inventory_id)
            return InventoryMapper.to_domain(model)
        except InventoryModel.DoesNotExist:
            return None

    def save(self, inventory: Inventory) -> Inventory:
        model = InventoryMapper.to_db(inventory)
        model.save()
        return InventoryMapper.to_domain(model)


class DjangoOrderRepository:
    def get_by_id(self, order_id: int) -> Optional[Order]:
        try:
            model = OrderModel.objects.get(id=order_id)
            return OrderMapper.to_domain(model)
        except OrderModel.DoesNotExist:
            return None

    def save(self, order: Order) -> Order:
        model = OrderMapper.to_db(order)
        model.save()
        return OrderMapper.to_domain(model)


class DjangoPaymentRepository:
    def get_by_id(self, payment_id: int) -> Optional[Payment]:
        try:
            model = PaymentModel.objects.get(id=payment_id)
            return PaymentMapper.to_domain(model)
        except PaymentModel.DoesNotExist:
            return None

    def save(self, payment: Payment) -> Payment:
        model = PaymentMapper.to_db(payment)
        model.save()
        return PaymentMapper.to_domain(model)
