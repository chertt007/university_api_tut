from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_HOST: str = Field(
        default="localhost",
        validation_alias=AliasChoices("DATABASE_HOST", "POSTGRES_HOST"),
    )
    DATABASE_NAME: str = Field(
        default="university_api_db",
        validation_alias=AliasChoices("DATABASE_NAME", "POSTGRES_DB"),
    )
    DATABASE_USER: str = Field(
        default="university_api_user",
        validation_alias=AliasChoices("DATABASE_USER", "POSTGRES_USER"),
    )
    DATABASE_PASSWORD: str = Field(
        default="university_api_password",
        validation_alias=AliasChoices("DATABASE_PASSWORD", "POSTGRES_PASSWORD"),
    )

    model_config = SettingsConfigDict(extra="ignore")
    
settings = Settings()
