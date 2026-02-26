import cloudinary.uploader
from fastapi import UploadFile
import uuid

# ✅ This line is critical
from app.core import cloudinary_config

async def upload_image(file: UploadFile):

    contents = await file.read()

    result = cloudinary.uploader.upload(
        contents,
        folder="academic_portfolio",
        public_id=str(uuid.uuid4()),
        overwrite=True,
        resource_type="image"
    )

    return result.get("secure_url")