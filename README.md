# 📦 WhatsApp Sentiment Dashboard – Backend

Este backend recibe mensajes de WhatsApp vía webhook, analiza su contenido emocional y temático, y los guarda en MongoDB para visualización en un dashboard React.

---

## 🚀 Funcionalidades actuales

- 📲 Recepción de mensajes desde Twilio WhatsApp
- 🧠 Análisis de sentimiento con OpenAI (`gpt-3.5-turbo`)
- 🔄 Fallback automático con:
  - 🤖 Transformers (`nlptown/bert-base-multilingual-uncased-sentiment`)
  - 🧪 TextBlob (análisis local)
- 🏷️ Detección de tema por palabras clave
- 🗃️ Almacenamiento estructurado en MongoDB
- 🔍 Trazabilidad del motor usado (`openai`, `transformers`, `textblob`)

---

## 🧠 Estructura del análisis

Cada mensaje se analiza y se guarda con esta estructura:

```json
{
  "texto_mensaje": "Estoy muy satisfecho con el servicio",
  "numero_remitente": "whatsapp:+50312345678",
  "timestamp": "2025-11-02T23:39:10.634Z",
  "sentimiento": "positivo",
  "tema": "Servicio al Cliente",
  "resumen": "Clasificado como 5 stars con 0.98 de confianza. Tema detectado: Servicio al Cliente.",
  "motor": "transformers"
}
## Configuracion inicial del proyecto
