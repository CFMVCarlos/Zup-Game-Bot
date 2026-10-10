from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os

from src.services.automation import AutomationService

app = FastAPI(
    title="ZUP Automation API",
    description="A robust backend for managing the game automation process.",
    version="1.0.0"
)

# Initialize the core service
automation_service = AutomationService()

# Ensure directories exist
os.makedirs("src/static/css", exist_ok=True)
os.makedirs("src/static/js", exist_ok=True)
os.makedirs("src/templates", exist_ok=True)

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

class StandardResponse(BaseModel):
    status: str
    message: str

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Global exception handler to never expose stack traces to the client.
    """
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": "An internal server error occurred."}
    )

@app.get("/", response_class=HTMLResponse)
async def serve_frontend(request: Request):
    """
    Serves the main frontend UI.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/status")
async def get_status():
    """
    Returns the current status of the automation service.
    """
    try:
        return {"status": "success", "data": automation_service.get_status()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/start", response_model=StandardResponse)
async def start_automation():
    """
    Starts the automation sequence.
    """
    if automation_service.is_running:
        return JSONResponse(status_code=400, content={"status": "error", "message": "Automation is already running."})
    
    automation_service.start()
    return {"status": "success", "message": "Automation started successfully."}

@app.post("/api/stop", response_model=StandardResponse)
async def stop_automation():
    """
    Stops the automation sequence.
    """
    if not automation_service.is_running:
        return JSONResponse(status_code=400, content={"status": "error", "message": "Automation is not running."})
        
    automation_service.stop()
    return {"status": "success", "message": "Automation stopped successfully."}
