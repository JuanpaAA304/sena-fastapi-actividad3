from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilita CORS para permitir peticiones desde cualquier origen.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido..."}


@app.get("/item/{item_id}")
def read_item(item_id: int, q: str | None = None, activo: bool = True):
    return {"item_id": item_id, "q": q, "activo": activo}


@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"saludo": f"¡Hola, {nombre}!"}


@app.get("/config")
def config(modo: str = "produccion", version: float = 1.0):
    return {"modo": modo, "version": version}
