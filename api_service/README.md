# API service

### To run locally
```
poetry run uvicorn src.main:app --reload
```

### To run via Docker
```
docker build -t pl_sa_detector_api_service .
docker run -p 8000:8000 pl_sa_detector_api_service
```
