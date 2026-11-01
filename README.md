# product-service

Sample product API with in-memory demo data

## Requirements
- Python 3.12
- pip
- Docker (for container build)
- Kubernetes and kubectl (for cluster deployment)

## Run locally
Create and activate a virtual environment (recommended), then install dependencies:

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

Test the API:
```bash
curl http://localhost:8000/api/products
curl http://localhost:8000/health
```

Interactive API documentation is available at `http://localhost:8000/docs`.

## Build and run with Docker
```bash
docker build -t product-service:1.0.0 .
docker run --rm -p 8000:8000 product-service:1.0.0
```

Then test `http://localhost:8000/api/products`.

## Deploy to Kubernetes
1. Update the image in `k8s/deployment.yaml` to your pushed registry image.
2. Build and push the image:
   ```bash
   docker tag product-service:1.0.0 YOUR_REGISTRY/product-service:1.0.0
   docker push YOUR_REGISTRY/product-service:1.0.0
   ```
3. Apply the manifests:
   ```bash
   kubectl apply -f k8s/
   kubectl rollout status deployment/product-service
   kubectl get pods,svc -l app=product-service
   ```
4. Test using port-forward:
   ```bash
   kubectl port-forward svc/product-service 8000:80
   curl http://localhost:8000/api/products
   ```

These are demo APIs with static/in-memory data only; no database is required.
