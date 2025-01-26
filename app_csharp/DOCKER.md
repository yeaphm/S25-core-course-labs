# Docker Implementation Details

## Best Practices Applied

### 1. **Multi-Stage Builds**  

- **Build Stage**: Used `mcr.microsoft.com/dotnet/sdk:6.0` to compile the app.  
- **Runtime Stage**: Used lightweight `mcr.microsoft.com/dotnet/aspnet:8.0` for production.  

### 2. **Non-Root User**  

- Created a dedicated user `appuser` to avoid running as root.  
- Set ownership of `/app` to `appuser`.  

### 3. **Layer Optimization**  

- Copied `.csproj` first to cache dependency restoration.  
- Separated `dotnet restore` and `dotnet publish` for efficient layer caching.  

### 4. **Security**  

- Added `.dockerignore` to exclude build artifacts and sensitive files.  

### 5. **Explicit Versioning**  

- Pinned .NET SDK and runtime to version `8.0`.  

---

## How to Build and Run

```bash
# Build the image
docker build -t dockerhub-username/moscow-time-csharp-app:latest .

# Run the container
docker run -p 8080:80 dockerhub-username/moscow-time-csharp-app:latest

#You can use mine:
docker run -p 8080:80 efimpuzhalov/moscow-time-csharp-app:latest
```

Access the app at `http://localhost:8080`.
