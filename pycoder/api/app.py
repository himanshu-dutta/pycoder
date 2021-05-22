from pycoder.api.main import query
from pycoder.imports import FastAPI, create_task, run

app = FastAPI()


async def load_model_call():
    query(
        topics="python",
        description="a sample call to load the model",
        verbose=True,
    )


@app.get("/query-code")
async def query_code(
    topics: str, description: str, prefix: str = "", max_length: int = 200
):
    result = query(topics, description, prefix, max_length, verbose=True)

    return {"code": result}


@app.get("/load-model")
async def load_model():
    create_task(load_model_call())
    return {"status": "loading model..."}


def main():
    run(app, host="127.0.0.1", log_level="info")
