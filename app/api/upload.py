from fastapi import APIRouter, UploadFile, File, Depends
from app.utils.upload import upload_image
from app.core.auth_guard import get_current_user

router = APIRouter()

@router.post("/image")
async def upload_image_endpoint(
    file: UploadFile = File(...),
    user: str = Depends(get_current_user)
):
    image_url = await upload_image(file)
    return {"url": image_url}