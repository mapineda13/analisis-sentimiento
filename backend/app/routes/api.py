from fastapi import APIRouter
from app.database import mensajes_collection

router = APIRouter()

@router.get("/api/sentimientos")
def obtener_sentimientos():
    """
    Devuelve un diccionario con el conteo de mensajes por sentimiento.
    """
    pipeline = [
        {"$group": {"_id": "$sentimiento", "count": {"$sum": 1}}}
    ]
    resultados = mensajes_collection.aggregate(pipeline)
    return {r["_id"]: r["count"] for r in resultados}

@router.get("/api/temas")
def obtener_temas():
    """
    Devuelve un diccionario con el conteo de mensajes por tema.
    """
    pipeline = [
        {"$group": {"_id": "$tema", "count": {"$sum": 1}}}
    ]
    resultados = mensajes_collection.aggregate(pipeline)
    return {r["_id"]: r["count"] for r in resultados}

@router.get("/api/mensajes")
def obtener_mensajes():
    """
    Devuelve los últimos 20 mensajes analizados con sentimiento, tema y resumen.
    """
    cursor = mensajes_collection.find(
        {},
        {"_id": 0, "texto_mensaje": 1, "numero_remitente": 1, "timestamp": 1, "sentimiento": 1, "tema": 1, "resumen": 1}
    ).sort("timestamp", -1).limit(20)
    return list(cursor)
