from pycoder.api.main import query
from pycoder.imports import (
    run,
    Path,
    FastAPI,
    highlight,
    PythonLexer,
    create_task,
    HTMLResponse,
    HtmlFormatter,
)

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
    code = query(topics, description, prefix, max_length, verbose=True)
    code = highlight(code, PythonLexer(), HtmlFormatter())
    return {"code": code}


@app.get("/load-model")
async def load_model():
    create_task(load_model_call())
    return {"status": "loading model..."}


@app.get("/", response_class=HTMLResponse)
async def home():
    create_task(load_model_call())

    HOME_HTML = Path(__file__).parent.absolute() / "index.html"
    print(HOME_HTML)

    if HOME_HTML.exists():
        with HOME_HTML.open() as f:
            body = f.read()
    else:
        body = "not found :("
    return body


def main():
    run(app, host="127.0.0.1", log_level="info")
