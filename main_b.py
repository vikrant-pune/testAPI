from fastapi import FastAPI, Request
import time
from fastapi import Depends, FastAPI, Header, HTTPException
import uvicorn


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI()


# app = FastAPI()


# @app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


async def find_divisibles_a(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located

@app.get("/items/")
async def read_items(p1: int,p2: int ):
    foo = await find_divisibles_a(inrange=p1,div_by=p2)
    return [{"ans": foo}]


@app.get("/users/")
def read_users(p1: int, p2: int):
    foo = find_divisibles(inrange=p1, div_by=p2)
    return [{"ans": foo}]cd 
    
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
