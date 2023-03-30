from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from entities.entity_base import EntityBase

# Basically, there are 30 differnent ways of doing this mapping.
# Alternatively, you can just have a secondary table that joins ChildEntities to ParentEntities, however, we chose not to do that here.

class ChildEntity(EntityBase):
    __tablename__ = "child_entity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    parent_id : Mapped[int] = mapped_column(Integer, ForeignKey("parent_entity.id"))