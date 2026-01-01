from decimal import Decimal

from src.domain import entities
from src.domain.enums import OrderStatus, PaymentStatus
from src.infrastructure import models as db_models


class ProductMapper:
    @staticmethod
    def to_domain(model: db_models.ProductModel) -> entities.Product:
        return entities.Product(
            id=model.id,
            name=str(model.name),
            sku=str(model.sku),
            price=float(model.price),
            description=str(model.description),
        )

    @staticmethod
    def to_db(entity: entities.Product) -> db_models.ProductModel:
        return db_models.ProductModel(
            id=entity.id,
            name=entity.name,
            sku=entity.sku,
            price=Decimal(str(entity.price)),
            description=entity.description,
        )


class UserMapper:
    @staticmethod
    def to_domain(model: db_models.CustomUser) -> entities.User:
        return entities.User(
            id=model.id,
            username=str(model.username),
            email=str(model.email),
            is_active=bool(model.is_active),
            is_staff=bool(model.is_staff),
        )

    @staticmethod
    def to_db(entity: entities.User) -> db_models.CustomUser:
        return db_models.CustomUser(
            id=entity.id,
            username=entity.username,
            email=entity.email,
            is_active=entity.is_active,
            is_staff=entity.is_staff,
        )


class ServiceMapper:
    @staticmethod
    def to_domain(model: db_models.ServiceModel) -> entities.Service:
        return entities.Service(
            id=model.id,
            name=str(model.name),
            hourly_rate=float(model.hourly_rate),
            description=str(model.description),
        )

    @staticmethod
    def to_db(entity: entities.Service) -> db_models.ServiceModel:
        return db_models.ServiceModel(
            id=entity.id,
            name=entity.name,
            hourly_rate=Decimal(str(entity.hourly_rate)),
            description=entity.description,
        )


class InventoryMapper:
    @staticmethod
    def to_domain(model: db_models.InventoryModel) -> entities.Inventory:
        return entities.Inventory(
            id=model.id,
            product_id=model.product_id,
            quantity=model.quantity,
            location=str(model.location),
        )

    @staticmethod
    def to_db(entity: entities.Inventory) -> db_models.InventoryModel:
        return db_models.InventoryModel(
            id=entity.id,
            product_id=entity.product_id,
            quantity=entity.quantity,
            location=entity.location,
        )


class OrderMapper:
    @staticmethod
    def to_domain(model: db_models.OrderModel) -> entities.Order:
        items = [
            entities.OrderItem(
                product_id=item.product_id,
                service_id=item.service_id,
                name=str(item.name_at_purchase),
                quantity=item.quantity,
                unit_price=float(item.unit_price_at_purchase),
            )
            for item in model.items.all()
        ]
        return entities.Order(
            id=model.id,
            user_id=model.user_id,
            created_at=model.created_at,
            status=OrderStatus(model.status),
            items=items,
        )

    @staticmethod
    def to_db(entity: entities.Order) -> db_models.OrderModel:
        return db_models.OrderModel(
            id=entity.id,
            user_id=entity.user_id,
            created_at=entity.created_at,
            status=entity.status.value,
        )


class PaymentMapper:
    @staticmethod
    def to_domain(model: db_models.PaymentModel) -> entities.Payment:
        return entities.Payment(
            id=model.id,
            order_id=model.order_id,
            amount=float(model.amount),
            status=PaymentStatus(model.status),
            transaction_id=model.transaction_id,
            created_at=model.created_at,
        )

    @staticmethod
    def to_db(entity: entities.Payment) -> db_models.PaymentModel:
        return db_models.PaymentModel(
            id=entity.id,
            order_id=entity.order_id,
            amount=Decimal(str(entity.amount)),
            status=entity.status.value,
            transaction_id=entity.transaction_id,
            created_at=entity.created_at,
        )
