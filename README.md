# ProductQueryBot

## Requisitos
- Python **3.10+**
- `pip`
- **Docker** y **Docker Compose**

## 📦 Instalación local

1. Clona el repositorio:
   ```sh
   git clone <repo-url>
   cd productquerybot
	```
2. Crea y activa un entorno virtual:
	```sh
	python -m venv venv
	.\venv\Scripts\activate  # En Windows
	```
3. Instala dependencias:
	```sh
	pip install -r requirements.txt
	```

## Indexar el corpus
Antes de consultar, indexa el corpus de productos:
```sh
python -m app/rag/indexer.py
```
Esto procesará `document_corpus.txt` y almacenará los vectores en `vector_store`.

## Ejecutar la API
Puedes iniciar la API con FastAPI:
```sh
python -m uvicorn app.main:app --reload
```
La API estará disponible en [http://localhost:8000/query](http://localhost:8000/query).

### Ejemplo de consulta
Envía un POST a `/query` con JSON:
```json
{
  "user_id": "usuario1",
  "query": "estoy buscando laptops"
}
```

# 📦 Ejecutar con docker

1. Construye y levanta el servicio:
	```sh
	docker compose --profile api up --build
	```
2. Envía una consulta de ejemplo:
	```sh
	curl -X POST http://localhost:8000/query \
    -H "Content-Type: application/json" \
    -d '{"user_id":"demo","query":"Estoy buscando laptops"}'
	```




## Testing
### Pruebas unitarias
Ejecuta los tests con pytest:
```sh
pytest -m pytest  -q
```
O usando Docker:
```sh
docker compose --profile tests up --build
```


