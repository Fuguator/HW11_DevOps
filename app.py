from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
async def greet():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "127.0.0.1"
    return {
        "message": "Hello, World!",
        "hostname": hostname,
        "ip_address": ip_address,
        "status": "running"
    }

@app.get("/health")
async def health():
    return "OK"

@app.get("/ready")
async def ready():
    return {"status": "oughsdoigsusdobi"}