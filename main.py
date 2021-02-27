from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from fastapi import FastAPI, Form, Body

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


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail={"disMsg": "Search somewhere else"})
    return {"item": items[item_id]}
