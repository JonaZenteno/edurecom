#!/usr/bin/env python3
"""
Script de prueba para el sistema de clustering
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from clustering.auto_assignment import AutoAssignment
from models import UserProfile

def test_clustering_system():
    """
    Prueba el sistema de clustering con diferentes perfiles
    """
    print("🧪 PRUEBAS DEL SISTEMA DE CLUSTERING")
    print("=" * 50)
    
    # Cargar el modelo entrenado
    auto_assignment = AutoAssignment()
    
    if not auto_assignment.load_model():
        print("❌ No se pudo cargar el modelo entrenado")
        return
    
    print("✅ Modelo cargado exitosamente")
    
    # Crear perfiles de prueba
    test_profiles = create_test_profiles()
    
    print(f"\n📊 Probando {len(test_profiles)} perfiles de prueba:")
    print("-" * 50)
    
    results = []
    
    for i, profile in enumerate(test_profiles, 1):
        print(f"\n👤 Perfil de prueba {i}:")
        print(f"   Habilidades digitales: {profile.digital_tools_skill}/{profile.advanced_tic_skill}/{profile.digital_citizenship_skill}/{profile.teaching_tech_skill}")
        print(f"   Apoyo institucional: {profile.leadership_support}/{profile.resource_support}")
        print(f"   Rol: {profile.role}, Escuela: {profile.school_type}")
        print(f"   Intereses: Digital={profile.interest_digital_literacy}, Innovación={profile.interest_educational_innovation}, Liderazgo={profile.interest_leadership}")
        
        # Probar asignación
        try:
            assigned_group = auto_assignment.assign_group(profile)
            confidence = auto_assignment.get_assignment_confidence(profile)
            
            print(f"   🎯 Grupo asignado: {assigned_group}")
            print(f"   📈 Confianza: {confidence:.2f}")
            
            results.append({
                'profile': i,
                'group': assigned_group,
                'confidence': confidence
            })
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            results.append({
                'profile': i,
                'group': 'Error',
                'confidence': 0.0
            })
    
    # Mostrar resumen
    print(f"\n📋 RESUMEN DE PRUEBAS")
    print("-" * 50)
    
    groups = {}
    total_confidence = 0
    valid_results = 0
    
    for result in results:
        group = result['group']
        confidence = result['confidence']
        
        if group not in groups:
            groups[group] = 0
        groups[group] += 1
        
        if confidence > 0:
            total_confidence += confidence
            valid_results += 1
    
    print(f"   Distribución de grupos:")
    for group, count in groups.items():
        print(f"     {group}: {count} perfiles")
    
    if valid_results > 0:
        avg_confidence = total_confidence / valid_results
        print(f"   Confianza promedio: {avg_confidence:.2f}")
    
    print(f"\n✅ Pruebas completadas")

def create_test_profiles():
    """
    Crea perfiles de prueba variados
    """
    test_profiles = []
    
    # Perfil 1: Alfabetización Digital Básica (bajas habilidades)
    profile1 = UserProfile()
    profile1.digital_tools_skill = 1
    profile1.advanced_tic_skill = 1
    profile1.digital_citizenship_skill = 2
    profile1.teaching_tech_skill = 1
    profile1.leadership_support = 2
    profile1.resource_support = 2
    profile1.role = 'profesor'
    profile1.school_type = 'rural'
    profile1.dependency = 'municipal'
    profile1.age_range = '51+'
    profile1.learning_format = 'autoaprendizaje'
    profile1.interest_digital_literacy = True
    profile1.interest_educational_innovation = False
    profile1.interest_leadership = False
    test_profiles.append(profile1)
    
    # Perfil 2: Fortalecimiento Institucional (bajo apoyo institucional)
    profile2 = UserProfile()
    profile2.digital_tools_skill = 3
    profile2.advanced_tic_skill = 3
    profile2.digital_citizenship_skill = 3
    profile2.teaching_tech_skill = 3
    profile2.leadership_support = 1
    profile2.resource_support = 2
    profile2.role = 'director'
    profile2.school_type = 'urbana'
    profile2.dependency = 'municipal'
    profile2.age_range = '41-50'
    profile2.learning_format = 'talleres'
    profile2.interest_digital_literacy = False
    profile2.interest_educational_innovation = False
    profile2.interest_leadership = True
    test_profiles.append(profile2)
    
    # Perfil 3: Innovación Educativa (alto interés en innovación)
    profile3 = UserProfile()
    profile3.digital_tools_skill = 4
    profile3.advanced_tic_skill = 4
    profile3.digital_citizenship_skill = 4
    profile3.teaching_tech_skill = 4
    profile3.leadership_support = 4
    profile3.resource_support = 4
    profile3.role = 'profesor'
    profile3.school_type = 'cientifico-humanistica'
    profile3.dependency = 'privada-subvencionada'
    profile3.age_range = '31-40'
    profile3.learning_format = 'en-linea'
    profile3.interest_digital_literacy = False
    profile3.interest_educational_innovation = True
    profile3.interest_leadership = False
    test_profiles.append(profile3)
    
    # Perfil 4: Habilidades Digitales Avanzadas (altas habilidades)
    profile4 = UserProfile()
    profile4.digital_tools_skill = 5
    profile4.advanced_tic_skill = 5
    profile4.digital_citizenship_skill = 5
    profile4.teaching_tech_skill = 5
    profile4.leadership_support = 4
    profile4.resource_support = 4
    profile4.role = 'profesor'
    profile4.school_type = 'tecnico-profesional'
    profile4.dependency = 'privada-pagada'
    profile4.age_range = '20-30'
    profile4.learning_format = 'en-linea'
    profile4.interest_digital_literacy = False
    profile4.interest_educational_innovation = False
    profile4.interest_leadership = False
    test_profiles.append(profile4)
    
    # Perfil 5: Caso límite (habilidades medias)
    profile5 = UserProfile()
    profile5.digital_tools_skill = 3
    profile5.advanced_tic_skill = 3
    profile5.digital_citizenship_skill = 3
    profile5.teaching_tech_skill = 3
    profile5.leadership_support = 3
    profile5.resource_support = 3
    profile5.role = 'profesor'
    profile5.school_type = 'urbana'
    profile5.dependency = 'privada-subvencionada'
    profile5.age_range = '31-40'
    profile5.learning_format = 'talleres'
    profile5.interest_digital_literacy = False
    profile5.interest_educational_innovation = False
    profile5.interest_leadership = False
    test_profiles.append(profile5)
    
    return test_profiles

if __name__ == "__main__":
    test_clustering_system() 