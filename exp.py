from app.db.session import SessionLocal
from app.models.user import User
from app.utils.security import hash_password

db = SessionLocal()

admin = User(
    username="admin",
    password_hash=hash_password("admin123"),
)

db.add(admin)
db.commit()
db.close()

print("Admin created")
