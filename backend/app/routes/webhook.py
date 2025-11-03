from fastapi import APIRouter, Request
from app.services.ai_analysis import analizar_mensaje
from app.database import mensajes_collection
from datetime import datetime

router = APIRouter()

@router.post("/webhook")
async def recibir_mensaje(request: Request):
    form = await request.form()
    mensaje = form.get("Body")
    numero = form.get("From")
    timestamp = datetime.utcnow().isoformat()

    # Documento base
    doc = {
        "texto_mensaje": mensaje,
        "numero_remitente": numero,
        "timestamp": timestamp
    }

    # Análisis con IA
    enriquecido = analizar_mensaje(mensaje)

    # Actualizar documento con análisis
    doc.update(enriquecido)

    # Guardar en MongoDB
    mensajes_collection.insert_one(doc)

    return {"status": "ok", "mensaje": "Mensaje recibido y analizado"}
