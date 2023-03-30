from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from entities.entity_base import EntityBase
from entities.many_to_one_uni.student_entity import StudentEntity

class PostEntity(EntityBase):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)

    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id"))
    student : Mapped[StudentEntity] = relationship("StudentEntity")