# Barbería SaaS Backend

Este es el backend del sistema de gestión para barberías. Está construido con FastAPI y maneja la lógica de negocio y la persistencia de datos.

## Requisitos

- Python 3.12
- FastAPI
- Uvicorn
- PostgreSQL

## Configuración

Asegúrate de definir las variables de entorno `DATABASE_URL` y `CORS_ORIGINS` en tu archivo `.env` para que la aplicación pueda conectarse a la base de datos y permitir CORS desde el frontend.