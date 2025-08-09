from clustering.auto_assignment import AutoAssignment

def assign_group(profile):
    """
    Asigna un grupo de formación usando clustering automático con fallback manual
    """
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
    
    # Fallback a asignación manual
    print("🔄 Usando asignación manual")
    return _manual_assign_group(profile)

def _manual_assign_group(profile):
    """
    Asignación manual basada en el algoritmo original
    """
    # Calculate average digital skills with None handling
    digital_skills = [
        profile.digital_tools_skill,
        profile.advanced_tic_skill,
        profile.digital_citizenship_skill,
        profile.teaching_tech_skill
    ]
    # Filter out None values and use default of 3 if all are None
    valid_digital_skills = [skill for skill in digital_skills if skill is not None]
    if not valid_digital_skills:
        avg_digital_skills = 3  # Default value
    else:
        avg_digital_skills = sum(valid_digital_skills) / len(valid_digital_skills)
    
    # Calculate average institutional support with None handling
    institutional_support = [
        profile.leadership_support,
        profile.resource_support
    ]
    # Filter out None values and use default of 3 if all are None
    valid_institutional_support = [support for support in institutional_support if support is not None]
    if not valid_institutional_support:
        avg_institutional_support = 3  # Default value
    else:
        avg_institutional_support = sum(valid_institutional_support) / len(valid_institutional_support)
    
    # Group assignment logic
    if avg_digital_skills < 3:
        return "Alfabetización Digital Básica"
    elif avg_institutional_support < 3 or profile.interest_leadership:
        return "Fortalecimiento Institucional"
    elif profile.interest_educational_innovation:
        return "Innovación Educativa"
    else:
        return "Habilidades Digitales Avanzadas"

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
