from fastapi import UploadFile, File
from project1.v1.request.type import File_request


# this is for uploading files and working with them

async def File_upload(
        metadata: File_request, UploadFile = File(...)):
    """
    This function is used to upload files
    """

    return {"filename": metadata.name}