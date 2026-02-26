from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    Float,
    ForeignKey,
    DateTime,
    Enum,
    Index
)
from sqlalchemy.orm import relationship
from datetime import datetime
# from app.db.base import Base
from app.db.base_class import Base
import enum


# ---------------------------------------------------
# Publication Type Enum (Clean Separation)
# ---------------------------------------------------
class PublicationType(str, enum.Enum):
    journal = "journal"
    conference = "conference"


# ---------------------------------------------------
# Publication Model
# ---------------------------------------------------
class Publication(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)

    faculty_id = Column(
        Integer,
        ForeignKey("faculty.id"),
        nullable=False,
        index=True
    )

    title = Column(Text, nullable=False)
    authors = Column(Text, nullable=False)

    publication_type = Column(
        Enum(PublicationType, name="publication_type_enum"),
        nullable=False,
        index=True
    )

    journal_name = Column(String, nullable=True)
    publisher = Column(String, nullable=True)

    year = Column(Integer, index=True)
    volume = Column(String, nullable=True)
    issue = Column(String, nullable=True)
    pages = Column(String, nullable=True)

    doi = Column(String, nullable=True)
    impact_factor = Column(Float, nullable=True)

    is_scopus_indexed = Column(Boolean, default=False)
    is_web_of_science = Column(Boolean, default=False)

    pdf_url = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    faculty = relationship("Faculty", backref="publications")
    
    official_url = Column(String)
    cover_image = Column(String)
    abstract = Column(Text)


# ---------------------------------------------------
# Composite Index (Performance Optimization)
# ---------------------------------------------------
Index("ix_faculty_year", Publication.faculty_id, Publication.year)