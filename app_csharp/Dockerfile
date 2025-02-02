# Stage 1: Build the application
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

# Set working directory in container
WORKDIR /src

# 1. Copy the main project file first for better layer caching
COPY ["app_csharp/MoscowTimeApp/MoscowTimeApp.csproj", "MoscowTimeApp/"]
RUN dotnet restore "MoscowTimeApp/MoscowTimeApp.csproj"

# 2. Copy remaining source code
COPY app_csharp/MoscowTimeApp/ MoscowTimeApp/

# 3. Build specific project and publish
RUN dotnet publish "MoscowTimeApp/MoscowTimeApp.csproj" \
    -c Release \
    -o /app \
    --no-restore

# Stage 2: Runtime image
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app

# Copy build artifacts
COPY --from=build /app .

# Security enhancements
RUN adduser -u 5678 --disabled-password --gecos "" appuser && \
    chown -R appuser:appuser /app
USER appuser

# Runtime configuration
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS=http://+:80
EXPOSE 80
ENTRYPOINT ["dotnet", "MoscowTimeApp.dll"]