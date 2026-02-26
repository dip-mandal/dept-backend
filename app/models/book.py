import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
# from app.db.base import Base
from app.db.base_class import Base

class BookCategory(str, enum.Enum):
    authored = "authored"
    edited = "edited"
    monograph = "monograph"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    faculty_id = Column(Integer, ForeignKey("faculty.id"), nullable=False)

    title = Column(String, nullable=False)
    isbn = Column(String)
    publisher = Column(String)
    year = Column(Integer)
    doi = Column(String)
    cover_image = Column(String)

    category = Column(Enum(BookCategory), nullable=False)
    
    official_url = Column(String, nullable=True)

    faculty = relationship("Faculty", backref="books")
