from app.db.session import SessionLocal
from app.models.faculty import Faculty

db = SessionLocal()

faculty = Faculty(
    full_name="Dr. Arindam Biswas",
    designation="Associate Professor",
    department="Computer Science and Engineering",
    university="Kalyani University",
    email="example@email.com",
)

db.add(faculty)
db.commit()
db.refresh(faculty)

print("Faculty ID:", faculty.id)

db.close()
