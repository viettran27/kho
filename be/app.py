import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config.config import settings
from controller.router import router
from fastapi import FastAPI

def get_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(router, prefix=settings.API_PREFIX)

    return application


app = get_application()

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')