from typing import Optional

from src.domain.entities import Product
from src.infrastructure.mappers import ProductMapper
from src.infrastructure.models import ProductModel


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
