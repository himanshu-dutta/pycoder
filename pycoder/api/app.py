import pycoder.config as cfg
from pycoder.api.main import query
from pycoder.imports import FastAPI, create_task

app = FastAPI()


async def load_model_call():
    query(
        cfg,
        topics="python",
        description="a sample call to load the model",
        verbose=True,
    )


@app.get("/")
async def query_code(topics: str, description: str, prefix: str = ""):
    result = query(cfg, topics, description, prefix, True)

    return {"code": result}


@app.get("/load-model")
async def load_model():
    create_task(load_model_call())
    return {"status": "loading model..."}
