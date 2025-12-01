from fastapi import FastAPI, Response
import os
import socket

app = FastAPI()

@app.get("/")
def greet():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {"message": "Hello, World!", "hostname": hostname, "ip_address": ip_address}

