from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    # FastAPI will convert this to JSON for us
    return {"message": "Hello World!"}
