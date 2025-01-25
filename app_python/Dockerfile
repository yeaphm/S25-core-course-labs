FROM python:3.9-alpine3.15

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser -D appuser && \
    mkdir /app && \
    chown appuser:appuser /app
USER appuser
WORKDIR /app

COPY --chown=appuser:appuser requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary application files (explicitly listed)
COPY --chown=appuser:appuser app.py .

EXPOSE 5000
CMD ["python", "app.py"]