from typing import List
from entities.entity_base import EntityBase
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from entities.many_to_many_bi.product_entity import ProductEntity
from entities.many_to_many_bi.customer_product_entity import customer_product_table


class CustomerEntity(EntityBase):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    products_bought : Mapped[List[ProductEntity]] = relationship(secondary=customer_product_table ,back_populates="customers")