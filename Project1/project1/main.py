from fastapi import FastAPI
from fastapi.responses import JSONResponse
from project1.db import db

app = FastAPI()

@app.get("/")
async def root():
    _, err = db.get_engine()
    if err is None:
        return JSONResponse(status_code=200, content={"message": "Connection to database established"})
    else:
        return JSONResponse(status_code=500, content={"message": "Connection to database failed",
                                                      "error": str(err)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)