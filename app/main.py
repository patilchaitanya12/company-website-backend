from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, contact, projects, services
from app.config.settings import settings

app = FastAPI(
    title="RKH Automation API",
    description="Backend API for RKH Automation company website. Manages projects, services, gallery, and contact inquiries.",
    version="1.0.0",
    contact={
        "name": "RKH Automation",
        "email": "email@rkhautomation.com",
    },
    license_info={
        "name": "Private",
    },
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(services.router)
app.include_router(contact.router)


@app.get("/", tags=["health"])
def root():
    return {"message": "RKH Automation API", "docs": "/docs"}


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}