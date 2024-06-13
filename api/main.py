'''Main file, which starting an app'''

import uvicorn

from fastapi import FastAPI

from routes import mainApiRouter

if __name__ == '__main__':
    app = FastAPI()

    app.include_router(mainApiRouter, prefix='/api')

    uvicorn.run(app, host='0.0.0.0', port=8080)
