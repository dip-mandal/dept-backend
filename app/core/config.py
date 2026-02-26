from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str
    
    smtp_host: str
    smtp_port: int
    smtp_user: str
    smtp_password: str
    admin_email: str

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
