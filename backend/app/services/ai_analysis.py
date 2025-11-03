import os
from dotenv import load_dotenv
from textblob import TextBlob
from openai import OpenAI, RateLimitError, APIError
from transformers import pipeline

load_dotenv()

# Inicializa clientes
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def detectar_tema(texto):
    texto_lower = texto.lower()
    if "precio" in texto_lower or "caro" in texto_lower or "barato" in texto_lower:
        return "Precio"
    elif "atención" in texto_lower or "servicio" in texto_lower or "trato" in texto_lower:
        return "Servicio al Cliente"
    elif "producto" in texto_lower or "calidad" in texto_lower or "café" in texto_lower:
        return "Calidad del Producto"
    elif "limpio" in texto_lower or "sucio" in texto_lower or "higiene" in texto_lower:
        return "Limpieza"
    else:
        return "Otro"

def analizar_mensaje(texto):
    prompt = f"""
    Analiza este mensaje de cliente: "{texto}"
    Devuelve un JSON con:
    - sentimiento: positivo, negativo o neutro
    - tema: Servicio al Cliente, Calidad del Producto, Precio, Limpieza u Otro
    - resumen: breve explicación del mensaje
    """

    # 🔹 Intento principal con OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return eval(response.choices[0].message.content)

    # 🔸 Fallback con Transformers si OpenAI falla
    except (RateLimitError, APIError, Exception) as e:
        print("⚠️ OpenAI falló, usando Transformers:", e)
        try:
            resultado = sentiment_pipeline(texto)[0]
            label = resultado["label"]  # Ej. '5 stars'
            score = round(resultado["score"], 2)

            if "4" in label or "5" in label:
                sentimiento = "positivo"
            elif "1" in label or "2" in label:
                sentimiento = "negativo"
            else:
                sentimiento = "neutro"

            tema = detectar_tema(texto)
            return {
                "sentimiento": sentimiento,
                "tema": tema,
                "resumen": f"Clasificado como {label} con {score} de confianza. Tema detectado: {tema}.",
                "motor": "Texblob"
            }

        # 🔻 Fallback final con TextBlob si Transformers también falla
        except Exception as e2:
            print("⚠️ Transformers falló, usando TextBlob:", e2)
            blob = TextBlob(texto)
            polaridad = blob.sentiment.polarity
            sentimiento = "positivo" if polaridad > 0 else "negativo" if polaridad < 0 else "neutro"
            tema = detectar_tema(texto)

            return {
                "sentimiento": sentimiento,
                "tema": tema,
                "resumen": f"Polaridad: {polaridad:.2f} según TextBlob. Tema detectado: {tema}.",
                "motor": "transformers"
            }
