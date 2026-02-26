from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
# from app.db.base import Base
from app.db.base_class import Base


class Faculty(Base):
    __tablename__ = "faculty"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    designation = Column(String)
    department = Column(String)
    university = Column(String)
    email = Column(String)
    bio = Column(Text)
    
    profile_image = Column(String)

    awards = relationship("Award", back_populates="faculty", cascade="all, delete-orphan")