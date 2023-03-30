
from sqlalchemy import Column, Integer, ForeignKey, String
from entities.entity_base import EntityBase


class StudentEntity(EntityBase):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
