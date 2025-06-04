from fastapi import FastAPI,Path,Query,Form,File,UploadFile,Header,Request,Response,Body, status, HTTPException
from typing import List

app = FastAPI()
# API that expects an integer in the last part of its path
@app.get("/users/{id}")
async def get_user(id: int):
    return {"id": id}

from enum import Enum
class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"
@app.get("/users/{type}/{id}/")
async def get_user(type: UserType, id: int):
    return {"type": type, "id": id}

@app.get("/users/{id}")
async def get_user(id: int = Path(..., ge=1)):
    return {"id": id}

@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(...,
regex=r"^\d{5}-\d{3}-\d{2}$")):
    return {"license": license}

# 05
@app.get("/users")
async def get_user(page: int = 1, size: int = 10):
    return {"page": page, "size": size}

#06
@app.get("/users")
async def get_user(page: int = Query(1, gt = 0),
size: int = Query(10, le = 100)):
    return {"page": page, "size": size}

#07
@app.post("/users")
async def create_user(name: str = Form(...),
age: int = Form(...)):
    return {"name": name, "age": age}

#08
@app.post("/files")
async def upload_file(file: UploadFile = File(...)):
    return {"file_name": file.filename,
            "content_type": file.content_type}

#09
@app.post("/uploadMultipleFiles")
async def upload_multiple_files(files: List[UploadFile]=File(...)):
    return [
        {"file_name": file.filename,
        "content_type": file.content_type}
        for file in files
    ]

#10
@app.get("/getHeader")
async def get_header(user_agent: str = Header(...)):
    return {"user_agent": user_agent}

#11
@app.get("/request")
async def get_request_object(request: Request):
    return {"path": request.url.path}

#12
@app.get("/setCookie")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name",
                        "cookie-value",
                        max_age=86400)
    return {"hello": "world"}

#13
@app.post("/password")
async def check_password(password: str = Body(...),
password_confirm: str = Body(...)):
    if password != password_confirm:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail="Passwords don't match.",
        )
    return {"message": "Passwords match."}