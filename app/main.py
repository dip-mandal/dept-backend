from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from app.api.auth import router as auth_router
from app.core.auth_guard import get_current_user


from app.api.publications import router as publications_router
from app.api.projects import router as projects_router
from app.api.phd_students import router as phd_students_router
from app.api.books import router as books_router
from app.api.dashboard import router as dashboard_router
from app.api.awards import router as awards_router
from app.api.patents import router as patents_router

from app.api.upload import router as upload_router


from app.api.public import router as public_router

from app.api.faculty import router as faculty_router
from app.api.public_publications import router as public_publications_router
from app.api.public_books import router as public_books_router
from app.api.public_projects import router as public_projects_router
from app.api.public_patents import router as public_patents_router
from app.api.public_awards import router as public_awards_router





from app.api.gallery import router as gallery_router
from app.api.public_gallery import router as public_gallery_router



from app.api.contact_admin import router as contact_admin_router
from app.api.public_contact import router as public_contact_router




app = FastAPI(title="Academic Portfolio API")




app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://hodwebsite-6nvzjgpkh-dm9475511-9693s-projects.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





app.include_router(auth_router, prefix="/api")

app.include_router(publications_router, prefix="/api/publications", tags=["Publications"])

app.include_router(projects_router, prefix="/api/projects", tags=["Projects"])

app.include_router(phd_students_router, prefix="/api/phd-students", tags=["PhD Students"])

app.include_router(books_router, prefix="/api/books", tags=["Books"])

app.include_router(dashboard_router, prefix="/api/dashboard", tags=["Dashboard"])

app.include_router(awards_router, prefix="/api")

app.include_router(patents_router, prefix="/api/patents", tags=["Patents"])

app.include_router(upload_router, prefix="/api/upload", tags=["Upload"])

app.include_router(public_router, prefix="/api")

app.include_router(faculty_router, prefix="/api/faculty", tags=["Faculty"])

app.include_router(public_publications_router, prefix="/api")

app.include_router(public_books_router, prefix="/api/public", tags=["Public"])

app.include_router(public_projects_router, prefix="/api/public", tags=["Public"])

app.include_router(public_patents_router, prefix="/api/public", tags=["Public"])

app.include_router(public_awards_router, prefix="/api/public", tags=["Public"])






app.include_router(gallery_router, prefix="/api/gallery", tags=["Gallery"])
app.include_router(public_gallery_router, prefix="/api/public", tags=["Public"])


app.include_router(contact_admin_router, prefix="/api/contact", tags=["Contact Admin"])
app.include_router(public_contact_router, prefix="/api/public", tags=["Public"])



@app.get("/api/protected")
def protected_route(user: str = Depends(get_current_user)):
    return {"message": f"Hello {user}, you are authenticated"}
