from app import create_app
import uvicorn

""" RUN FAST API. """
app = create_app()


@app.get('/', tags=['Home'])
def home():
    return ' Home Page - FAST API '


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
