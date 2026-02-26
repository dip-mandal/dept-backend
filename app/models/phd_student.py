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


class PhDStudent(Base):
    __tablename__ = "phd_students"

    id = Column(Integer, primary_key=True, index=True)

    faculty_id = Column(Integer, ForeignKey("faculty.id"), nullable=False)

    name = Column(String, nullable=False)
    thesis_title = Column(Text, nullable=False)

    university = Column(String)

    role = Column(String)  # Principal Supervisor / External Supervisor / Joint Supervisor

    award_date = Column(Date)

    status = Column(String)  # completed / ongoing
    
    profile_image = Column(String)   # Cloudinary URL
    bio = Column(Text)
    research_area = Column(String)

    faculty = relationship("Faculty", backref="phd_students")
