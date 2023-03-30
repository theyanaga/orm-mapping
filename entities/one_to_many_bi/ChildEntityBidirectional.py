from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from entities.entity_base import EntityBase
from entities.one_to_many_bi.ParentEntityBidirectional import ParentEntityBidirectional


class ChildEntityBidirectional(EntityBase):
    __tablename__ = "child_entity_bidirectional"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    parent_id : Mapped[int] = mapped_column(Integer, ForeignKey("parent_entity_bidirectional.id"))
    parent : Mapped[ParentEntityBidirectional] = relationship("ParentEntityBidirectional", back_populates="children")