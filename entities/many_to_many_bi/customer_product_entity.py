from sqlalchemy import Column, Integer, ForeignKey, Table
from entities.entity_base import EntityBase

customer_product_table = Table(
    "customer_order",
    EntityBase.metadata,
    Column("customer_id", Integer, ForeignKey("customers.id")),
    Column("product_id", Integer, ForeignKey("products.id"))
)