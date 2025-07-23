from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes.register import router as register_router
from app.database.connection import Base, engine

# Create tables in DB
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount static files (CSS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Template config
templates = Jinja2Templates(directory="templates")

# Register routes
app.include_router(register_router)

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
