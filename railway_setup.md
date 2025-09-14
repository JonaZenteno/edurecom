# Configuración de Railway para Persistencia de Datos

## 🚨 Problema Identificado

Con SQLite en Railway, la base de datos se reinicia en cada despliegue, perdiendo todos los usuarios y datos.

## ✅ Soluciones Implementadas

### 1. **Base de Datos Persistente**
- ✅ Configurado SQLite en directorio `/tmp` que es más persistente en Railway
- ✅ Detección automática del entorno Railway
- ✅ Fallback a directorio local para desarrollo

### 2. **Usuario Administrador Automático**
- ✅ Se crea automáticamente en cada inicialización
- ✅ Credenciales: `admin` / `admin123`
- ✅ Perfil completo de administrador

### 3. **Usuarios de Prueba**
- ✅ Se crean automáticamente usuarios de prueba
- ✅ Diferentes perfiles para testing
- ✅ Grupos de formación variados

### 4. **Sistema de Backup/Restore**
- ✅ Script para hacer backup de la base de datos
- ✅ Exportación a JSON para portabilidad
- ✅ Restauración desde JSON

## 🔧 Configuración de Railway

### Variables de Entorno Recomendadas

Agregar estas variables en Railway:

```bash
# Para persistencia de base de datos
RAILWAY_ENVIRONMENT=production

# Para seguridad
SESSION_SECRET=tu_clave_secreta_muy_larga_y_segura

# Opcional: Base de datos externa (recomendado para producción)
# DATABASE_URL=postgresql://usuario:password@host:puerto/database
```

### Comando de Inicio Actualizado

```bash
python init_db.py && python check_courses.py && python create_test_users.py && gunicorn --bind 0.0.0.0:$PORT app:app
```

## 👑 Usuario Administrador

**Credenciales por defecto:**
- **Usuario**: `admin`
- **Contraseña**: `admin123`
- **Email**: `admin@edurecom.com`

⚠️ **IMPORTANTE**: Cambiar la contraseña en producción

## 🧪 Usuarios de Prueba

Se crean automáticamente:

1. **testuser1** / `test123`
   - Rol: Profesor
   - Habilidades: Básicas (2/5)
   - Grupo esperado: Alfabetización Digital Básica

2. **testuser2** / `test123`
   - Rol: Director
   - Habilidades: Avanzadas (4/5)
   - Grupo esperado: Habilidades Digitales Avanzadas

3. **testuser3** / `test123`
   - Rol: Profesor
   - Habilidades: Intermedias (3/5)
   - Interés: Liderazgo
   - Grupo esperado: Fortalecimiento Institucional

## 📊 Flujo de Inicialización

1. **Crear tablas** de base de datos
2. **Crear usuario administrador** si no existe
3. **Cargar cursos** desde JSON
4. **Crear usuarios de prueba** si no existen
5. **Iniciar aplicación**

## 🔄 Backup y Restore

### Hacer Backup
```bash
python backup_restore.py backup
```

### Restaurar desde JSON
```bash
python backup_restore.py restore backups/edurecom_data_20240101_120000.json
```

## 🎯 Próximos Pasos

1. **Configurar variables de entorno** en Railway
2. **Hacer commit y push** de los cambios
3. **Desplegar en Railway**
4. **Verificar logs** para confirmar inicialización
5. **Probar con usuario administrador**: `admin` / `admin123`
6. **Probar con usuarios de prueba**

## 🔍 Verificación

Los logs deberían mostrar:
- ✅ Base de datos inicializada
- ✅ Usuario administrador creado
- ✅ Cursos cargados
- ✅ Usuarios de prueba creados
- ✅ Aplicación iniciada

## 🚨 Recomendaciones para Producción

1. **Usar base de datos externa** (PostgreSQL) en lugar de SQLite
2. **Cambiar contraseñas por defecto**
3. **Configurar variables de entorno seguras**
4. **Hacer backups regulares**
5. **Monitorear logs de Railway**

## 📝 Notas Importantes

- Los datos se mantendrán entre reinicios de la aplicación
- Los datos se perderán solo si Railway reinicia el contenedor completamente
- Para máxima persistencia, usar base de datos externa
- Los usuarios de prueba se recrean automáticamente si no existen
