from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("int/{num}")
def read_item(num: int):
    return {"int": num}

@app.get("/float/{float}")
def read_float(float: float):
    return {"float": float}


@app.get("/")
def read_root():
   return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
    #uvicorn.run("API:app", host="localhost", port=8000, reload=True)