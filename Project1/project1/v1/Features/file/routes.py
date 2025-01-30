from fastapi import APIRouter

router = APIRouter()

@router.post("/uplaod-file")
async def upload_file():
    return {"message": "File uploaded successfully"}