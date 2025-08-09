#!/usr/bin/env python3
"""
Script para implementar mejoras específicas del sistema de clustering
Basado en el análisis de resultados y recomendaciones
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import warnings
warnings.filterwarnings('ignore')

class ClusteringImprovements:
    """
    Implementa mejoras específicas al sistema de clustering
    """
    
    def __init__(self):
        self.data_path = 'data/'
        self.improved_model_path = 'improved_clustering_model.pkl'
        self.results = {}
        
    def implement_data_improvements(self):
        """
        MEJORA 1: Mejorar la calidad y diversidad de datos
        """
        print("🔧 MEJORA 1: CALIDAD Y DIVERSIDAD DE DATOS")
        print("=" * 50)
        
        # Cargar datos existentes
        data_files = {
            'asistentes': 'Asistentes.csv',
            'directores': 'Directores.csv', 
            'docentes': 'RespuestasDocentes.csv',
            'docentes_directores': 'RespuesDocentesYDirectores.csv'
        }
        
        # Analizar balance actual
        data_analysis = {}
        total_records = 0
        
        for name, filename in data_files.items():
            filepath = os.path.join(self.data_path, filename)
            if os.path.exists(filepath):
                df = pd.read_csv(filepath, sep=';', encoding='utf-8')
                data_analysis[name] = df.shape[0]
                total_records += df.shape[0]
                print(f"📊 {name.capitalize()}: {df.shape[0]} registros")
        
        # Crear dataset sintético mejorado con mejor balance
        print("\n🔄 Generando dataset sintético mejorado...")
        improved_dataset = self._create_balanced_synthetic_dataset(data_analysis, total_records)
        
        print(f"✅ Dataset mejorado creado: {improved_dataset.shape}")
        print(f"   Distribución por rol:")
        role_counts = improved_dataset['role'].value_counts()
        for role, count in role_counts.items():
            percentage = (count / len(improved_dataset)) * 100
            print(f"   {role}: {count} ({percentage:.1f}%)")
        
        self.results['data_improvements'] = {
            'original_total': total_records,
            'improved_total': len(improved_dataset),
            'role_distribution': role_counts.to_dict()
        }
        
        return improved_dataset
    
    def _create_balanced_synthetic_dataset(self, data_analysis, total_records):
        """
        Crea un dataset sintético con mejor balance entre roles
        """
        # Determinar distribución objetivo
        target_distribution = {
            'profesor': 0.45,    # 45% docentes
            'director': 0.30,    # 30% directores
            'asistente': 0.25    # 25% asistentes
        }
        
        n_profiles = 300  # Aumentar significativamente el número de perfiles
        
        synthetic_data = []
        
        for role, percentage in target_distribution.items():
            n_role_profiles = int(n_profiles * percentage)
            
            for i in range(n_role_profiles):
                profile = self._generate_improved_synthetic_profile(role)
                synthetic_data.append(profile)
        
        df = pd.DataFrame(synthetic_data)
        
        # Asegurar que no hay valores faltantes
        df = df.fillna(df.median())
        
        return df
    
    def _generate_improved_synthetic_profile(self, role):
        """
        Genera un perfil sintético mejorado con características más realistas
        """
        # Parámetros base según el rol
        if role == 'profesor':
            # Docentes: variabilidad alta en habilidades digitales
            digital_skills_base = np.random.normal(3.2, 1.3)
            leadership_support = np.random.normal(2.8, 1.1)
            resource_support = np.random.normal(2.6, 1.2)
            innovation_interest = np.random.choice([True, False], p=[0.6, 0.4])
            leadership_interest = np.random.choice([True, False], p=[0.2, 0.8])
        elif role == 'director':
            # Directores: habilidades digitales moderadas, alto liderazgo
            digital_skills_base = np.random.normal(3.0, 1.1)
            leadership_support = np.random.normal(4.2, 0.8)
            resource_support = np.random.normal(3.8, 1.0)
            innovation_interest = np.random.choice([True, False], p=[0.4, 0.6])
            leadership_interest = np.random.choice([True, False], p=[0.8, 0.2])
        else:  # asistente
            # Asistentes: habilidades digitales básicas
            digital_skills_base = np.random.normal(2.5, 1.2)
            leadership_support = np.random.normal(2.2, 1.0)
            resource_support = np.random.normal(2.0, 1.1)
            innovation_interest = np.random.choice([True, False], p=[0.3, 0.7])
            leadership_interest = np.random.choice([True, False], p=[0.1, 0.9])
        
        # Asegurar valores en rango [1, 5]
        digital_skills_base = np.clip(digital_skills_base, 1, 5)
        leadership_support = np.clip(leadership_support, 1, 5)
        resource_support = np.clip(resource_support, 1, 5)
        
        # Generar habilidades digitales correlacionadas
        digital_tools = digital_skills_base + np.random.normal(0, 0.4)
        advanced_tic = digital_skills_base + np.random.normal(0, 0.5)
        digital_citizenship = digital_skills_base + np.random.normal(0, 0.3)
        teaching_tech = digital_skills_base + np.random.normal(0, 0.4)
        
        # Asegurar rango [1, 5]
        digital_tools = np.clip(digital_tools, 1, 5)
        advanced_tic = np.clip(advanced_tic, 1, 5)
        digital_citizenship = np.clip(digital_citizenship, 1, 5)
        teaching_tech = np.clip(teaching_tech, 1, 5)
        
        profile = {
            'digital_tools_skill': digital_tools,
            'advanced_tic_skill': advanced_tic,
            'digital_citizenship_skill': digital_citizenship,
            'teaching_tech_skill': teaching_tech,
            'leadership_support': leadership_support,
            'resource_support': resource_support,
            'role': role,
            'school_type': np.random.choice(['rural', 'urbana', 'cientifico-humanistica', 'tecnico-profesional']),
            'dependency': np.random.choice(['municipal', 'privada-subvencionada', 'privada-pagada']),
            'age_range': np.random.choice(['20-30', '31-40', '41-50', '51+']),
            'learning_format': np.random.choice(['en-linea', 'talleres', 'autoaprendizaje']),
            'interest_digital_literacy': np.random.choice([True, False], p=[0.5, 0.5]),
            'interest_educational_innovation': innovation_interest,
            'interest_leadership': leadership_interest
        }
        
        return profile
    
    def implement_preprocessing_improvements(self, dataset):
        """
        MEJORA 2: Mejorar el preprocesamiento de datos
        """
        print("\n🔧 MEJORA 2: PREPROCESAMIENTO DE DATOS")
        print("=" * 50)
        
        # Aplicar preprocesamiento mejorado
        dataset_processed = self._improved_preprocessing_pipeline(dataset)
        
        # Verificar integridad de datos
        data_integrity = self._verify_data_integrity(dataset_processed)
        
        print(f"✅ Datos preprocesados: {dataset_processed.shape}")
        print(f"   Valores faltantes: {data_integrity['missing_values']}")
        print(f"   Valores únicos por columna: {data_integrity['unique_values']}")
        
        self.results['preprocessing_improvements'] = {
            'original_shape': dataset.shape,
            'processed_shape': dataset_processed.shape,
            'data_integrity': data_integrity
        }
        
        return dataset_processed
    
    def _improved_preprocessing_pipeline(self, df):
        """
        Pipeline de preprocesamiento mejorado
        """
        df_processed = df.copy()
        
        # 1. Manejo inteligente de valores faltantes
        numeric_cols = df_processed.select_dtypes(include=[np.number]).columns
        categorical_cols = df_processed.select_dtypes(include=['object', 'bool']).columns
        
        # Para columnas numéricas: usar mediana por grupo
        for col in numeric_cols:
            if df_processed[col].isnull().any():
                # Calcular mediana por rol si es posible
                if 'role' in df_processed.columns:
                    median_by_role = df_processed.groupby('role')[col].median()
                    for role in df_processed['role'].unique():
                        mask = (df_processed['role'] == role) & (df_processed[col].isnull())
                        if role in median_by_role.index:
                            df_processed.loc[mask, col] = median_by_role[role]
                        else:
                            df_processed.loc[mask, col] = df_processed[col].median()
                else:
                    df_processed[col].fillna(df_processed[col].median(), inplace=True)
        
        # Para columnas categóricas: usar moda por grupo
        for col in categorical_cols:
            if df_processed[col].isnull().any():
                if 'role' in df_processed.columns:
                    mode_by_role = df_processed.groupby('role')[col].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else x.mode().iloc[0] if len(x.mode()) > 0 else 'unknown')
                    for role in df_processed['role'].unique():
                        mask = (df_processed['role'] == role) & (df_processed[col].isnull())
                        if role in mode_by_role.index:
                            df_processed.loc[mask, col] = mode_by_role[role]
                        else:
                            df_processed.loc[mask, col] = df_processed[col].mode().iloc[0] if not df_processed[col].mode().empty else 'unknown'
                else:
                    mode_val = df_processed[col].mode().iloc[0] if not df_processed[col].mode().empty else 'unknown'
                    df_processed[col].fillna(mode_val, inplace=True)
        
        # 2. Detección y manejo de outliers
        for col in numeric_cols:
            Q1 = df_processed[col].quantile(0.25)
            Q3 = df_processed[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Reemplazar outliers con valores límite
            df_processed[col] = df_processed[col].clip(lower_bound, upper_bound)
        
        # 3. Normalización de características numéricas
        for col in numeric_cols:
            if col in ['digital_tools_skill', 'advanced_tic_skill', 'digital_citizenship_skill', 'teaching_tech_skill', 'leadership_support', 'resource_support']:
                # Normalizar a escala 1-5
                df_processed[col] = df_processed[col].clip(1, 5)
        
        return df_processed
    
    def _verify_data_integrity(self, df):
        """
        Verifica la integridad de los datos procesados
        """
        return {
            'missing_values': df.isnull().sum().sum(),
            'unique_values': {col: df[col].nunique() for col in df.columns},
            'data_types': df.dtypes.value_counts().to_dict(),
            'shape': df.shape
        }
    
    def implement_feature_engineering_improvements(self, dataset):
        """
        MEJORA 3: Mejorar la ingeniería de características
        """
        print("\n🔧 MEJORA 3: INGENIERÍA DE CARACTERÍSTICAS")
        print("=" * 50)
        
        from clustering.feature_engineering import FeatureEngineer
        
        feature_engineer = FeatureEngineer()
        
        # Crear características derivadas mejoradas
        dataset_enhanced = self._create_improved_derived_features(dataset)
        print(f"✅ Características derivadas creadas: {dataset_enhanced.shape}")
        
        # Selección de características mejorada
        dataset_selected = self._improved_feature_selection(dataset_enhanced)
        print(f"✅ Características seleccionadas: {dataset_selected.shape}")
        
        # Análisis de importancia de características
        feature_importance = self._analyze_feature_importance(dataset_selected)
        
        self.results['feature_engineering_improvements'] = {
            'original_features': dataset.shape[1],
            'derived_features': dataset_enhanced.shape[1],
            'selected_features': dataset_selected.shape[1],
            'feature_importance': feature_importance
        }
        
        return dataset_selected
    
    def _create_improved_derived_features(self, df):
        """
        Crea características derivadas mejoradas
        """
        df_enhanced = df.copy()
        
        # 1. Índices compuestos mejorados
        digital_skills_cols = ['digital_tools_skill', 'advanced_tic_skill', 'digital_citizenship_skill', 'teaching_tech_skill']
        df_enhanced['digital_skills_index'] = df_enhanced[digital_skills_cols].mean(axis=1)
        df_enhanced['digital_skills_std'] = df_enhanced[digital_skills_cols].std(axis=1)
        
        institutional_cols = ['leadership_support', 'resource_support']
        df_enhanced['institutional_support_index'] = df_enhanced[institutional_cols].mean(axis=1)
        
        # 2. Indicadores de brecha y necesidad
        df_enhanced['skills_support_gap'] = df_enhanced['digital_skills_index'] - df_enhanced['institutional_support_index']
        df_enhanced['digital_literacy_need'] = (5 - df_enhanced['digital_skills_index']) * df_enhanced['interest_digital_literacy']
        
        # 3. Perfiles de innovación y liderazgo mejorados
        innovation_score = (df_enhanced['interest_educational_innovation'] * 2 + 
                          df_enhanced['interest_digital_literacy'] + 
                          df_enhanced['interest_leadership'])
        df_enhanced['innovation_profile'] = innovation_score
        
        leadership_score = (df_enhanced['interest_leadership'] * 2 + 
                          df_enhanced['leadership_support'])
        df_enhanced['leadership_profile'] = leadership_score
        
        # 4. Capacidad de innovación educativa
        innovation_capacity = (df_enhanced['digital_skills_index'] * 
                             df_enhanced['interest_educational_innovation'] * 
                             df_enhanced['institutional_support_index'])
        df_enhanced['innovation_capacity'] = innovation_capacity
        
        # 5. Codificación mejorada de características categóricas
        df_enhanced['rural_urban_profile'] = self._encode_school_profile(df_enhanced['school_type'])
        df_enhanced['dependency_profile'] = self._encode_dependency_profile(df_enhanced['dependency'])
        df_enhanced['age_profile'] = self._encode_age_profile(df_enhanced['age_range'])
        df_enhanced['learning_profile'] = self._encode_learning_profile(df_enhanced['learning_format'])
        
        # 6. Interacciones entre características
        df_enhanced['digital_leadership_interaction'] = df_enhanced['digital_skills_index'] * df_enhanced['leadership_profile']
        df_enhanced['innovation_support_interaction'] = df_enhanced['innovation_profile'] * df_enhanced['institutional_support_index']
        
        return df_enhanced
    
    def _encode_school_profile(self, school_type_series):
        """Codifica el tipo de escuela"""
        encoding = {
            'rural': 1,
            'urbana': 2, 
            'cientifico-humanistica': 3,
            'tecnico-profesional': 4
        }
        return school_type_series.map(encoding)
    
    def _encode_dependency_profile(self, dependency_series):
        """Codifica la dependencia"""
        encoding = {
            'municipal': 1,
            'privada-subvencionada': 2,
            'privada-pagada': 3
        }
        return dependency_series.map(encoding)
    
    def _encode_age_profile(self, age_series):
        """Codifica el rango de edad"""
        encoding = {
            '20-30': 1,
            '31-40': 2,
            '41-50': 3,
            '51+': 4
        }
        return age_series.map(encoding)
    
    def _encode_learning_profile(self, learning_series):
        """Codifica el formato de aprendizaje"""
        encoding = {
            'autoaprendizaje': 1,
            'talleres': 2,
            'en-linea': 3
        }
        return learning_series.map(encoding)
    
    def _improved_feature_selection(self, df):
        """
        Selección de características mejorada usando múltiples criterios
        """
        # Separar características numéricas y categóricas
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(include=['object', 'bool']).columns
        
        selected_features = []
        
        # 1. Selección de características numéricas usando análisis de varianza
        if len(numeric_cols) > 0:
            X_numeric = df[numeric_cols].values
            y_dummy = np.random.randint(0, 2, len(X_numeric))
            
            # Usar SelectKBest con f_classif
            k_best = min(12, len(numeric_cols))
            selector = SelectKBest(score_func=f_classif, k=k_best)
            X_selected = selector.fit_transform(X_numeric, y_dummy)
            
            selected_numeric = numeric_cols[selector.get_support()].tolist()
            selected_features.extend(selected_numeric)
        
        # 2. Incluir características categóricas importantes
        important_categorical = ['role', 'school_type', 'dependency', 'age_range', 'learning_format']
        for col in important_categorical:
            if col in categorical_cols:
                selected_features.append(col)
        
        # 3. Incluir características booleanas de interés
        interest_cols = [col for col in categorical_cols if 'interest' in col]
        selected_features.extend(interest_cols)
        
        # 4. Crear dataset final
        df_final = df[selected_features].copy()
        
        # 5. Codificar características categóricas
        for col in df_final.select_dtypes(include=['object']).columns:
            df_final[col] = pd.Categorical(df_final[col]).codes
        
        return df_final
    
    def _analyze_feature_importance(self, df):
        """
        Analiza la importancia de las características
        """
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {}
        
        # Calcular correlación con variable objetivo (usar primera columna como proxy)
        correlations = {}
        for col in numeric_df.columns:
            if col != numeric_df.columns[0]:
                corr = abs(numeric_df[col].corr(numeric_df.iloc[:, 0]))
                correlations[col] = corr
        
        # Ordenar por importancia
        sorted_features = sorted(correlations.items(), key=lambda x: x[1], reverse=True)
        
        return {
            'top_features': sorted_features[:5],
            'correlation_matrix_shape': numeric_df.shape
        }
    
    def implement_clustering_improvements(self, dataset):
        """
        MEJORA 4: Mejorar el modelo de clustering
        """
        print("\n🔧 MEJORA 4: MODELO DE CLUSTERING")
        print("=" * 50)
        
        # Preparar datos
        X = dataset.values
        
        # Normalización robusta
        scaler = RobustScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Probar múltiples algoritmos con optimización de hiperparámetros
        algorithms = self._create_optimized_algorithms()
        
        results = {}
        
        for name, algorithm in algorithms.items():
            print(f"\n🔍 Probando {name}...")
            
            try:
                # Entrenar modelo
                labels = algorithm.fit_predict(X_scaled)
                
                # Calcular métricas
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
                
                print(f"   Silhouette: {silhouette:.3f}")
                print(f"   Calinski: {calinski:.2f}")
                print(f"   Clusters: {len(set(labels))}")
                
            except Exception as e:
                print(f"   ❌ Error con {name}: {e}")
                results[name] = None
        
        # Seleccionar mejor algoritmo
        best_algorithm = self._select_best_algorithm_improved(results)
        
        self.results['clustering_improvements'] = {
            'algorithms_tested': len(results),
            'best_algorithm': best_algorithm,
            'all_results': results
        }
        
        return best_algorithm, X_scaled
    
    def _create_optimized_algorithms(self):
        """
        Crea algoritmos de clustering optimizados
        """
        algorithms = {
            'KMeans++': KMeans(
                n_clusters=4, 
                random_state=42, 
                n_init=25, 
                max_iter=1000,
                init='k-means++'
            ),
            'KMeans++_Optimized': KMeans(
                n_clusters=4, 
                random_state=42, 
                n_init=50, 
                max_iter=1500,
                init='k-means++',
                tol=1e-5
            ),
            'DBSCAN_Conservative': DBSCAN(
                eps=0.3, 
                min_samples=8
            ),
            'DBSCAN_Aggressive': DBSCAN(
                eps=0.7, 
                min_samples=5
            ),
            'Hierarchical_Complete': AgglomerativeClustering(
                n_clusters=4,
                linkage='complete'
            ),
            'Hierarchical_Ward': AgglomerativeClustering(
                n_clusters=4,
                linkage='ward'
            )
        }
        
        return algorithms
    
    def _select_best_algorithm_improved(self, results):
        """
        Selecciona el mejor algoritmo usando criterios mejorados
        """
        valid_results = {k: v for k, v in results.items() if v is not None}
        
        if not valid_results:
            print("❌ Ningún algoritmo funcionó correctamente")
            return None
        
        # Calcular score compuesto mejorado
        for name, result in valid_results.items():
            # Normalizar scores
            silhouette_norm = max(0, result['silhouette_score'])
            calinski_norm = min(1, result['calinski_score'] / 2000)  # Ajustar escala
            
            # Score compuesto con pesos ajustados
            composite_score = 0.6 * silhouette_norm + 0.4 * calinski_norm
            result['composite_score'] = composite_score
        
        # Seleccionar el mejor
        best_name = max(valid_results.keys(), key=lambda k: valid_results[k]['composite_score'])
        best_result = valid_results[best_name]
        
        print(f"\n🏆 Mejor algoritmo: {best_name}")
        print(f"   Score compuesto: {best_result['composite_score']:.3f}")
        print(f"   Silhouette: {best_result['silhouette_score']:.3f}")
        print(f"   Calinski: {best_result['calinski_score']:.2f}")
        
        return best_name, best_result
    
    def implement_auto_assignment_improvements(self, clustering_result, X_scaled):
        """
        MEJORA 5: Mejorar el sistema de asignación automática
        """
        print("\n🔧 MEJORA 5: SISTEMA DE ASIGNACIÓN AUTOMÁTICA")
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
        
        # Probar asignaciones automáticas mejoradas
        test_results = self._test_improved_auto_assignments(algorithm, cluster_mapping, X_scaled, scaler)
        
        # Guardar modelo mejorado
        self._save_improved_model(algorithm, cluster_mapping, scaler)
        
        self.results['auto_assignment_improvements'] = {
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
        cluster_characteristics = {}
        
        # Calcular centroides y características de cada cluster
        for label in unique_labels:
            if label != -1:  # Excluir ruido (DBSCAN)
                cluster_points = X_scaled[labels == label]
                cluster_centers[label] = np.mean(cluster_points, axis=0)
                cluster_characteristics[label] = {
                    'size': len(cluster_points),
                    'std': np.std(cluster_points, axis=0),
                    'center': cluster_centers[label]
                }
        
        # Mapear clusters a grupos de formación usando lógica mejorada
        cluster_mapping = {}
        
        for label in unique_labels:
            if label == -1:
                cluster_mapping[label] = 'Sin asignar'
            else:
                center = cluster_centers[label]
                characteristics = cluster_characteristics[label]
                
                # Lógica de mapeo mejorada basada en múltiples características
                digital_skills_level = center[0] if len(center) > 0 else 0
                institutional_support = center[1] if len(center) > 1 else 0
                innovation_interest = center[2] if len(center) > 2 else 0
                leadership_interest = center[3] if len(center) > 3 else 0
                
                # Determinar grupo basado en características dominantes
                if digital_skills_level > 0.5 and innovation_interest > 0.3:
                    cluster_mapping[label] = 'Innovación Educativa'
                elif institutional_support > 0.5 and leadership_interest > 0.3:
                    cluster_mapping[label] = 'Liderazgo Educativo'
                elif institutional_support > 0.3 and digital_skills_level > 0.2:
                    cluster_mapping[label] = 'Fortalecimiento Institucional'
                else:
                    cluster_mapping[label] = 'Alfabetización Digital Básica'
        
        return cluster_mapping
    
    def _test_improved_auto_assignments(self, algorithm, cluster_mapping, X_scaled, scaler):
        """
        Prueba el sistema de asignación automática mejorado
        """
        # Crear perfiles de prueba más diversos
        test_profiles = self._create_diverse_test_profiles()
        
        results = {
            'agreement_count': 0,
            'total_tests': len(test_profiles),
            'assignments': [],
            'confidence_scores': []
        }
        
        for i, profile in enumerate(test_profiles):
            # Preparar perfil para clustering
            profile_scaled = self._prepare_profile_for_clustering_improved(profile, scaler)
            
            # Predecir cluster
            predicted_label = algorithm.predict(profile_scaled.reshape(1, -1))[0]
            
            # Obtener asignación automática
            auto_assignment = cluster_mapping.get(predicted_label, 'Sin asignar')
            
            # Asignación manual esperada
            manual_assignment = self._get_expected_manual_assignment_improved(profile)
            
            # Calcular confianza
            confidence = self._calculate_assignment_confidence(profile, auto_assignment)
            
            # Comparar
            agreement = auto_assignment == manual_assignment
            
            results['assignments'].append({
                'profile_id': i+1,
                'auto_assignment': auto_assignment,
                'manual_assignment': manual_assignment,
                'agreement': agreement,
                'confidence': confidence
            })
            
            results['confidence_scores'].append(confidence)
            
            if agreement:
                results['agreement_count'] += 1
        
        # Calcular métricas finales
        results['overall_confidence'] = np.mean(results['confidence_scores'])
        results['agreement_rate'] = results['agreement_count'] / results['total_tests']
        
        print(f"✅ Pruebas completadas: {results['agreement_count']}/{results['total_tests']} acuerdos")
        print(f"   Tasa de acuerdo: {results['agreement_rate']:.2f}")
        print(f"   Confianza promedio: {results['overall_confidence']:.2f}")
        
        return results
    
    def _create_diverse_test_profiles(self):
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
        
        # Perfil 5: Caso límite
        profile5 = {
            'digital_tools_skill': 3,
            'advanced_tic_skill': 3,
            'digital_citizenship_skill': 3,
            'teaching_tech_skill': 3,
            'leadership_support': 3,
            'resource_support': 3,
            'role': 'profesor',
            'school_type': 'urbana',
            'dependency': 'municipal',
            'age_range': '31-40',
            'learning_format': 'talleres',
            'interest_digital_literacy': True,
            'interest_educational_innovation': True,
            'interest_leadership': False
        }
        profiles.append(profile5)
        
        return profiles
    
    def _prepare_profile_for_clustering_improved(self, profile, scaler):
        """
        Prepara un perfil para clustering con mejor normalización
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
        
        # Usar el scaler entrenado
        profile_scaled = scaler.transform(profile_array.reshape(1, -1))
        
        return profile_scaled.flatten()
    
    def _get_expected_manual_assignment_improved(self, profile):
        """
        Determina la asignación manual esperada con lógica mejorada
        """
        # Calcular índices compuestos
        digital_skills_avg = (profile['digital_tools_skill'] + 
                             profile['advanced_tic_skill'] + 
                             profile['digital_citizenship_skill'] + 
                             profile['teaching_tech_skill']) / 4
        
        institutional_support_avg = (profile['leadership_support'] + profile['resource_support']) / 2
        
        # Lógica de asignación mejorada
        if digital_skills_avg >= 4 and profile['interest_educational_innovation']:
            return 'Innovación Educativa'
        elif institutional_support_avg >= 4 and profile['interest_leadership']:
            return 'Liderazgo Educativo'
        elif institutional_support_avg >= 3 and digital_skills_avg >= 2.5:
            return 'Fortalecimiento Institucional'
        else:
            return 'Alfabetización Digital Básica'
    
    def _calculate_assignment_confidence(self, profile, assignment):
        """
        Calcula la confianza de una asignación
        """
        # Calcular características del perfil
        digital_skills_avg = (profile['digital_tools_skill'] + 
                             profile['advanced_tic_skill'] + 
                             profile['digital_citizenship_skill'] + 
                             profile['teaching_tech_skill']) / 4
        
        institutional_support_avg = (profile['leadership_support'] + profile['resource_support']) / 2
        
        # Calcular confianza basada en la claridad del perfil
        if assignment == 'Innovación Educativa':
            confidence = min(1.0, (digital_skills_avg / 5) * (profile['interest_educational_innovation'] * 0.8 + 0.2))
        elif assignment == 'Liderazgo Educativo':
            confidence = min(1.0, (institutional_support_avg / 5) * (profile['interest_leadership'] * 0.8 + 0.2))
        elif assignment == 'Fortalecimiento Institucional':
            confidence = min(1.0, (institutional_support_avg / 5) * 0.7)
        else:  # Alfabetización Digital Básica
            confidence = min(1.0, (1 - digital_skills_avg / 5) * 0.8)
        
        return confidence
    
    def _save_improved_model(self, algorithm, cluster_mapping, scaler):
        """
        Guarda el modelo mejorado
        """
        model_data = {
            'algorithm': algorithm,
            'cluster_mapping': cluster_mapping,
            'scaler': scaler,
            'improvement_version': '2.0'
        }
        
        joblib.dump(model_data, self.improved_model_path)
        print(f"💾 Modelo mejorado guardado en: {self.improved_model_path}")
    
    def run_improvements(self):
        """
        Ejecuta todas las mejoras del sistema
        """
        print("🚀 INICIANDO IMPLEMENTACIÓN DE MEJORAS DEL SISTEMA DE CLUSTERING")
        print("=" * 70)
        
        # MEJORA 1: Datos
        dataset = self.implement_data_improvements()
        
        # MEJORA 2: Preprocesamiento
        dataset_processed = self.implement_preprocessing_improvements(dataset)
        
        # MEJORA 3: Ingeniería de características
        dataset_enhanced = self.implement_feature_engineering_improvements(dataset_processed)
        
        # MEJORA 4: Clustering
        clustering_result = self.implement_clustering_improvements(dataset_enhanced)
        
        # MEJORA 5: Asignación automática
        auto_assignment_result = self.implement_auto_assignment_improvements(clustering_result, dataset_enhanced.values)
        
        print("\n🎉 IMPLEMENTACIÓN DE MEJORAS COMPLETADA")
        print("=" * 70)
        
        # Mostrar resumen de mejoras
        self._show_improvements_summary()
        
        return {
            'dataset': dataset,
            'dataset_processed': dataset_processed,
            'dataset_enhanced': dataset_enhanced,
            'clustering_result': clustering_result,
            'auto_assignment_result': auto_assignment_result
        }
    
    def _show_improvements_summary(self):
        """
        Muestra un resumen de las mejoras implementadas
        """
        print("\n📊 RESUMEN DE MEJORAS IMPLEMENTADAS")
        print("=" * 50)
        
        if 'data_improvements' in self.results:
            data_imp = self.results['data_improvements']
            print(f"📈 Datos: {data_imp['original_total']} → {data_imp['improved_total']} registros")
            print(f"   Distribución mejorada por rol")
        
        if 'preprocessing_improvements' in self.results:
            prep_imp = self.results['preprocessing_improvements']
            print(f"🔧 Preprocesamiento: {prep_imp['original_shape']} → {prep_imp['processed_shape']}")
            print(f"   Valores faltantes: {prep_imp['data_integrity']['missing_values']}")
        
        if 'feature_engineering_improvements' in self.results:
            feat_imp = self.results['feature_engineering_improvements']
            print(f"⚙️  Características: {feat_imp['original_features']} → {feat_imp['selected_features']}")
        
        if 'clustering_improvements' in self.results:
            clust_imp = self.results['clustering_improvements']
            print(f"🎯 Clustering: {clust_imp['algorithms_tested']} algoritmos probados")
            if clust_imp['best_algorithm']:
                best_name, best_result = clust_imp['best_algorithm']
                print(f"   Mejor algoritmo: {best_name}")
                print(f"   Silhouette Score: {best_result['silhouette_score']:.3f}")
        
        if 'auto_assignment_improvements' in self.results:
            auto_imp = self.results['auto_assignment_improvements']
            if 'test_results' in auto_imp:
                test_results = auto_imp['test_results']
                print(f"🤖 Asignación Automática:")
                print(f"   Tasa de acuerdo: {test_results['agreement_rate']:.2f}")
                print(f"   Confianza promedio: {test_results['overall_confidence']:.2f}")

def main():
    """
    Función principal
    """
    improvements = ClusteringImprovements()
    results = improvements.run_improvements()
    
    return results

if __name__ == "__main__":
    main() 