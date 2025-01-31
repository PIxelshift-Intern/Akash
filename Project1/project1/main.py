from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from project1.db import db
from project1.v1.Features.file.routes import router as file_router
from project1.v1.Features.verification.routes import router as verification_router
from project1.v1.request.type import Login,Register
from project1.functions import login,register

app = FastAPI()

# mandatory hello world route
@app.get("/hi")
async def root():
    return {"message": "Hello World"}

# Basic authentication route
@app.post("/v1/login")
async def login_route(data: Login):
    """
    Handle login requests.
    
    Args:
        data (Login): Validated request data from Pydantic model
        
    Returns:
        dict: User profile data if login successful
    """
    try:
        result = await login(data.username, data.password)
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Login failed: {str(e)}"
        )

@app.post("/v1/register")
async def register_route(data: Register):
    """
    Handle registration requests.
    
    Args:
        data (Register): Validated request data from Pydantic model
        
    Returns:
        dict: Registration status and verification details
    """
    try:
        result = await register(data.username, data.password, data.email)
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Registration failed: {str(e)}"
        )
    

# include routers
app.include_router(
    file_router, prefix="/file",
    tags=["file"])

app.include_router(
    verification_router, prefix="/api",
    tags=["verification"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)