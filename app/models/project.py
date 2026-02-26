from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
# from app.db.base import Base
from app.db.base_class import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    faculty_id = Column(Integer, ForeignKey("faculty.id"), nullable=False, default=1)

    title = Column(String, nullable=False)
    funding_agency = Column(String)
    amount = Column(Float)
    role = Column(String)
    duration = Column(String)   # ✅ ADD THIS
    status = Column(String)
    description = Column(Text)

    faculty = relationship("Faculty", backref="projects")
