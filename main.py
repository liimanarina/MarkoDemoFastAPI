from fastapi import FastAPI, Request, Form, Response, status, Depends, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="yes_its_secret")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Dummy credentials (replace with a real authentication system)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"
AUTH_COOKIE_NAME = "auth_token"

def is_authenticated(request: Request):
    if "user" in request.session:
        return request.session["user"] == VALID_USERNAME
    return False

@app.post("/login")
async def login(data: dict, request: Request, response: Response):
    """Handles login and sets the auth."""
    username = data.get("username")
    password = data.get("password")

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        request.session["user"] = username
        return JSONResponse(content={"success": True})
    
    return JSONResponse(content={"success": False}, status_code=401)

@app.get("/logout")
async def logout(request: Request, response: Response):
    """Clears the authentication and redirects to home."""
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    request.session["user"] = None
    return response

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Public route: Home page"""
    return templates.TemplateResponse('index.html', {"request": request})

@app.get("/protected", response_class=HTMLResponse)
async def protected_page(request: Request):
    """Protected route: Only accessible if logged in"""
    if not is_authenticated(request):
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    
    return templates.TemplateResponse('protected.html', {"request": request})

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
