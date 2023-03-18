# pl_sa_detector
An API to detect political leaning (Pro-Ukrainian or Pro-Russian) and sentiment (Positive, Neutral, Negative) of the text message

Note: more info can be found on `api_service` and `ml_service` `README.md` files

---
## ML models
To detect the political leaning and sentiment of the text, 2 machine learning models were used.

They were implemented as part of the master diploma research where machine learning algorithms, neural networks, ensembles of models and different vectorization and imbalanced data techniques were applied.

As a result, the prediction of the text's political leaning involved Logistic Regression with TF-IDF vectorization, whereas, for sentiment analysis, LinearSVC and TF-IDF vectorization were used. More info can be found in this [repository](https://github.com/yurdosii/pl_sa_diploma).

---
## Running
### To run using docker-compose:
```
docker-compose build
docker-compose up
```

After this go to `http://127.0.0.1:8001/docs/` and `http://127.0.0.1:8002/docs/`.

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
