"""Data convert API inferece server.

- Author: Minki Lee
- Email: minki@annotation-ai.com
"""
import sys

import uvicorn
from fastapi import FastAPI
from src.controllers import test


sys.path.insert(0, "src")


# pylint: disable=invalid-name,unused-argument
def create_app() -> FastAPI:
    """Create a fastapi app instance."""
    app_instance = FastAPI()
    app_instance.include_router(test.router)

    return app_instance

app = create_app()

@app.get("/healthcheck")
def healthcheck() -> bool:
    """Healthcheck api."""
    return True


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=51234, reload=True)
