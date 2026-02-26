from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    Date
)
from sqlalchemy.orm import relationship
# from app.db.base import Base
from app.db.base_class import Base


class InvitedLecture(Base):
    __tablename__ = "invited_lectures"

    id = Column(Integer, primary_key=True, index=True)

    faculty_id = Column(Integer, ForeignKey("faculty.id"), nullable=False)

    title = Column(Text, nullable=False)

    event_name = Column(String)

    organizer = Column(String)

    event_date = Column(Date)

    role = Column(String)  # Invited Talk / Session Chair / Judge

    location = Column(String)

    description = Column(Text)

    faculty = relationship("Faculty", backref="invited_lectures")
