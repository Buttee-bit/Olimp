from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_start():
    return 'Start'