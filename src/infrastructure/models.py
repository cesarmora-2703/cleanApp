from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# 1. USUARIO (Hereda de AbstractUser para aprovechar el Auth de Django)
class CustomUser(AbstractUser):
    # Aquí puedes añadir campos extra que requiera PostgreSQL
    pass


# 2. PRODUCTOS Y SERVICIOS
class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)


class ServiceModel(models.Model):
    name = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)


# 3. INVENTARIO
class InventoryModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)


# 4. ORDENES
class OrderModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default="PENDING")


class OrderItemModel(models.Model):
    order = models.ForeignKey(
        OrderModel, related_name="items", on_delete=models.CASCADE
    )
    # Relaciones opcionales (nullable)
    product = models.ForeignKey(
        ProductModel, null=True, blank=True, on_delete=models.SET_NULL
    )
    service = models.ForeignKey(
        ServiceModel, null=True, blank=True, on_delete=models.SET_NULL
    )

    # Guardamos el snapshot de los datos al momento de la compra
    name_at_purchase = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)


# 5. PAGOS
class PaymentModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
