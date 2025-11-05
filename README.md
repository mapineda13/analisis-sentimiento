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
## 🔎 Configuraciones iniciales
- Twilio
  - Crear cuenta en Twilio: https://www.twilio.com/
  - Configurar sandbox para whatsapp
  - Configurar endpoint para recibir mensajes por parte de la api mediante "/webhook""
- MongoDB
  - Crear cuenta en atlas: https://www.mongodb.com/products/platform/atlas-database
  - Configurar cluster
  - Generar linea de conexion
- OPENIA
  - Crear cuenta en OPEN IA platform: https://openai.com/es-419/api/
  - Generar API KEY
  - Recargar saldo
- Ngrok
  - Crear cuenta de NGROK para poder exponer publicamente localhost y poder comunicarse con Twilio

---
## 🔎 Instalaciones iniciales del proyecto
- Frontend
  - Ejecutar desde carpeta raiz frontend el comando npm install para instalar librerias
  - Generar archivo .env
    - Crear variable de entorno REACT_APP_API_URL con direccion de api
  - Ejecutar comando npm start en carpeta raiz para levantar frontend 
- Backend
  - Crear entorno virtual en carpeta backend en python con comando python -m venv .venv
  - Generar archivo .env
    - Crear variables de entorno OPENAI_API_KEY y MONGO_URI con sus respectivos datos 
  - Activar entorno virtual
  - Instalar librerias con comando pip install -r requirements.txt
  - Levantar ambiente backend con comando uvicorn app.main:app --reload
  - Activar NGROK con comando ngrok http 8000

---
## 📚 Librerias utilizadas
Al ser un proyecto un poco sencillo decidi utilizar las siguientes librerias. Manteniendolo lo mas sencillo y liviando posible:

- Frontend
  - axios
  - bootstrap
  - chart.js
  - react-bootstrap
  - react-chartjs-2
  - react-scripts
- Backend
  - fastapi
  - openai
  - pymongo
  - python-dotenv
  - textblob
  - torch
  - transformers
  - uvicorn

Con sus respectivas dependecias.
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

