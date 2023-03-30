from typing import List
from entities.entity_base import EntityBase
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from entities.many_to_many_uni.event_user import user_event_table
from entities.many_to_many_uni.user_entity import UserEntity


class EventEntity(EntityBase):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    users: Mapped[List[UserEntity]] = relationship("UserEntity", secondary=user_event_table)