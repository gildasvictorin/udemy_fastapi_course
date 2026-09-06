from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .database import engine
from .models import Base
from .routers import auth, todos, admin, users
from fastapi.staticfiles import StaticFiles



app = FastAPI()

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(
    directory=str(Path(__file__).resolve().parent / "templates")
)

app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")




@app.get("/")
def test(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"request": request},
    )

@app.get("/healthy")
def health_check():
    return {"status": "healthy"}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)










