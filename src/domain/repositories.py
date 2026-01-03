from typing import Protocol, Optional 
from .entities import Payment, Product, Order, User

# 1. Repositorio de Usuarios
class UserRepository(Protocol):
    def get_by_id(self, id: int) -> Optional[User]: ...

# 2. Repositorio de Productos
class ProductRepository(Protocol):
    def get_by_id(self, id: int) -> Optional[Product]: ...
    def save(self, product: Product) -> Product: ...

# 3. Repositorio de Inventario
class InventoryRepository(Protocol):
    def check_stock(self, product_id: int, quantity: int) -> bool: ...
    def reduce_stock(self, product_id: int, quantity: int) -> None: ...

# 4. Repositorio de Ordenes
class OrderRepository(Protocol):
    def save(self, order: Order) -> Order: ...

# 5. Repositorio de Pagos
class PaymentRepository(Protocol):
    def save(self, payment: Payment) -> Payment: ...
    def mark_as_paid(self, payment_id: int, transaction_id: str) -> None: ...

#