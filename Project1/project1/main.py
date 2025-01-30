from fastapi import FastAPI, requests, UploadFile, File
from fastapi.responses import JSONResponse
from project1.db import db
from project1.v1.Features.file.routes import router as file_router
from project1.v1.Features.verification.routes import router as verification_router


app = FastAPI()

# mandatory hello world route
@app.get("/hi")
async def root():
    return {"message": "Hello World"}

app.include_router(file_router, prefix="/file", tags=["file"])
app.include_router(verification_router, prefix="/api", tags=["verification"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)