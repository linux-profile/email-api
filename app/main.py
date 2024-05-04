from fastapi import FastAPI

from app import __version__
from app.api.v1.routers import v1


app = FastAPI(
    title="Email Profile API",
    description="Linux Profile Email Project API",
    version=__version__
)


app.include_router(v1, prefix="/v1")


@app.get("/status", include_in_schema=False)
def get_status():
    """Get status of messaging server."""
    return ({"status":  "it's alive"})


@app.get("/error", include_in_schema=False)
def get_status():
    """Get error of messaging server."""
    raise
