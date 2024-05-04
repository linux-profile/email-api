from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from app.core.database import Base, engine


class Email(Base):

    __tablename__ = 'email'

    id = Column(Integer, primary_key=True, nullable=False)
    body_text_plain = Column(String, nullable=True)
    body_text_html = Column(String, nullable=True)
    return_path = Column(String, nullable=True)
    delivered_to = Column(String, nullable=True)
    received = Column(String, nullable=True)
    dkim_signature = Column(String, nullable=True)
    received = Column(String, nullable=True)
    content_type = Column(String, nullable=True)
    date = Column(DateTime, nullable=True)
    from_who = Column(String, nullable=True)
    mime_version = Column(String, nullable=True)
    message_id = Column(String, nullable=True)
    subject = Column(String, nullable=True)
    reply_to = Column(String, nullable=True)
    precedence = Column(String, nullable=True)
    x_sg_eid = Column(String, nullable=True)
    x_sg_id = Column(String, nullable=True)
    to_who = Column(String, nullable=True)
    x_entity_id = Column(String, nullable=True)


Base.metadata.create_all(bind=engine)
