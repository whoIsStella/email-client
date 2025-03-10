from fastapi import FastAPI
from routes import user_routes, email_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user_routes.router, prefix="/users")
app.use_router(emailRoutes.router)

app = FastAPI()
