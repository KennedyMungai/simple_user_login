"""The main file for the app"""
from fastapi import FastAPI


app = FastAPI(title='Simple User Authentication', description="A simple user authentication backend")


@app.get("/", name="Root", description="The root endpoint for the app", response_model=dict[str, str])
async def root_endpoint() -> dict[str, str]:
    """The root endpoint for the app

    Returns:
        dict[str, str]: A simple message
    """
    return {"message": "Hello World"}