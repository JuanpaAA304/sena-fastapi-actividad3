# sena-fastapi-actividad3

API mínima con FastAPI que demuestra rutas básicas, parámetros de ruta y de consulta. Incluye CORS abierto para facilitar pruebas desde cualquier origen y cubre los 10 casos solicitados.

## Requisitos
- Python 3.10+
- fastapi y uvicorn: `pip install fastapi uvicorn`

## Ejecutar localmente
1. Instala dependencias: `pip install fastapi uvicorn`
2. Inicia el servidor: `uvicorn main:app --reload`
3. Abre el navegador en `http://localhost:8000` para ver el estado y en `http://localhost:8000/docs` para la documentación interactiva.

## Endpoints
- `GET /` → `{"mensaje": "Bienvenido..."}`
- `GET /item/{item_id}` con opcionales `q` (str | None) y `activo` (bool, por defecto `true`). Ejemplos:
	- `/item/42` → `{"item_id": 42, "q": null, "activo": true}`
	- `/item/10?q=busqueda&activo=false` → `{"item_id": 10, "q": "busqueda", "activo": false}`
	- `/item/0?q=&activo=true` → `{"item_id": 0, "q": "", "activo": true}`
	- `/item/-7` → `{"item_id": -7, "q": null, "activo": true}`
- `GET /saludo/{nombre}` devuelve un saludo: ej. `/saludo/María` → `{"saludo": "¡Hola, María!"}`; `/saludo/José%20Luis` → `{"saludo": "¡Hola, José Luis!"}`
- `GET /config` con opcionales `modo` (str, por defecto `produccion`) y `version` (float, por defecto `1.0`). Ejemplos:
	- `/config` → `{"modo": "produccion", "version": 1.0}`
	- `/config?modo=dev&version=2.5` → `{"modo": "dev", "version": 2.5}`
	- `/config?modo=test&version=abc` → devuelve **422 Unprocessable Entity** por error de tipo en `version`.

## Notas
- La app incluye `CORSMiddleware` con orígenes abiertos para facilitar pruebas cruzadas.
- Todas las respuestas usan tipos simples (`str`, `int`, `float`, `bool`) sin modelos Pydantic.