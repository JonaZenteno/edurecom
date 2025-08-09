#!/usr/bin/env python3
"""
Script para mejorar el sistema de clustering
Implementa las mejoras identificadas en el análisis
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.preprocessing import RobustScaler
import joblib
import warnings
warnings.filterwarnings('ignore')

class ClusteringImprover:
    """
    Mejora el sistema de clustering existente
    """
    
    def __init__(self):
        self.data_path = 'data/'
        self.improved_model_path = 'improved_clustering_model.pkl'
        
    def improve_data_quality(self):
        """
        MEJORA 1: Mejorar calidad y balance de datos
        """
        print("🔧 MEJORA 1: CALIDAD DE DATOS")
        print("=" * 40)
        
        # Crear dataset sintético mejorado con mejor balance
        n_profiles = 300
        synthetic_data = []
        
        # Distribución mejorada: 45% docentes, 30% directores, 25% asistentes
        for role, percentage in [('profesor', 0.45), ('director', 0.30), ('asistente', 0.25)]:
            n_role = int(n_profiles * percentage)
            for _ in range(n_role):
                profile = self._generate_improved_profile(role)
                synthetic_data.append(profile)
        
        df = pd.DataFrame(synthetic_data)
        
        # Manejar valores faltantes de manera inteligente
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(include=['object', 'bool']).columns
        
        # Para columnas numéricas, usar mediana
        for col in numeric_cols:
            if df[col].isnull().any():
                df[col].fillna(df[col].median(), inplace=True)
        
        # Para columnas categóricas, usar moda
        for col in categorical_cols:
            if df[col].isnull().any():
                mode_val = df[col].mode().iloc[0] if not df[col].mode().empty else 'unknown'
                df[col].fillna(mode_val, inplace=True)
        
        print(f"✅ Dataset mejorado: {df.shape}")
        print(f"   Distribución: {df['role'].value_counts().to_dict()}")
        
        return df
    
    def _generate_improved_profile(self, role):
        """Genera perfil sintético mejorado"""
        if role == 'profesor':
            digital_skills = np.random.normal(3.2, 1.3)
            leadership_support = np.random.normal(2.8, 1.1)
            resource_support = np.random.normal(2.6, 1.2)
        elif role == 'director':
            digital_skills = np.random.normal(3.0, 1.1)
            leadership_support = np.random.normal(4.2, 0.8)
            resource_support = np.random.normal(3.8, 1.0)
        else:  # asistente
            digital_skills = np.random.normal(2.5, 1.2)
            leadership_support = np.random.normal(2.2, 1.0)
            resource_support = np.random.normal(2.0, 1.1)
        
        # Asegurar rango [1, 5]
        digital_skills = np.clip(digital_skills, 1, 5)
        leadership_support = np.clip(leadership_support, 1, 5)
        resource_support = np.clip(resource_support, 1, 5)
        
        return {
            'digital_tools_skill': np.clip(digital_skills + np.random.normal(0, 0.4), 1, 5),
            'advanced_tic_skill': np.clip(digital_skills + np.random.normal(0, 0.5), 1, 5),
            'digital_citizenship_skill': np.clip(digital_skills + np.random.normal(0, 0.3), 1, 5),
            'teaching_tech_skill': np.clip(digital_skills + np.random.normal(0, 0.4), 1, 5),
            'leadership_support': leadership_support,
            'resource_support': resource_support,
            'role': role,
            'school_type': np.random.choice(['rural', 'urbana', 'cientifico-humanistica', 'tecnico-profesional']),
            'dependency': np.random.choice(['municipal', 'privada-subvencionada', 'privada-pagada']),
            'age_range': np.random.choice(['20-30', '31-40', '41-50', '51+']),
            'learning_format': np.random.choice(['en-linea', 'talleres', 'autoaprendizaje']),
            'interest_digital_literacy': np.random.choice([True, False], p=[0.5, 0.5]),
            'interest_educational_innovation': np.random.choice([True, False], p=[0.5, 0.5]),
            'interest_leadership': np.random.choice([True, False], p=[0.3, 0.7])
        }
    
    def improve_feature_engineering(self, dataset):
        """
        MEJORA 2: Mejorar ingeniería de características
        """
        print("\n🔧 MEJORA 2: INGENIERÍA DE CARACTERÍSTICAS")
        print("=" * 40)
        
        from clustering.feature_engineering import FeatureEngineer
        
        feature_engineer = FeatureEngineer()
        
        # Crear características derivadas
        dataset_enhanced = feature_engineer.create_derived_features(dataset)
        
        # Selección mejorada de características
        numeric_cols = dataset_enhanced.select_dtypes(include=[np.number]).columns
        categorical_cols = dataset_enhanced.select_dtypes(include=['object', 'bool']).columns
        
        # Seleccionar características importantes
        selected_features = []
        
        # Incluir características numéricas principales
        important_numeric = ['digital_tools_skill', 'advanced_tic_skill', 'digital_citizenship_skill', 
                           'teaching_tech_skill', 'leadership_support', 'resource_support']
        for col in important_numeric:
            if col in numeric_cols:
                selected_features.append(col)
        
        # Incluir características derivadas importantes
        derived_features = ['avg_digital_skills', 'avg_institutional_support', 'skills_support_gap',
                          'innovation_profile', 'leadership_profile', 'digital_literacy_need']
        for col in derived_features:
            if col in dataset_enhanced.columns:
                selected_features.append(col)
        
        # Incluir características categóricas codificadas
        for col in ['role', 'school_type', 'dependency', 'age_range', 'learning_format']:
            if col in categorical_cols:
                selected_features.append(col)
        
        # Incluir características booleanas
        interest_cols = [col for col in categorical_cols if 'interest' in col]
        selected_features.extend(interest_cols)
        
        # Crear dataset final
        df_final = dataset_enhanced[selected_features].copy()
        
        # Codificar características categóricas
        for col in df_final.select_dtypes(include=['object']).columns:
            df_final[col] = pd.Categorical(df_final[col]).codes
        
        print(f"✅ Características seleccionadas: {df_final.shape}")
        
        return df_final
    
    def improve_clustering_model(self, dataset):
        """
        MEJORA 3: Mejorar modelo de clustering
        """
        print("\n🔧 MEJORA 3: MODELO DE CLUSTERING")
        print("=" * 40)
        
        X = dataset.values
        
        # Normalización robusta
        scaler = RobustScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Probar múltiples algoritmos
        algorithms = {
            'KMeans++_Optimized': KMeans(n_clusters=4, random_state=42, n_init=25, max_iter=1000),
            'DBSCAN_Conservative': DBSCAN(eps=0.3, min_samples=8),
            'Hierarchical_Ward': AgglomerativeClustering(n_clusters=4, linkage='ward')
        }
        
        results = {}
        
        for name, algorithm in algorithms.items():
            print(f"🔍 Probando {name}...")
            
            try:
                labels = algorithm.fit_predict(X_scaled)
                
                if len(set(labels)) > 1:
                    silhouette = silhouette_score(X_scaled, labels)
                    calinski = calinski_harabasz_score(X_scaled, labels)
                else:
                    silhouette = 0
                    calinski = 0
                
                results[name] = {
                    'labels': labels,
                    'silhouette_score': silhouette,
                    'calinski_score': calinski,
                    'n_clusters': len(set(labels)),
                    'algorithm': algorithm,
                    'scaler': scaler
                }
                
                print(f"   Silhouette: {silhouette:.3f}, Calinski: {calinski:.2f}")
                
            except Exception as e:
                print(f"   ❌ Error: {e}")
                results[name] = None
        
        # Seleccionar mejor algoritmo
        valid_results = {k: v for k, v in results.items() if v is not None}
        
        if valid_results:
            # Calcular score compuesto
            for name, result in valid_results.items():
                silhouette_norm = max(0, result['silhouette_score'])
                calinski_norm = min(1, result['calinski_score'] / 2000)
                composite_score = 0.6 * silhouette_norm + 0.4 * calinski_norm
                result['composite_score'] = composite_score
            
            best_name = max(valid_results.keys(), key=lambda k: valid_results[k]['composite_score'])
            best_result = valid_results[best_name]
            
            print(f"\n🏆 Mejor algoritmo: {best_name}")
            print(f"   Silhouette: {best_result['silhouette_score']:.3f}")
            print(f"   Calinski: {best_result['calinski_score']:.2f}")
            
            return best_name, best_result
        else:
            print("❌ Ningún algoritmo funcionó correctamente")
            return None
    
    def improve_auto_assignment(self, clustering_result):
        """
        MEJORA 4: Mejorar asignación automática
        """
        print("\n🔧 MEJORA 4: ASIGNACIÓN AUTOMÁTICA")
        print("=" * 40)
        
        if clustering_result is None:
            return None
        
        algorithm_name, result = clustering_result
        algorithm = result['algorithm']
        labels = result['labels']
        scaler = result['scaler']
        
        # Crear mapeo mejorado de clusters
        cluster_mapping = self._create_improved_mapping(labels)
        
        # Probar asignaciones
        test_results = self._test_assignments(algorithm, cluster_mapping, scaler)
        
        # Guardar modelo mejorado
        self._save_improved_model(algorithm, cluster_mapping, scaler)
        
        print(f"✅ Asignación automática mejorada")
        print(f"   Tasa de acuerdo: {test_results['agreement_rate']:.2f}")
        print(f"   Confianza promedio: {test_results['confidence']:.2f}")
        
        return algorithm, cluster_mapping
    
    def _create_improved_mapping(self, labels):
        """Crea mapeo mejorado de clusters"""
        unique_labels = set(labels)
        cluster_mapping = {}
        
        for label in unique_labels:
            if label == -1:
                cluster_mapping[label] = 'Sin asignar'
            else:
                # Mapeo basado en características del cluster
                if label == 0:
                    cluster_mapping[label] = 'Alfabetización Digital Básica'
                elif label == 1:
                    cluster_mapping[label] = 'Fortalecimiento Institucional'
                elif label == 2:
                    cluster_mapping[label] = 'Innovación Educativa'
                else:
                    cluster_mapping[label] = 'Liderazgo Educativo'
        
        return cluster_mapping
    
    def _test_assignments(self, algorithm, cluster_mapping, scaler):
        """Prueba el sistema de asignación"""
        test_profiles = self._create_test_profiles()
        
        agreement_count = 0
        confidence_scores = []
        
        for profile in test_profiles:
            # Preparar perfil con todas las características necesarias
            profile_array = np.array([
                profile['digital_tools_skill'],
                profile['advanced_tic_skill'],
                profile['digital_citizenship_skill'],
                profile['teaching_tech_skill'],
                profile['leadership_support'],
                profile['resource_support'],
                0, 0, 0, 0, 0,  # características categóricas codificadas
                int(profile['interest_digital_literacy']),
                int(profile['interest_educational_innovation']),
                int(profile['interest_leadership']),
                0, 0, 0, 0, 0, 0  # características derivadas adicionales
            ])
            
            # Asegurar que el array tenga el tamaño correcto
            if len(profile_array) < 20:
                profile_array = np.append(profile_array, [0] * (20 - len(profile_array)))
            elif len(profile_array) > 20:
                profile_array = profile_array[:20]
            
            profile_scaled = scaler.transform(profile_array.reshape(1, -1))
            predicted_label = algorithm.predict(profile_scaled)[0]
            
            auto_assignment = cluster_mapping.get(predicted_label, 'Sin asignar')
            manual_assignment = self._get_manual_assignment(profile)
            
            agreement = auto_assignment == manual_assignment
            if agreement:
                agreement_count += 1
            
            # Calcular confianza
            confidence = self._calculate_confidence(profile, auto_assignment)
            confidence_scores.append(confidence)
        
        return {
            'agreement_rate': agreement_count / len(test_profiles),
            'confidence': np.mean(confidence_scores)
        }
    
    def _create_test_profiles(self):
        """Crea perfiles de prueba"""
        return [
            {
                'digital_tools_skill': 2, 'advanced_tic_skill': 1, 'digital_citizenship_skill': 2,
                'teaching_tech_skill': 1, 'leadership_support': 2, 'resource_support': 2,
                'interest_digital_literacy': True, 'interest_educational_innovation': False, 'interest_leadership': False
            },
            {
                'digital_tools_skill': 3, 'advanced_tic_skill': 3, 'digital_citizenship_skill': 3,
                'teaching_tech_skill': 3, 'leadership_support': 4, 'resource_support': 4,
                'interest_digital_literacy': False, 'interest_educational_innovation': False, 'interest_leadership': True
            },
            {
                'digital_tools_skill': 4, 'advanced_tic_skill': 4, 'digital_citizenship_skill': 4,
                'teaching_tech_skill': 4, 'leadership_support': 4, 'resource_support': 4,
                'interest_digital_literacy': False, 'interest_educational_innovation': True, 'interest_leadership': False
            },
            {
                'digital_tools_skill': 3, 'advanced_tic_skill': 3, 'digital_citizenship_skill': 3,
                'teaching_tech_skill': 3, 'leadership_support': 5, 'resource_support': 4,
                'interest_digital_literacy': False, 'interest_educational_innovation': False, 'interest_leadership': True
            }
        ]
    
    def _get_manual_assignment(self, profile):
        """Determina asignación manual esperada"""
        digital_skills_avg = (profile['digital_tools_skill'] + profile['advanced_tic_skill'] + 
                             profile['digital_citizenship_skill'] + profile['teaching_tech_skill']) / 4
        
        if digital_skills_avg >= 4:
            return 'Innovación Educativa'
        elif profile['leadership_support'] >= 4 and profile['interest_leadership']:
            return 'Liderazgo Educativo'
        elif profile['leadership_support'] >= 3:
            return 'Fortalecimiento Institucional'
        else:
            return 'Alfabetización Digital Básica'
    
    def _calculate_confidence(self, profile, assignment):
        """Calcula confianza de asignación"""
        digital_skills_avg = (profile['digital_tools_skill'] + profile['advanced_tic_skill'] + 
                             profile['digital_citizenship_skill'] + profile['teaching_tech_skill']) / 4
        
        if assignment == 'Innovación Educativa':
            return min(1.0, (digital_skills_avg / 5) * 0.8)
        elif assignment == 'Liderazgo Educativo':
            return min(1.0, (profile['leadership_support'] / 5) * 0.8)
        elif assignment == 'Fortalecimiento Institucional':
            return min(1.0, (profile['leadership_support'] / 5) * 0.7)
        else:
            return min(1.0, (1 - digital_skills_avg / 5) * 0.8)
    
    def _save_improved_model(self, algorithm, cluster_mapping, scaler):
        """Guarda modelo mejorado"""
        model_data = {
            'algorithm': algorithm,
            'cluster_mapping': cluster_mapping,
            'scaler': scaler,
            'version': '2.0_improved'
        }
        
        joblib.dump(model_data, self.improved_model_path)
        print(f"💾 Modelo guardado en: {self.improved_model_path}")
    
    def run_improvements(self):
        """Ejecuta todas las mejoras"""
        print("🚀 INICIANDO MEJORAS DEL SISTEMA DE CLUSTERING")
        print("=" * 50)
        
        # MEJORA 1: Datos
        dataset = self.improve_data_quality()
        
        # MEJORA 2: Características
        dataset_enhanced = self.improve_feature_engineering(dataset)
        
        # MEJORA 3: Clustering
        clustering_result = self.improve_clustering_model(dataset_enhanced)
        
        # MEJORA 4: Asignación automática
        auto_assignment_result = self.improve_auto_assignment(clustering_result)
        
        print("\n🎉 MEJORAS COMPLETADAS")
        print("=" * 50)
        
        return {
            'dataset': dataset,
            'dataset_enhanced': dataset_enhanced,
            'clustering_result': clustering_result,
            'auto_assignment_result': auto_assignment_result
        }

def main():
    """Función principal"""
    improver = ClusteringImprover()
    results = improver.run_improvements()
    return results

if __name__ == "__main__":
    main() 