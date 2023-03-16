# pl_sa_detector
An API to detect political leaning (pro-ukrainian or pro-russian) and sentiment (positive, neutral, negative)

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
