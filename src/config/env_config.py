from pydantic_settings import BaseSettings

class EnvironmentConfig(BaseSettings):
    env: str
    grpc_url: str

    class Config:
        env_file = ".env"

config = EnvironmentConfig()