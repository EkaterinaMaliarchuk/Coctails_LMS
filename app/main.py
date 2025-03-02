from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# Create a FastAPI instance
app = FastAPI()

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.utils import ask_llm  # Import the ask_llm function from utils.py

# Create a FastAPI instance
app = FastAPI()

# Mount static files (CSS, JS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize templates (HTML files)
templates = Jinja2Templates(directory="templates")

# Define a Pydantic model for the user query
class UserQuery(BaseModel):
    question: str

# Root route: serves the main HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Example API endpoint: returns a simple JSON response
@app.get("/api/hello")
async def hello():
    return {"message": "Hello, World!"}

# API endpoint to handle user questions
@app.post("/api/ask")
async def ask_question(query: UserQuery):
    question = query.question
    # Use the ask_llm function to generate a response
    response = ask_llm(question)
    return {"response": response}