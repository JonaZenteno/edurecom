# 🚀 Guía de Despliegue en Railway - EduRecom

Esta guía te llevará paso a paso para desplegar tu aplicación EduRecom en Railway con MySQL.

## 📋 Prerrequisitos

- Cuenta en [Railway](https://railway.app)
- Cuenta en [GitHub](https://github.com) (recomendado)
- Tu proyecto subido a un repositorio de GitHub

## 🛠️ Preparación del Proyecto

### 1. Estructura de Archivos Creada

El proyecto ya está configurado con los siguientes archivos:

```
edurecom-master/
├── Procfile                 # Configuración de Railway
├── railway.json            # Configuración avanzada de Railway
├── requirements.txt        # Dependencias optimizadas
├── env.example            # Variables de entorno de ejemplo
├── app.py                 # Punto de entrada de la aplicación
├── __init__.py            # Configuración de Flask y base de datos
└── ... (resto de archivos)
```

### 2. Verificar Configuración

- ✅ **Procfile**: Configurado para usar Gunicorn
- ✅ **requirements.txt**: Optimizado para producción
- ✅ **Base de datos**: Configurada para MySQL con soporte para Railway
- ✅ **Variables de entorno**: Preparadas para Railway

## 🚀 Despliegue en Railway

### Paso 1: Crear Proyecto en Railway

1. Ve a [railway.app](https://railway.app)
2. Inicia sesión con tu cuenta
3. Haz clic en **"New Project"**
4. Selecciona **"Deploy from GitHub repo"**
5. Conecta tu cuenta de GitHub si no lo has hecho
6. Selecciona tu repositorio `edurecom-master`

### Paso 2: Configurar Variables de Entorno

1. En tu proyecto de Railway, ve a la pestaña **"Variables"**
2. Agrega las siguientes variables:

```
SECRET_KEY=tu-clave-secreta-muy-segura-aqui
SESSION_SECRET=tu-session-secret-aqui
```

**Importante**: Genera claves seguras usando:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Paso 3: Agregar Base de Datos MySQL

1. En tu proyecto de Railway, haz clic en **"+ New"**
2. Selecciona **"Database"**
3. Elige **"MySQL"**
4. Railway creará automáticamente la base de datos y configurará `DATABASE_URL`

### Paso 4: Configurar el Servicio Web

1. Railway detectará automáticamente que es una aplicación Python
2. Usará el `Procfile` para iniciar la aplicación
3. La aplicación se desplegará automáticamente

### Paso 5: Verificar el Despliegue

1. Ve a la pestaña **"Deployments"**
2. Espera a que el despliegue termine (estado "Success")
3. Haz clic en el dominio generado para ver tu aplicación

## 🔧 Configuración de la Base de Datos

### Conexión Automática

Railway configurará automáticamente la variable `DATABASE_URL` con el formato:
```
mysql://usuario:password@host:puerto/nombre_bd
```

### Inicializar la Base de Datos

Una vez desplegada, necesitas crear las tablas. Puedes hacerlo de dos formas:

#### Opción 1: Desde la Consola de Railway

1. Ve a tu proyecto en Railway
2. Haz clic en el servicio web
3. Ve a la pestaña **"Console"**
4. Ejecuta:

```bash
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('Tablas creadas exitosamente')"
```

#### Opción 2: Crear Usuario Administrador

```bash
python create_admin.py admin admin@ejemplo.com password123
```

## 📊 Monitoreo y Logs

### Ver Logs en Tiempo Real

1. En Railway, ve a tu servicio web
2. Pestaña **"Logs"**
3. Verás los logs en tiempo real

### Métricas de la Aplicación

- **CPU**: Uso de procesador
- **Memoria**: Uso de RAM
- **Red**: Tráfico de red
- **Base de datos**: Conexiones activas

## 🔄 Actualizaciones

### Desplegar Cambios

1. Haz `git push` a tu repositorio
2. Railway detectará los cambios automáticamente
3. Iniciará un nuevo despliegue
4. La aplicación se actualizará sin tiempo de inactividad

### Rollback

Si algo sale mal:
1. Ve a **"Deployments"**
2. Selecciona una versión anterior
3. Haz clic en **"Redeploy"**

## 🛡️ Configuración de Seguridad

### Variables de Entorno Sensibles

Nunca subas archivos `.env` con credenciales reales. Railway maneja esto automáticamente.

### HTTPS

Railway proporciona HTTPS automáticamente para todos los dominios.

## 🐛 Solución de Problemas

### Error de Conexión a Base de Datos

1. Verifica que `DATABASE_URL` esté configurada
2. Revisa los logs para errores específicos
3. Asegúrate de que el servicio MySQL esté activo

### Error de Dependencias

1. Verifica que `requirements.txt` esté actualizado
2. Revisa los logs de build
3. Asegúrate de que todas las dependencias estén disponibles

### Error de Puerto

Railway usa la variable `PORT` automáticamente. No necesitas configurarla.

## 📈 Escalabilidad

### Planes de Railway

- **Hobby**: Gratuito, perfecto para desarrollo
- **Pro**: Para aplicaciones en producción
- **Team**: Para equipos

### Recursos

- **CPU**: 1 vCPU (Hobby) / 2 vCPU (Pro)
- **RAM**: 1GB (Hobby) / 2GB (Pro)
- **Almacenamiento**: 1GB (Hobby) / 8GB (Pro)

## 🔗 URLs Importantes

- **Aplicación**: `https://tu-proyecto.railway.app`
- **Panel de Railway**: `https://railway.app/dashboard`
- **Logs**: Disponibles en el panel de Railway
- **Base de datos**: Configurada automáticamente

## ✅ Checklist de Despliegue

- [ ] Proyecto subido a GitHub
- [ ] Proyecto creado en Railway
- [ ] Variables de entorno configuradas
- [ ] Base de datos MySQL agregada
- [ ] Aplicación desplegada exitosamente
- [ ] Tablas de base de datos creadas
- [ ] Usuario administrador creado
- [ ] Aplicación accesible desde el navegador

## 🆘 Soporte

Si tienes problemas:

1. Revisa los logs en Railway
2. Verifica la configuración de variables de entorno
3. Asegúrate de que la base de datos esté activa
4. Consulta la [documentación de Railway](https://docs.railway.app)

---

¡Tu aplicación EduRecom estará lista para usar en Railway! 🎉
