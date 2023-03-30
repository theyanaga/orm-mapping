from entities.entity_base import EntityBase
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from typing import List

from entities.many_to_many_bi.customer_product_entity import customer_product_table

class ProductEntity(EntityBase):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    customers : Mapped[List['CustomerEntity']] = relationship(secondary=customer_product_table, back_populates="products_bought")