# 🚀 EduRecom - Despliegue en Railway

## Configuración Rápida

### 1. Subir a GitHub
```bash
git add .
git commit -m "Configuración para Railway"
git push origin main
```

### 2. Crear Proyecto en Railway
1. Ve a [railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub repo"
3. Selecciona tu repositorio

### 3. Configurar Variables
En Railway → Variables:
```
SECRET_KEY=tu-clave-secreta-aqui
SESSION_SECRET=tu-session-secret-aqui
```

### 4. Agregar MySQL
1. "+ New" → "Database" → "MySQL"
2. Railway configurará `DATABASE_URL` automáticamente

### 5. Inicializar Base de Datos
En Railway Console:
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
python create_admin.py admin admin@ejemplo.com password123
```

## Archivos de Configuración

- `Procfile`: Configuración de Railway
- `railway.json`: Configuración avanzada
- `requirements.txt`: Dependencias optimizadas
- `env.example`: Variables de entorno

## URLs
- **App**: `https://tu-proyecto.railway.app`
- **Admin**: `https://tu-proyecto.railway.app/admin`

¡Listo! 🎉
