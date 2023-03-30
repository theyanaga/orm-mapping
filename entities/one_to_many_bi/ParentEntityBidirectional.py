from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped

from entities.one_to_many_uni.child_entity import ChildEntity
from ..entity_base import EntityBase
from typing import List

class ParentEntityBidirectional(EntityBase):
    __tablename__ = "parent_entity_bidirectional"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    children: Mapped[List[ChildEntity]]= relationship("ChildEntityBidirectional", back_populates="parent")