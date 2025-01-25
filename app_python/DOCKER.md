# Docker Implementation Details

## Best Practices Applied

### 1. **Non-Root User**  

- Created a dedicated user `appuser` to avoid running as root.  
- Set ownership of `/app` to `appuser`.  

### 2. **Base Image**  

- Used `python:3.9-alpine3.15` for a lightweight, version-pinned base.  

### 3. **Layer Optimization**  

- Copied `requirements.txt` first to cache dependency installation.  
- Combined `RUN` commands to minimize layers.  

### 4. **Security**  

- Added `.dockerignore` to exclude sensitive/unnecessary files.  
- Installed dependencies with `--no-cache-dir` to reduce bloat.  

### 5. **Explicit Versioning**  

- Pinned Python and Alpine versions for reproducibility.  
