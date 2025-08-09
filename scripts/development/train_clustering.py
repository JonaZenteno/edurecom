#!/usr/bin/env python3
"""
Script principal para entrenar el sistema de clustering
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from clustering.data_preprocessing import DataPreprocessor
from clustering.feature_engineering import FeatureEngineer
from clustering.clustering_engine import ClusteringEngine
from clustering.auto_assignment import AutoAssignment
import pandas as pd
import numpy as np

def main():
    """
    Pipeline completo de entrenamiento del sistema de clustering
    """
    print("🚀 INICIANDO ENTRENAMIENTO DEL SISTEMA DE CLUSTERING")
    print("=" * 60)
    
    # FASE 1: PREPARACIÓN DE DATOS
    print("\n📊 FASE 1: PREPARACIÓN DE DATOS")
    print("-" * 40)
    
    preprocessor = DataPreprocessor(data_path='data/')
    
    # Cargar y analizar datos CSV
    data_dict = preprocessor.load_and_analyze_data()
    
    if not data_dict:
        print("❌ No se pudieron cargar los archivos CSV")
        return
    
    # Extraer características de los datos
    features_dict = preprocessor.extract_features_from_data(data_dict)
    print(f"✅ Características extraídas de {len(features_dict)} fuentes de datos")
    
    # Crear dataset sintético para clustering
    print("\n🔄 Generando dataset sintético...")
    dataset = preprocessor.create_clustering_dataset(features_dict)
    print(f"✅ Dataset creado: {dataset.shape}")
    
    # Preprocesar datos
    dataset_processed = preprocessor.preprocess_for_clustering(dataset)
    print(f"✅ Datos preprocesados: {dataset_processed.shape}")
    
    # Limpiar datos (eliminar NaN)
    dataset_cleaned = preprocessor.clean_dataset(dataset_processed)
    print(f"✅ Datos limpios: {dataset_cleaned.shape}")
    
    # FASE 2: INGENIERÍA DE CARACTERÍSTICAS
    print("\n🔧 FASE 2: INGENIERÍA DE CARACTERÍSTICAS")
    print("-" * 40)
    
    feature_engineer = FeatureEngineer()
    
    # Crear características derivadas
    dataset_enhanced = feature_engineer.create_derived_features(dataset_cleaned)
    print(f"✅ Características derivadas creadas: {dataset_enhanced.shape}")
    
    # Seleccionar mejores características
    dataset_final = feature_engineer.select_best_features(dataset_enhanced)
    print(f"✅ Características seleccionadas: {dataset_final.shape}")
    
    # Limpiar dataset final
    dataset_final_clean = preprocessor.clean_dataset(dataset_final)
    print(f"✅ Dataset final limpio: {dataset_final_clean.shape}")
    
    # FASE 3: ENTRENAMIENTO DEL CLUSTERING
    print("\n🎯 FASE 3: ENTRENAMIENTO DEL CLUSTERING")
    print("-" * 40)
    
    clustering_engine = ClusteringEngine(n_clusters=4, random_state=42)
    
    # Convertir DataFrame a array para sklearn
    X = dataset_final_clean.values
    feature_names = dataset_final_clean.columns.tolist()
    
    # Verificar que no hay valores NaN
    if np.isnan(X).any():
        print("❌ Error: Aún hay valores NaN en los datos")
        return
    
    print(f"✅ Datos listos para clustering: {X.shape}")
    
    # Entrenar modelo
    clustering_engine.train_clustering_model(X, n_clusters=4)
    
    # Analizar clusters
    cluster_analysis = clustering_engine.analyze_clusters(X, feature_names)
    
    # Mapear clusters a grupos de formación
    cluster_mapping = clustering_engine.map_clusters_to_groups(cluster_analysis)
    
    # FASE 4: SISTEMA DE ASIGNACIÓN AUTOMÁTICA
    print("\n🤖 FASE 4: SISTEMA DE ASIGNACIÓN AUTOMÁTICA")
    print("-" * 40)
    
    auto_assignment = AutoAssignment()
    auto_assignment.train_model(clustering_engine, feature_engineer, cluster_mapping)
    
    # FASE 5: EVALUACIÓN Y PRUEBAS
    print("\n📈 FASE 5: EVALUACIÓN Y PRUEBAS")
    print("-" * 40)
    
    # Crear perfiles de prueba
    test_profiles = create_test_profiles()
    
    print("\n🧪 Probando asignaciones automáticas:")
    for i, profile in enumerate(test_profiles):
        print(f"\n   Perfil de prueba {i+1}:")
        comparison = auto_assignment.compare_assignments(profile)
        
        if comparison['agreement']:
            print(f"   ✅ Acuerdo entre asignación automática y manual")
        else:
            print(f"   ⚠️  Diferencia: Auto={comparison['auto_assignment']}, Manual={comparison['manual_assignment']}")
    
    # Mostrar métricas finales
    print("\n📊 MÉTRICAS FINALES")
    print("-" * 40)
    
    metrics = clustering_engine.get_model_metrics()
    print(f"   Silhouette Score: {metrics['silhouette_score']:.3f}")
    print(f"   Calinski-Harabasz Score: {metrics['calinski_score']:.2f}")
    print(f"   Número de clusters: {metrics['n_clusters']}")
    
    model_info = auto_assignment.get_model_info()
    print(f"   Estado del modelo: {model_info['status']}")
    print(f"   Ruta del modelo: {model_info['model_path']}")
    
    print("\n🎉 ¡ENTRENAMIENTO COMPLETADO EXITOSAMENTE!")
    print("=" * 60)
    
    return auto_assignment

def create_test_profiles():
    """
    Crea perfiles de prueba para evaluar el sistema
    """
    from models import UserProfile
    
    test_profiles = []
    
    # Perfil 1: Alfabetización Digital Básica
    profile1 = UserProfile()
    profile1.digital_tools_skill = 2
    profile1.advanced_tic_skill = 1
    profile1.digital_citizenship_skill = 2
    profile1.teaching_tech_skill = 1
    profile1.leadership_support = 2
    profile1.resource_support = 2
    profile1.role = 'profesor'
    profile1.school_type = 'rural'
    profile1.dependency = 'municipal'
    profile1.age_range = '41-50'
    profile1.learning_format = 'autoaprendizaje'
    profile1.interest_digital_literacy = True
    profile1.interest_educational_innovation = False
    profile1.interest_leadership = False
    test_profiles.append(profile1)
    
    # Perfil 2: Fortalecimiento Institucional
    profile2 = UserProfile()
    profile2.digital_tools_skill = 3
    profile2.advanced_tic_skill = 3
    profile2.digital_citizenship_skill = 3
    profile2.teaching_tech_skill = 3
    profile2.leadership_support = 2
    profile2.resource_support = 2
    profile2.role = 'director'
    profile2.school_type = 'urbana'
    profile2.dependency = 'municipal'
    profile2.age_range = '51+'
    profile2.learning_format = 'talleres'
    profile2.interest_digital_literacy = False
    profile2.interest_educational_innovation = False
    profile2.interest_leadership = True
    test_profiles.append(profile2)
    
    # Perfil 3: Innovación Educativa
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
    
    # Perfil 4: Habilidades Digitales Avanzadas
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
    
    return test_profiles

if __name__ == "__main__":
    main() 