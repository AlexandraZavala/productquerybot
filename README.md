# ProductQueryBot

## Requisitos
- Python 3.10+
- pip
- Docker 

## Instalación
1. Clona el repositorio :
	```sh
	git clone <repo-url>
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
python app/rag/indexer.py
```
Esto procesará `document_corpus.txt` y almacenará los vectores en `vector_store`.

## Ejecutar la API
Puedes iniciar la API con FastAPI:
```sh
python -m app.main
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

## Testing
### Pruebas unitarias
Ejecuta los tests con pytest:
```sh
pytest
```
O usando Docker:
```sh
docker compose --profile tests up --build
```


