from fastapi import FastAPI, HTTPException
import asyncio  # Para el punto 5 (delay)

app = FastAPI()

# ==========================================================
# BASE DE DATOS SIMULADA Y CONTADOR (Punto 4)
# ==========================================================
clientes = [] 
contador_creaciones = 0  # Contador global de clientes creados

@app.get("/")
def home():
    return {
        "mensaje": "API del Banco funcionando",
        "total_creaciones_historicas": contador_creaciones
    }

# 1 y 5. CREAR CLIENTE CON VALIDACIÓN Y DELAY
@app.post("/clientes")
async def crear_cliente(nombre: str):
    global contador_creaciones
    
    # Punto 3: Validación básica (no permitir nombre vacío)
    if not nombre or nombre.strip() == "":
        raise HTTPException(status_code=400, detail="El nombre no puede estar vacío")

    # Punto 5: Simulación de delay asíncrono de 3 segundos
    await asyncio.sleep(3)

    cliente = {
        "id": len(clientes) + 1,
        "nombre": nombre
    }
    clientes.append(cliente)
    contador_creaciones += 1  # Punto 4: Incrementar contador
    return cliente

@app.get("/clientes")
def listar_clientes():
    return clientes

# Punto 2: Endpoint PUT para actualizar nombre
@app.put("/clientes/{cliente_id}")
def actualizar_cliente(cliente_id: int, nuevo_nombre: str):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            cliente["nombre"] = nuevo_nombre
            return {"mensaje": "Cliente actualizado", "cliente": cliente}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# Punto 1: Endpoint DELETE para eliminar cliente
@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    for i, cliente in enumerate(clientes):
        if cliente["id"] == cliente_id:
            cliente_eliminado = clientes.pop(i)
            return {"mensaje": "Cliente eliminado", "cliente": cliente_eliminado}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")