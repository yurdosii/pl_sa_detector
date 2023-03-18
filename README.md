# pl_sa_detector
An API to detect political leaning (Pro-Ukrainian or Pro-Russian) and sentiment (Positive, Neutral, Negative) of the text message

Note: more info can be found on `api_service` and `ml_service` `README.md` files

---
## Running
### To run using docker-compose:
```
docker-compose build
docker-compose up
```
### To use `breakpoint()`
```
docker-compose build
docker-compose up
docker-compose run -p 8000:8000 --rm compose_ml_service
```

---

## Known issues
### scipy installation
Problem description:
```
ERROR: Dependency "OpenBLAS" not found, tried pkgconfig and framework
```
Fix (set env variables):
```
export LDFLAGS="-L/opt/homebrew/opt/openblas/lib"
export CPPFLAGS="-I/opt/homebrew/opt/openblas/include"
export PKG_CONFIG_PATH="/opt/homebrew/opt/openblas/lib/pkgconfig"
```
