from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT

from auth_routes import auth_router
from order_routes import order_router
from schemas import Settings

app = FastAPI()


@AuthJWT.load_config  # create an instance to using our secret token in schemas
def get_config():
    return Settings()


app.include_router(auth_router)
app.include_router(order_router)
