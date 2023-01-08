"""
The main module for creating the application logic.
"""

from fastapi import FastAPI, Depends
import models
from database import engine
from routers import auth, todos, users
from company import companyapis, dependencies

# initiating the app
app = FastAPI()

# this will create todos.db file with tables and columns when we run the app
models.Base.metadata.create_all(bind=engine)

# our auth and todos endpoints will be added to our main app, we added routers
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
app.include_router(
    companyapis.router,
    prefix="/companyapis",
    tags=['companyapis'],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={418: {"description": "Internal use only"}}
)
