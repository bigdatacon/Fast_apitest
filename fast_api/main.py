import logging

# from alembic.config import Config
# from alembic.command import upgrade
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
#
# from api import layer, layer_type, dashboard, apitesting
#
# from db.db import engine, init_db
# from core.config import CORS_ORIGINS
# from core.logger import LOGGING
# from seeds.seeder import seed_db


# app = FastAPI(
#     title='Interactive Map',
#     description="Backend for Interactive Map",
#     docs_url='/api/openapi',
# )



# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=CORS_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# app.include_router(layer.router, prefix='/api/v1/layer')
# app.include_router(layer_type.router, prefix='/api/v1/layer_type')
# app.include_router(dashboard.router, prefix='/api/v1/dashboard')





# @app.on_event('startup')
# async def startup():
#     init_db()
#     # upgrade(Config("./alembic.ini"), "head")
#     seed_db()



import uvicorn
from core.logger import LOGGING
from fastapi import FastAPI
from api import apitesting


app = FastAPI()
app.include_router(apitesting.router, prefix='/api/v1/apitesting')

def main() -> None:
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,  # TODO set level through env var
    )


if __name__ == '__main__':
    main()