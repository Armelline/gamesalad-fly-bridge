FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENV PORT=8000 HOST=0.0.0.0
EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]