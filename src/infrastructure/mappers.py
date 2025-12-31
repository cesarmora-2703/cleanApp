from django.db.models.expressions import Decimal

from src.domain import entities
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
