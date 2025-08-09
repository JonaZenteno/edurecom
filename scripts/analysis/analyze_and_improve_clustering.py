#!/usr/bin/env python3
"""
Script de análisis y mejora del sistema de clustering
Aborda los problemas identificados y propone soluciones
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

class ClusteringAnalyzer:
    """
    Analizador y mejorador del sistema de clustering
    """
    
    def __init__(self):
        self.data_path = 'data/'
        self.results = {}
        
    def analyze_data_quality(self):
        """
        FASE 1: Análisis de calidad de datos
        """
        print("🔍 FASE 1: ANÁLISIS DE CALIDAD DE DATOS")
        print("=" * 50)
        
        # Cargar datos
        data_files = {
            'asistentes': 'Asistentes.csv',
            'directores': 'Directores.csv', 
            'docentes': 'RespuestasDocentes.csv',
            'docentes_directores': 'RespuesDocentesYDirectores.csv'
        }
        
        data_analysis = {}
        total_records = 0
        
        for name, filename in data_files.items():
            filepath = os.path.join(self.data_path, filename)
            if os.path.exists(filepath):
                df = pd.read_csv(filepath, sep=';', encoding='utf-8')
                data_analysis[name] = {
                    'shape': df.shape,
                    'missing_values': df.isnull().sum().sum(),
                    'duplicates': df.duplicated().sum(),
                    'data_types': df.dtypes.value_counts().to_dict()
                }
                total_records += df.shape[0]
                print(f"📊 {name.capitalize()}: {df.shape[0]} registros, {df.shape[1]} columnas")
                print(f"   Valores faltantes: {data_analysis[name]['missing_values']}")
                print(f"   Duplicados: {data_analysis[name]['duplicates']}")
        
        print(f"\n📈 RESUMEN DE DATOS:")
        print(f"   Total de registros: {total_records}")
        print(f"   Fuentes de datos: {len(data_analysis)}")
        
        # Identificar problemas de balance
        if 'docentes' in data_analysis:
            docentes_count = data_analysis['docentes']['shape'][0]
            asistentes_count = data_analysis.get('asistentes', {}).get('shape', [0])[0]
            directores_count = data_analysis.get('directores', {}).get('shape', [0])[0]
            
            print(f"\n⚖️  ANÁLISIS DE BALANCE:")
            print(f"   Docentes: {docentes_count}")
            print(f"   Asistentes: {asistentes_count}")
            print(f"   Directores: {directores_count}")
            
            if docentes_count < min(asistentes_count, directores_count) * 0.5:
                print("   ⚠️  ADVERTENCIA: Datos de docentes insuficientes")
                print("   💡 RECOMENDACIÓN: Recolectar más datos de docentes")
        
        self.results['data_quality'] = data_analysis
        return data_analysis
    
    def improve_data_preprocessing(self):
        """
        FASE 2: Mejora del preprocesamiento de datos
        """
        print("\n🔧 FASE 2: MEJORA DEL PREPROCESAMIENTO")
        print("=" * 50)
        
        from clustering.data_preprocessing import DataPreprocessor
        
        preprocessor = DataPreprocessor(data_path=self.data_path)
        
        # Cargar datos
        data_dict = preprocessor.load_and_analyze_data()
        
        if not data_dict:
            print("❌ No se pudieron cargar los archivos CSV")
            return None
        
        # Extraer características con mejor manejo de errores
        features_dict = self._extract_features_improved(data_dict)
        print(f"✅ Características extraídas: {len(features_dict)} fuentes")
        
        # Crear dataset sintético mejorado
        print("\n🔄 Generando dataset sintético mejorado...")
        dataset = self._create_improved_synthetic_dataset(features_dict)
        print(f"✅ Dataset creado: {dataset.shape}")
        
        # Preprocesar con mejor manejo de valores faltantes
        dataset_processed = self._improved_preprocessing(dataset)
        print(f"✅ Datos preprocesados: {dataset_processed.shape}")
        
        # Verificar que no se pierdan datos importantes
        if dataset_processed.empty:
            print("❌ ERROR: Dataset vacío después del preprocesamiento")
            print("🔧 Aplicando correcciones...")
            dataset_processed = self._fix_empty_dataset(dataset)
        
        self.results['preprocessing'] = {
            'original_shape': dataset.shape,
            'processed_shape': dataset_processed.shape,
            'data_loss': dataset.shape[0] - dataset_processed.shape[0]
        }
        
        return dataset_processed
    
    def _extract_features_improved(self, data_dict):
        """
        Extracción mejorada de características con mejor manejo de errores
        """
        features = {}
        
        for name, df in data_dict.items():
            try:
                # Mejorar el manejo de porcentajes
                numeric_features = {}
                
                for col in df.columns[1:]:  # Excluir primera columna
                    if isinstance(col, str) and any(keyword in col.lower() for keyword in ['rural', 'urbana', 'municipal', 'ps', 'pp']):
                        values = []
                        for val in df[col]:
                            if pd.isna(val):
                                values.append(0)
                            elif isinstance(val, str):
                                if '%' in val:
                                    try:
                                        num_val = float(val.replace('%', '').replace(',', '.'))
                                        values.append(num_val)
                                    except:
                                        values.append(0)
                                else:
                                    values.append(0)
                            else:
                                values.append(float(val) if val is not None else 0)
                        
                        if values:
                            numeric_features[f'{name}_{col.lower().replace(" ", "_")}'] = np.mean(values)
                
                features[name] = numeric_features
                
            except Exception as e:
                print(f"⚠️  Error procesando {name}: {e}")
                features[name] = {}
        
        return features
    
    def _create_improved_synthetic_dataset(self, features_dict):
        """
        Crea un dataset sintético mejorado con mejor distribución
        """
        # Crear perfiles sintéticos más diversos
        n_profiles = 200  # Aumentar el número de perfiles
        
        synthetic_data = []
        
        # Perfiles de docentes (40%)
        for i in range(int(n_profiles * 0.4)):
            profile = self._generate_synthetic_profile('profesor', features_dict)
            synthetic_data.append(profile)
        
        # Perfiles de directores (30%)
        for i in range(int(n_profiles * 0.3)):
            profile = self._generate_synthetic_profile('director', features_dict)
            synthetic_data.append(profile)
        
        # Perfiles de asistentes (30%)
        for i in range(int(n_profiles * 0.3)):
            profile = self._generate_synthetic_profile('asistente', features_dict)
            synthetic_data.append(profile)
        
        df = pd.DataFrame(synthetic_data)
        return df
    
    def _generate_synthetic_profile(self, role, features_dict):
        """
        Genera un perfil sintético más realista
        """
        # Valores base según el rol
        if role == 'profesor':
            digital_skills = np.random.normal(3.5, 1.0)
            leadership_support = np.random.normal(2.5, 1.0)
            resource_support = np.random.normal(2.5, 1.0)
        elif role == 'director':
            digital_skills = np.random.normal(3.0, 1.2)
            leadership_support = np.random.normal(4.0, 0.8)
            resource_support = np.random.normal(3.5, 1.0)
        else:  # asistente
            digital_skills = np.random.normal(2.5, 1.2)
            leadership_support = np.random.normal(2.0, 1.0)
            resource_support = np.random.normal(2.0, 1.0)
        
        # Asegurar valores en rango [1, 5]
        digital_skills = np.clip(digital_skills, 1, 5)
        leadership_support = np.clip(leadership_support, 1, 5)
        resource_support = np.clip(resource_support, 1, 5)
        
        profile = {
            'digital_tools_skill': digital_skills,
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
            'interest_digital_literacy': np.random.choice([True, False], p=[0.6, 0.4]),
            'interest_educational_innovation': np.random.choice([True, False], p=[0.5, 0.5]),
            'interest_leadership': np.random.choice([True, False], p=[0.3, 0.7])
        }
        
        return profile
    
    def _improved_preprocessing(self, df):
        """
        Preprocesamiento mejorado con mejor manejo de valores faltantes
        """
        df_processed = df.copy()
        
        # Manejar valores faltantes de manera más inteligente
        numeric_cols = df_processed.select_dtypes(include=[np.number]).columns
        categorical_cols = df_processed.select_dtypes(include=['object', 'bool']).columns
        
        # Para columnas numéricas, usar mediana en lugar de eliminar
        for col in numeric_cols:
            if df_processed[col].isnull().any():
                median_val = df_processed[col].median()
                df_processed[col].fillna(median_val, inplace=True)
        
        # Para columnas categóricas, usar moda
        for col in categorical_cols:
            if df_processed[col].isnull().any():
                mode_val = df_processed[col].mode().iloc[0] if not df_processed[col].mode().empty else 'unknown'
                df_processed[col].fillna(mode_val, inplace=True)
        
        return df_processed
    
    def _fix_empty_dataset(self, original_df):
        """
        Corrige dataset vacío aplicando preprocesamiento más conservador
        """
        print("🔧 Aplicando preprocesamiento conservador...")
        
        df_fixed = original_df.copy()
        
        # Solo eliminar filas con más del 50% de valores faltantes
        threshold = len(df_fixed.columns) * 0.5
        df_fixed = df_fixed.dropna(thresh=threshold)
        
        # Para el resto, usar imputación simple
        df_fixed = df_fixed.fillna(df_fixed.median())
        
        print(f"✅ Dataset corregido: {df_fixed.shape}")
        return df_fixed
    
    def improve_feature_engineering(self, dataset):
        """
        FASE 3: Mejora de la ingeniería de características
        """
        print("\n🔧 FASE 3: MEJORA DE INGENIERÍA DE CARACTERÍSTICAS")
        print("=" * 50)
        
        from clustering.feature_engineering import FeatureEngineer
        
        feature_engineer = FeatureEngineer()
        
        # Crear características derivadas
        dataset_enhanced = feature_engineer.create_derived_features(dataset)
        print(f"✅ Características derivadas creadas: {dataset_enhanced.shape}")
        
        # Selección mejorada de características
        print("\n🔍 Analizando importancia de características...")
        dataset_final = self._improved_feature_selection(dataset_enhanced)
        print(f"✅ Características seleccionadas: {dataset_final.shape}")
        
        # Análisis de correlación para evitar redundancia
        correlation_analysis = self._analyze_feature_correlation(dataset_final)
        
        self.results['feature_engineering'] = {
            'original_features': dataset.shape[1],
            'derived_features': dataset_enhanced.shape[1],
            'selected_features': dataset_final.shape[1],
            'correlation_analysis': correlation_analysis
        }
        
        return dataset_final
    
    def _improved_feature_selection(self, df):
        """
        Selección mejorada de características usando múltiples métodos
        """
        # Separar características numéricas y categóricas
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(include=['object', 'bool']).columns
        
        # Para características numéricas, usar análisis de varianza
        if len(numeric_cols) > 0:
            X_numeric = df[numeric_cols].values
            y_dummy = np.random.randint(0, 2, len(X_numeric))  # Variable dummy para análisis
            
            # Usar SelectKBest con f_classif
            selector = SelectKBest(score_func=f_classif, k=min(10, len(numeric_cols)))
            X_selected = selector.fit_transform(X_numeric, y_dummy)
            
            # Obtener nombres de características seleccionadas
            selected_features = numeric_cols[selector.get_support()].tolist()
        else:
            selected_features = []
        
        # Incluir características categóricas importantes
        important_categorical = ['role', 'school_type', 'dependency', 'age_range', 'learning_format']
        for col in important_categorical:
            if col in categorical_cols:
                selected_features.append(col)
        
        # Incluir características booleanas de interés
        interest_cols = [col for col in categorical_cols if 'interest' in col]
        selected_features.extend(interest_cols)
        
        # Crear dataset final
        df_final = df[selected_features].copy()
        
        # Codificar características categóricas
        for col in df_final.select_dtypes(include=['object']).columns:
            df_final[col] = pd.Categorical(df_final[col]).codes
        
        return df_final
    
    def _analyze_feature_correlation(self, df):
        """
        Analiza correlación entre características para identificar redundancia
        """
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {}
        
        corr_matrix = numeric_df.corr()
        
        # Encontrar pares con alta correlación (> 0.8)
        high_corr_pairs = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                if abs(corr_matrix.iloc[i, j]) > 0.8:
                    high_corr_pairs.append({
                        'feature1': corr_matrix.columns[i],
                        'feature2': corr_matrix.columns[j],
                        'correlation': corr_matrix.iloc[i, j]
                    })
        
        return {
            'high_correlation_pairs': high_corr_pairs,
            'correlation_matrix_shape': corr_matrix.shape
        }
    
    def improve_clustering_model(self, dataset):
        """
        FASE 4: Mejora del modelo de clustering
        """
        print("\n🎯 FASE 4: MEJORA DEL MODELO DE CLUSTERING")
        print("=" * 50)
        
        # Preparar datos
        X = dataset.values
        
        # Normalización robusta
        scaler = RobustScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Probar diferentes algoritmos de clustering
        algorithms = {
            'KMeans++': KMeans(n_clusters=4, random_state=42, n_init=20, max_iter=500),
            'DBSCAN': DBSCAN(eps=0.5, min_samples=5),
            'Hierarchical': AgglomerativeClustering(n_clusters=4)
        }
        
        results = {}
        
        for name, algorithm in algorithms.items():
            print(f"\n🔍 Probando {name}...")
            
            try:
                # Entrenar modelo
                labels = algorithm.fit_predict(X_scaled)
                
                # Calcular métricas
                if len(set(labels)) > 1:  # Al menos 2 clusters
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
                    'algorithm': algorithm
                }
                
                print(f"   Silhouette: {silhouette:.3f}")
                print(f"   Calinski: {calinski:.2f}")
                print(f"   Clusters: {len(set(labels))}")
                
            except Exception as e:
                print(f"   ❌ Error con {name}: {e}")
                results[name] = None
        
        # Seleccionar mejor algoritmo
        best_algorithm = self._select_best_algorithm(results)
        
        self.results['clustering'] = {
            'algorithms_tested': len(results),
            'best_algorithm': best_algorithm,
            'all_results': results
        }
        
        return best_algorithm, X_scaled
    
    def _select_best_algorithm(self, results):
        """
        Selecciona el mejor algoritmo basado en métricas
        """
        valid_results = {k: v for k, v in results.items() if v is not None}
        
        if not valid_results:
            print("❌ Ningún algoritmo funcionó correctamente")
            return None
        
        # Calcular score compuesto
        for name, result in valid_results.items():
            # Normalizar scores (0-1)
            silhouette_norm = max(0, result['silhouette_score'])  # Silhouette ya está en [0,1]
            calinski_norm = min(1, result['calinski_score'] / 1000)  # Normalizar Calinski
            
            # Score compuesto (peso 0.7 para Silhouette, 0.3 para Calinski)
            composite_score = 0.7 * silhouette_norm + 0.3 * calinski_norm
            result['composite_score'] = composite_score
        
        # Seleccionar el mejor
        best_name = max(valid_results.keys(), key=lambda k: valid_results[k]['composite_score'])
        best_result = valid_results[best_name]
        
        print(f"\n🏆 Mejor algoritmo: {best_name}")
        print(f"   Score compuesto: {best_result['composite_score']:.3f}")
        print(f"   Silhouette: {best_result['silhouette_score']:.3f}")
        print(f"   Calinski: {best_result['calinski_score']:.2f}")
        
        return best_name, best_result
    
    def improve_auto_assignment(self, clustering_result, X_scaled):
        """
        FASE 5: Mejora del sistema de asignación automática
        """
        print("\n🤖 FASE 5: MEJORA DEL SISTEMA DE ASIGNACIÓN AUTOMÁTICA")
        print("=" * 50)
        
        if clustering_result is None:
            print("❌ No hay modelo de clustering válido")
            return None
        
        algorithm_name, result = clustering_result
        algorithm = result['algorithm']
        labels = result['labels']
        scaler = result['scaler']
        
        # Crear mapeo de clusters mejorado
        cluster_mapping = self._create_improved_cluster_mapping(labels, X_scaled)
        
        # Probar asignaciones automáticas
        test_results = self._test_auto_assignments(algorithm, cluster_mapping, X_scaled)
        
        self.results['auto_assignment'] = {
            'algorithm_used': algorithm_name,
            'cluster_mapping': cluster_mapping,
            'test_results': test_results
        }
        
        return algorithm, cluster_mapping
    
    def _create_improved_cluster_mapping(self, labels, X_scaled):
        """
        Crea mapeo mejorado de clusters a grupos de formación
        """
        unique_labels = set(labels)
        cluster_centers = {}
        
        # Calcular centroides de cada cluster
        for label in unique_labels:
            if label != -1:  # Excluir ruido (DBSCAN)
                cluster_points = X_scaled[labels == label]
                cluster_centers[label] = np.mean(cluster_points, axis=0)
        
        # Mapear clusters a grupos de formación basado en características
        cluster_mapping = {}
        
        for label in unique_labels:
            if label == -1:
                cluster_mapping[label] = 'Sin asignar'
            else:
                # Analizar características del cluster para determinar grupo
                center = cluster_centers[label]
                
                # Lógica de mapeo basada en características
                if center[0] > 0.5:  # Alta habilidad digital
                    cluster_mapping[label] = 'Innovación Educativa'
                elif center[1] > 0.5:  # Alto apoyo institucional
                    cluster_mapping[label] = 'Fortalecimiento Institucional'
                elif center[2] > 0.5:  # Alto interés en liderazgo
                    cluster_mapping[label] = 'Liderazgo Educativo'
                else:
                    cluster_mapping[label] = 'Alfabetización Digital Básica'
        
        return cluster_mapping
    
    def _test_auto_assignments(self, algorithm, cluster_mapping, X_scaled):
        """
        Prueba el sistema de asignación automática
        """
        # Crear perfiles de prueba
        test_profiles = self._create_test_profiles()
        
        results = {
            'agreement_count': 0,
            'total_tests': len(test_profiles),
            'assignments': []
        }
        
        for i, profile in enumerate(test_profiles):
            # Preparar perfil para clustering
            profile_scaled = self._prepare_profile_for_clustering(profile, X_scaled)
            
            # Predecir cluster
            predicted_label = algorithm.predict(profile_scaled.reshape(1, -1))[0]
            
            # Obtener asignación automática
            auto_assignment = cluster_mapping.get(predicted_label, 'Sin asignar')
            
            # Asignación manual esperada
            manual_assignment = self._get_expected_manual_assignment(profile)
            
            # Comparar
            agreement = auto_assignment == manual_assignment
            
            results['assignments'].append({
                'profile_id': i+1,
                'auto_assignment': auto_assignment,
                'manual_assignment': manual_assignment,
                'agreement': agreement
            })
            
            if agreement:
                results['agreement_count'] += 1
        
        # Calcular confianza
        confidence = results['agreement_count'] / results['total_tests']
        results['confidence'] = confidence
        
        print(f"✅ Pruebas completadas: {results['agreement_count']}/{results['total_tests']} acuerdos")
        print(f"   Confianza: {confidence:.2f}")
        
        return results
    
    def _create_test_profiles(self):
        """
        Crea perfiles de prueba más diversos
        """
        profiles = []
        
        # Perfil 1: Alfabetización Digital Básica
        profile1 = {
            'digital_tools_skill': 2,
            'advanced_tic_skill': 1,
            'digital_citizenship_skill': 2,
            'teaching_tech_skill': 1,
            'leadership_support': 2,
            'resource_support': 2,
            'role': 'profesor',
            'school_type': 'rural',
            'dependency': 'municipal',
            'age_range': '41-50',
            'learning_format': 'autoaprendizaje',
            'interest_digital_literacy': True,
            'interest_educational_innovation': False,
            'interest_leadership': False
        }
        profiles.append(profile1)
        
        # Perfil 2: Fortalecimiento Institucional
        profile2 = {
            'digital_tools_skill': 3,
            'advanced_tic_skill': 3,
            'digital_citizenship_skill': 3,
            'teaching_tech_skill': 3,
            'leadership_support': 4,
            'resource_support': 4,
            'role': 'director',
            'school_type': 'urbana',
            'dependency': 'municipal',
            'age_range': '51+',
            'learning_format': 'talleres',
            'interest_digital_literacy': False,
            'interest_educational_innovation': False,
            'interest_leadership': True
        }
        profiles.append(profile2)
        
        # Perfil 3: Innovación Educativa
        profile3 = {
            'digital_tools_skill': 4,
            'advanced_tic_skill': 4,
            'digital_citizenship_skill': 4,
            'teaching_tech_skill': 4,
            'leadership_support': 4,
            'resource_support': 4,
            'role': 'profesor',
            'school_type': 'cientifico-humanistica',
            'dependency': 'privada-subvencionada',
            'age_range': '31-40',
            'learning_format': 'en-linea',
            'interest_digital_literacy': False,
            'interest_educational_innovation': True,
            'interest_leadership': False
        }
        profiles.append(profile3)
        
        # Perfil 4: Liderazgo Educativo
        profile4 = {
            'digital_tools_skill': 3,
            'advanced_tic_skill': 3,
            'digital_citizenship_skill': 3,
            'teaching_tech_skill': 3,
            'leadership_support': 5,
            'resource_support': 4,
            'role': 'director',
            'school_type': 'tecnico-profesional',
            'dependency': 'privada-pagada',
            'age_range': '41-50',
            'learning_format': 'talleres',
            'interest_digital_literacy': False,
            'interest_educational_innovation': False,
            'interest_leadership': True
        }
        profiles.append(profile4)
        
        return profiles
    
    def _prepare_profile_for_clustering(self, profile, X_scaled):
        """
        Prepara un perfil para clustering
        """
        # Convertir perfil a array numérico
        profile_array = np.array([
            profile['digital_tools_skill'],
            profile['advanced_tic_skill'],
            profile['digital_citizenship_skill'],
            profile['teaching_tech_skill'],
            profile['leadership_support'],
            profile['resource_support'],
            profile.get('role_encoded', 0),
            profile.get('school_type_encoded', 0),
            profile.get('dependency_encoded', 0),
            profile.get('age_range_encoded', 0),
            profile.get('learning_format_encoded', 0),
            int(profile['interest_digital_literacy']),
            int(profile['interest_educational_innovation']),
            int(profile['interest_leadership'])
        ])
        
        # Normalizar usando la misma escala que los datos de entrenamiento
        scaler = RobustScaler()
        scaler.fit(X_scaled)  # Ajustar con datos de entrenamiento
        profile_scaled = scaler.transform(profile_array.reshape(1, -1))
        
        return profile_scaled.flatten()
    
    def _get_expected_manual_assignment(self, profile):
        """
        Determina la asignación manual esperada basada en el perfil
        """
        # Lógica de asignación manual
        digital_skills_avg = (profile['digital_tools_skill'] + 
                             profile['advanced_tic_skill'] + 
                             profile['digital_citizenship_skill'] + 
                             profile['teaching_tech_skill']) / 4
        
        if digital_skills_avg >= 4:
            return 'Innovación Educativa'
        elif profile['leadership_support'] >= 4 and profile['interest_leadership']:
            return 'Liderazgo Educativo'
        elif profile['leadership_support'] >= 3 and profile['resource_support'] >= 3:
            return 'Fortalecimiento Institucional'
        else:
            return 'Alfabetización Digital Básica'
    
    def generate_recommendations(self):
        """
        FASE 6: Generación de recomendaciones de mejora
        """
        print("\n📋 FASE 6: RECOMENDACIONES DE MEJORA")
        print("=" * 50)
        
        recommendations = []
        
        # Análisis de datos
        if 'data_quality' in self.results:
            data_quality = self.results['data_quality']
            
            # Verificar balance de datos
            if 'docentes' in data_quality:
                docentes_count = data_quality['docentes']['shape'][0]
                total_count = sum(data['shape'][0] for data in data_quality.values())
                
                if docentes_count / total_count < 0.3:
                    recommendations.append({
                        'category': 'Datos',
                        'priority': 'Alta',
                        'issue': 'Datos de docentes insuficientes',
                        'recommendation': 'Recolectar más datos de docentes para mejorar el balance'
                    })
        
        # Análisis de preprocesamiento
        if 'preprocessing' in self.results:
            preprocessing = self.results['preprocessing']
            
            if preprocessing['data_loss'] > 0:
                recommendations.append({
                    'category': 'Preprocesamiento',
                    'priority': 'Media',
                    'issue': f'Pérdida de {preprocessing["data_loss"]} registros',
                    'recommendation': 'Revisar criterios de limpieza para evitar pérdida de datos importantes'
                })
        
        # Análisis de características
        if 'feature_engineering' in self.results:
            feature_eng = self.results['feature_engineering']
            
            if feature_eng['selected_features'] < feature_eng['derived_features'] * 0.6:
                recommendations.append({
                    'category': 'Características',
                    'priority': 'Media',
                    'issue': 'Muchas características eliminadas',
                    'recommendation': 'Revisar criterios de selección de características'
                })
        
        # Análisis de clustering
        if 'clustering' in self.results:
            clustering = self.results['clustering']
            
            if clustering['best_algorithm']:
                best_name, best_result = clustering['best_algorithm']
                
                if best_result['silhouette_score'] < 0.2:
                    recommendations.append({
                        'category': 'Clustering',
                        'priority': 'Alta',
                        'issue': f'Silhouette Score bajo: {best_result["silhouette_score"]:.3f}',
                        'recommendation': 'Probar diferentes algoritmos o ajustar parámetros'
                    })
        
        # Análisis de asignación automática
        if 'auto_assignment' in self.results:
            auto_assignment = self.results['auto_assignment']
            
            if 'test_results' in auto_assignment:
                test_results = auto_assignment['test_results']
                
                if test_results['confidence'] < 0.7:
                    recommendations.append({
                        'category': 'Asignación Automática',
                        'priority': 'Alta',
                        'issue': f'Confianza baja: {test_results["confidence"]:.2f}',
                        'recommendation': 'Mejorar el mapeo de clusters y la lógica de asignación'
                    })
        
        # Mostrar recomendaciones
        print(f"\n📊 RESUMEN DE RECOMENDACIONES:")
        print(f"   Total de recomendaciones: {len(recommendations)}")
        
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. [{rec['priority']}] {rec['category']}")
            print(f"   Problema: {rec['issue']}")
            print(f"   Recomendación: {rec['recommendation']}")
        
        return recommendations
    
    def run_complete_analysis(self):
        """
        Ejecuta el análisis completo
        """
        print("🚀 INICIANDO ANÁLISIS COMPLETO DEL SISTEMA DE CLUSTERING")
        print("=" * 60)
        
        # FASE 1: Análisis de calidad de datos
        data_quality = self.analyze_data_quality()
        
        # FASE 2: Mejora del preprocesamiento
        dataset = self.improve_data_preprocessing()
        
        if dataset is None or dataset.empty:
            print("❌ No se pudo crear un dataset válido")
            return
        
        # FASE 3: Mejora de ingeniería de características
        dataset_enhanced = self.improve_feature_engineering(dataset)
        
        # FASE 4: Mejora del modelo de clustering
        clustering_result = self.improve_clustering_model(dataset_enhanced)
        
        # FASE 5: Mejora del sistema de asignación automática
        auto_assignment_result = self.improve_auto_assignment(clustering_result, dataset_enhanced.values)
        
        # FASE 6: Generación de recomendaciones
        recommendations = self.generate_recommendations()
        
        print("\n🎉 ANÁLISIS COMPLETADO")
        print("=" * 60)
        
        return {
            'data_quality': data_quality,
            'dataset': dataset,
            'dataset_enhanced': dataset_enhanced,
            'clustering_result': clustering_result,
            'auto_assignment_result': auto_assignment_result,
            'recommendations': recommendations
        }

def main():
    """
    Función principal
    """
    analyzer = ClusteringAnalyzer()
    results = analyzer.run_complete_analysis()
    
    return results

if __name__ == "__main__":
    main() 