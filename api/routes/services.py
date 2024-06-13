from fastapi import APIRouter

servicesRouter = APIRouter()


@servicesRouter.get('/ping')
async def ping():
    return {'message': 'pong'}
