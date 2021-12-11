import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get('/')
def index():
    return {
        'message': 'hello world',
        'status': 'ok'
    }


@app.get('/about')
def about():
    return {
        'message': 'this is the about page'
    }


uvicorn.run(app)
