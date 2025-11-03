from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import webhook, api

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:3000",  # React local
    "https://tu-frontend.vercel.app"  # Producción en Vercel (ajusta según tu dominio)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],              # Métodos permitidos (GET, POST, etc.)
    allow_headers=["*"],              # Headers permitidos
)

# Rutas
app.include_router(webhook.router)
app.include_router(api.router)
