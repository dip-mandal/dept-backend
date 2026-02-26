from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Award(Base):
    __tablename__ = "awards"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    organization = Column(String, nullable=False)
    award_date = Column(Date, nullable=False)
    description = Column(Text, nullable=True)

    faculty_id = Column(Integer, ForeignKey("faculty.id"), nullable=False)

    faculty = relationship("Faculty", back_populates="awards")