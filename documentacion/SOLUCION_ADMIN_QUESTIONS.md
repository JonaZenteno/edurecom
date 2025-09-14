# Solución - Preguntas del Administrador

## 🔍 Problema Identificado

**Síntoma**: El administrador solo ve 3 preguntas cuando accede a `/admin/questions` para editarlas, mientras que los usuarios normales ven las 14 preguntas completas en el formulario de perfil.

## 🔎 Análisis del Problema

### **Causa Raíz:**
La función `admin_questions()` en `routes.py` estaba usando las mismas preguntas por defecto limitadas (3 preguntas) que se usaban como fallback en el formulario de perfil, en lugar de usar las preguntas completas.

### **Problema Específico:**
```python
# Código anterior (problemático)
questions = [
    {"name": "role", "type": "select", "label": "¿Cuál es tu rol...", "choices": ["profesor", "director", "asistente"]},
    {"name": "age_range", "type": "select", "label": "¿En qué rango de edad...", "choices": ["20-30", "31-40", "41-50", "51+"]},
    {"name": "digital_tools_skill", "type": "select", "label": "Herramientas TI básicas", "choices": ["1", "2", "3", "4", "5"]}
]
```

## ✅ Soluciones Implementadas

### **1. Función `admin_questions()` Mejorada** (`routes.py`)
- ✅ **Preguntas completas por defecto**: Ahora usa las 14 preguntas completas como fallback
- ✅ **Logs detallados**: Para diagnosticar problemas de carga
- ✅ **Manejo robusto de errores**: Mejor gestión de excepciones
- ✅ **Logs de acciones**: Rastrea agregar, editar y eliminar preguntas

### **2. Script de Configuración** (`setup_questions.py`)
- ✅ **Crea archivo `questions_admin.json`** si no existe
- ✅ **Preguntas completas predefinidas**: 14 preguntas con todos los campos
- ✅ **Verificación de integridad**: Confirma que el archivo se guardó correctamente

### **3. Configuración de Railway** (`railway.json`)
- ✅ **Ejecuta configuración de preguntas** en cada despliegue
- ✅ **Asegura que el archivo esté disponible** en Railway

## 📋 Preguntas Completas Ahora Disponibles

El administrador ahora puede ver y editar las **14 preguntas completas**:

1. **Rol** - ¿Cuál es tu rol en el establecimiento educativo?
2. **Tipo de establecimiento** - ¿En qué tipo de establecimiento trabajas?
3. **Dependencia** - ¿Cuál es la dependencia de tu establecimiento?
4. **Rango de edad** - ¿En qué rango de edad te encuentras?
5. **Herramientas TI básicas** - Evalúa tu habilidad (1-5)
6. **TIC avanzadas** - Evalúa tu habilidad (1-5)
7. **Ciudadanía digital** - Evalúa tu conocimiento (1-5)
8. **Tecnología en enseñanza** - Evalúa tu habilidad (1-5)
9. **Apoyo del liderazgo** - Evalúa el apoyo (1-5)
10. **Recursos tecnológicos** - Evalúa los recursos (1-5)
11. **Interés en alfabetización digital** - ¿Te interesa?
12. **Interés en innovación educativa** - ¿Te interesa?
13. **Interés en liderazgo** - ¿Te interesa?
14. **Formato de aprendizaje** - ¿Qué formato prefieres?

## 🔧 Logs de Diagnóstico

Los logs ahora mostrarán:
- ✅ `🔍 Cargando preguntas para administrador desde: questions_admin.json`
- ✅ `✅ Preguntas cargadas desde archivo: 14 preguntas`
- ✅ `🔧 Acción del administrador: add/edit/delete`
- ✅ `💾 Preguntas guardadas: 14 preguntas`

## 🚀 Flujo de Solución

### **Paso 1: Configuración Inicial**
```bash
python setup_questions.py
```
- Crea archivo `questions_admin.json` con preguntas completas
- Verifica que se guardó correctamente

### **Paso 2: Acceso del Administrador**
- El administrador accede a `/admin/questions`
- Ve las 14 preguntas completas
- Puede agregar, editar o eliminar preguntas

### **Paso 3: Aplicación de Cambios**
- Los cambios se guardan en `questions_admin.json`
- Se aplican inmediatamente al formulario de perfil
- Los usuarios ven las preguntas actualizadas

## 🎯 Próximos Pasos

1. **Hacer commit y push** de los cambios
2. **Desplegar en Railway**
3. **Verificar logs** para confirmar configuración de preguntas
4. **Probar como administrador**:
   - Iniciar sesión con `admin` / `admin123`
   - Ir a `/admin/questions`
   - Verificar que aparecen las 14 preguntas
   - Probar agregar/editar/eliminar preguntas

## 🔍 Verificación

Para verificar que funciona:
1. **Iniciar sesión como administrador**
2. **Ir a `/admin/questions`**
3. **Verificar que aparecen 14 preguntas** (no 3)
4. **Probar editar una pregunta**
5. **Verificar que los cambios se aplican** al formulario de perfil

## 🚨 Si Aún Hay Problemas

Si el administrador sigue viendo solo 3 preguntas:
1. **Revisar logs** para ver si se carga el archivo correctamente
2. **Verificar que `questions_admin.json` existe** en Railway
3. **Usar el script `setup_questions.py`** para recrear el archivo
4. **Verificar permisos de escritura** en Railway

Los logs te dirán exactamente qué está pasando en cada paso.

## 📝 Notas Importantes

- **Consistencia**: Ahora tanto usuarios como administradores ven las mismas preguntas
- **Flexibilidad**: El administrador puede modificar las preguntas dinámicamente
- **Persistencia**: Los cambios se guardan en el archivo JSON
- **Logs detallados**: Para facilitar el diagnóstico de problemas
