from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    Date,
    Index
)
from sqlalchemy.orm import relationship
# from app.db.base import Base
from app.db.base_class import Base


class Patent(Base):
    __tablename__ = "patents"

    id = Column(Integer, primary_key=True, index=True)

    faculty_id = Column(Integer, ForeignKey("faculty.id"), nullable=False, index=True)

    title = Column(Text, nullable=False)

    patent_type = Column(String, index=True)  
    # domestic / international / copyright / design

    application_number = Column(String, index=True)
    registration_number = Column(String, index=True)

    filing_date = Column(Date)
    publication_date = Column(Date)
    issue_date = Column(Date)

    inventors = Column(Text)

    status = Column(String, index=True)  
    # filed / published / granted

    faculty = relationship("Faculty", backref="patents")


# Composite index for filtering
Index("ix_patent_type_status", Patent.patent_type, Patent.status)