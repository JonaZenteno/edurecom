from clustering.auto_assignment import AutoAssignment

def assign_group(profile):
    """
    Asigna un grupo de formación usando clustering automático con fallback manual
    """
    try:
        # Validar que el perfil tenga los datos necesarios
        if not profile:
            print("❌ Error: Perfil de usuario es None")
            return "Alfabetización Digital Básica"  # Grupo por defecto
        
        # Verificar campos críticos
        required_fields = ['digital_tools_skill', 'advanced_tic_skill', 'digital_citizenship_skill', 'teaching_tech_skill']
        missing_fields = [field for field in required_fields if getattr(profile, field) is None]
        
        if missing_fields:
            print(f"⚠️  Campos faltantes en el perfil: {missing_fields}")
            print("🔄 Usando asignación manual")
            return _manual_assign_group(profile)
        
        # Intentar usar el sistema de clustering automático
        auto_assignment = AutoAssignment()
        
        # Si el modelo está entrenado, usar asignación automática
        if auto_assignment.load_model():
            try:
                assigned_group = auto_assignment.assign_group(profile)
                confidence = auto_assignment.get_assignment_confidence(profile)
                
                # Si la confianza es alta, usar asignación automática
                if confidence > 0.7:
                    print(f"🤖 Asignación automática (confianza: {confidence:.2f})")
                    return assigned_group
                else:
                    print(f"⚠️  Baja confianza automática ({confidence:.2f}), usando manual")
            except Exception as e:
                print(f"❌ Error en asignación automática: {e}")
                print("🔄 Usando asignación manual como fallback")
        else:
            print("📂 No se pudo cargar el modelo de clustering")
    
    except Exception as e:
        print(f"❌ Error general en assign_group: {e}")
        print("🔄 Usando asignación manual como fallback")
    
    # Fallback a asignación manual
    print("🔄 Usando asignación manual")
    return _manual_assign_group(profile)

def _manual_assign_group(profile):
    """
    Asignación manual basada en el algoritmo original
    """
    try:
        if not profile:
            print("❌ Error: Perfil es None en asignación manual")
            return "Alfabetización Digital Básica"
        
        # Calcular promedio de habilidades digitales manejando valores None
        digital_skills = [
            profile.digital_tools_skill,
            profile.advanced_tic_skill,
            profile.digital_citizenship_skill,
            profile.teaching_tech_skill
        ]
        
        # Filtrar valores None y usar valor por defecto de 3 si todos son None
        valid_digital_skills = [skill for skill in digital_skills if skill is not None]
        if not valid_digital_skills:
            avg_digital_skills = 3  # Valor por defecto
            print("⚠️  No se encontraron habilidades digitales válidas, usando valor por defecto: 3")
        else:
            avg_digital_skills = sum(valid_digital_skills) / len(valid_digital_skills)
            print(f"📊 Habilidades digitales promedio: {avg_digital_skills:.2f}")
        
        # Calcular promedio de apoyo institucional manejando valores None
        institutional_support = [
            profile.leadership_support,
            profile.resource_support
        ]
        
        # Filtrar valores None y usar valor por defecto de 3 si todos son None
        valid_institutional_support = [support for support in institutional_support if support is not None]
        if not valid_institutional_support:
            avg_institutional_support = 3  # Valor por defecto
            print("⚠️  No se encontró apoyo institucional válido, usando valor por defecto: 3")
        else:
            avg_institutional_support = sum(valid_institutional_support) / len(valid_institutional_support)
            print(f"📊 Apoyo institucional promedio: {avg_institutional_support:.2f}")
        
        # Lógica de asignación de grupo
        if avg_digital_skills < 3:
            assigned_group = "Alfabetización Digital Básica"
        elif avg_institutional_support < 3 or (hasattr(profile, 'interest_leadership') and profile.interest_leadership):
            assigned_group = "Fortalecimiento Institucional"
        elif hasattr(profile, 'interest_educational_innovation') and profile.interest_educational_innovation:
            assigned_group = "Innovación Educativa"
        else:
            assigned_group = "Habilidades Digitales Avanzadas"
        
        print(f"🎯 Grupo asignado manualmente: {assigned_group}")
        return assigned_group
        
    except Exception as e:
        print(f"❌ Error en asignación manual: {e}")
        print("🔄 Usando grupo por defecto")
        return "Alfabetización Digital Básica"

def get_clustering_info():
    """
    Obtiene información sobre el sistema de clustering
    """
    auto_assignment = AutoAssignment()
    return auto_assignment.get_model_info()

def compare_assignments(profile):
    """
    Compara asignación automática vs manual
    """
    auto_assignment = AutoAssignment()
    return auto_assignment.compare_assignments(profile)
