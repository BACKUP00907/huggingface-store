from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    f = open("cache.txt","r")
    x = f.read()
    f.close()
    return x
