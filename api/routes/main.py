from fastapi import APIRouter

from routes.users import usersRouter
from routes.services import servicesRouter
from routes.teams import teamsRouter

mainApiRouter = APIRouter()

mainApiRouter.include_router(usersRouter, prefix='/users')
mainApiRouter.include_router(servicesRouter, prefix='/services')
mainApiRouter.include_router(teamsRouter, prefix='/teams')
