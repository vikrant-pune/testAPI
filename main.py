from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from fastapi import FastAPI, Form, Body, Request

app = FastAPI()


@app.post("/login/")
async def login(username: str = Body(...), password: str = Body(...)):
    return {"username": username}


# app = FastAPI()


@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    """ Has a byte opbjects
    """
    # with open(files, 'r') as file_obj:
    #     data = file_obj.read()

    # return {"file_sizes": [len(files)],
    #         "data" : files}

    return {#"filenames": [len(file) for file in files],
            "data": [file for file in files]
            }

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    """ has File object
    """
    return {"filenames": [file.filename for file in files],
            "data": [file for file in files ]
    }


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


items = {"foo": "The Foo Wrestlers"}


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id in ("foo3"):
        raise UnicornException(item_id)
    if item_id not in items:
        raise HTTPException(status_code=404, detail={"disMsg": "Search somewhere else"},
                            headers={"X-Error": "There goes my error"},
                            )
    return {"item": items[item_id]}
