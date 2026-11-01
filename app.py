from fastapi import FastAPI

app = FastAPI(
    title="product-service",
    description="Sample product API with in-memory demo data",
    version="1.0.0",
)

@app.get("/health")
def health():
    return {"status": "UP", "application": "product-service"}

@app.get("/api/products")
def products():
    return [
        {"id": 1, "name": "Laptop", "price": 65000},
        {"id": 2, "name": "Keyboard", "price": 1800},
        {"id": 3, "name": "Mouse", "price": 900},
    ]

