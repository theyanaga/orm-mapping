from entities.entity_base import EntityBase
from sqlalchemy import Column, Integer, String, Table, ForeignKey

user_event_table = Table(
    "user_event",
    EntityBase.metadata, 
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("event_id", Integer, ForeignKey("events.id"))
)