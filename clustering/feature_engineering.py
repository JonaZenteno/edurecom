import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif

class FeatureEngineer:
    """
    Crea características derivadas para mejorar el clustering
    """
    
    def __init__(self):
        self.pca = None
        self.feature_selector = None
        
    def create_derived_features(self, df):
        """
        Crea características derivadas basadas en el dominio educativo
        """
        df_enhanced = df.copy()
        
        # 1. Índice de habilidades digitales promedio
        digital_skills_cols = ['digital_tools_skill', 'advanced_tic_skill', 
                              'digital_citizenship_skill', 'teaching_tech_skill']
        df_enhanced['avg_digital_skills'] = df_enhanced[digital_skills_cols].mean(axis=1)
        
        # 2. Índice de apoyo institucional
        institutional_cols = ['leadership_support', 'resource_support']
        df_enhanced['avg_institutional_support'] = df_enhanced[institutional_cols].mean(axis=1)
        
        # 3. Gap entre habilidades y apoyo institucional
        df_enhanced['skills_support_gap'] = (df_enhanced['avg_digital_skills'] - 
                                           df_enhanced['avg_institutional_support'])
        
        # 4. Perfil de innovación (basado en intereses)
        innovation_score = (df_enhanced['interest_educational_innovation'] * 2 + 
                          df_enhanced['interest_digital_literacy'] + 
                          df_enhanced['interest_leadership'])
        df_enhanced['innovation_profile'] = innovation_score
        
        # 5. Perfil de liderazgo
        leadership_score = (df_enhanced['interest_leadership'] * 2 + 
                          df_enhanced['leadership_support'])
        df_enhanced['leadership_profile'] = leadership_score
        
        # 6. Necesidad de alfabetización digital
        digital_literacy_need = (5 - df_enhanced['avg_digital_skills']) * df_enhanced['interest_digital_literacy']
        df_enhanced['digital_literacy_need'] = digital_literacy_need
        
        # 7. Capacidad de innovación educativa
        innovation_capacity = (df_enhanced['avg_digital_skills'] * 
                             df_enhanced['interest_educational_innovation'] * 
                             df_enhanced['avg_institutional_support'])
        df_enhanced['innovation_capacity'] = innovation_capacity
        
        # 8. Perfil de establecimiento (codificado)
        df_enhanced['rural_urban_profile'] = self._encode_school_profile(df_enhanced['school_type'])
        df_enhanced['dependency_profile'] = self._encode_dependency_profile(df_enhanced['dependency'])
        
        # 9. Perfil de edad (codificado)
        df_enhanced['age_profile'] = self._encode_age_profile(df_enhanced['age_range'])
        
        # 10. Perfil de formato de aprendizaje (codificado)
        df_enhanced['learning_profile'] = self._encode_learning_profile(df_enhanced['learning_format'])
        
        return df_enhanced
    
    def _encode_school_profile(self, school_type_series):
        """
        Codifica el tipo de escuela en valores numéricos
        """
        encoding = {
            'rural': 1,
            'urbana': 2, 
            'cientifico-humanistica': 3,
            'tecnico-profesional': 4
        }
        return school_type_series.map(encoding)
    
    def _encode_dependency_profile(self, dependency_series):
        """
        Codifica la dependencia en valores numéricos
        """
        encoding = {
            'municipal': 1,
            'privada-subvencionada': 2,
            'privada-pagada': 3
        }
        return dependency_series.map(encoding)
    
    def _encode_age_profile(self, age_series):
        """
        Codifica el rango de edad en valores numéricos
        """
        encoding = {
            '20-30': 1,
            '31-40': 2,
            '41-50': 3,
            '51+': 4
        }
        return age_series.map(encoding)
    
    def _encode_learning_profile(self, learning_series):
        """
        Codifica el formato de aprendizaje en valores numéricos
        """
        encoding = {
            'en-linea': 1,
            'talleres': 2,
            'autoaprendizaje': 3
        }
        return learning_series.map(encoding)
    
    def select_best_features(self, df, target_col=None, k=15):
        """
        Selecciona las mejores características para clustering
        """
        # Si no hay target, usar características más relevantes para clustering
        if target_col is None:
            # Características más importantes para clustering educativo
            best_features = [
                'avg_digital_skills',
                'avg_institutional_support', 
                'skills_support_gap',
                'innovation_profile',
                'leadership_profile',
                'digital_literacy_need',
                'innovation_capacity',
                'rural_urban_profile',
                'dependency_profile',
                'age_profile',
                'learning_profile',
                'digital_tools_skill',
                'advanced_tic_skill',
                'teaching_tech_skill',
                'leadership_support'
            ]
            
            # Asegurar que todas las columnas existan
            available_features = [col for col in best_features if col in df.columns]
            return df[available_features]
        
        # Si hay target, usar selección automática
        else:
            self.feature_selector = SelectKBest(score_func=f_classif, k=k)
            X = df.drop(columns=[target_col])
            y = df[target_col]
            
            X_selected = self.feature_selector.fit_transform(X, y)
            selected_features = X.columns[self.feature_selector.get_support()].tolist()
            
            return df[selected_features + [target_col]]
    
    def reduce_dimensionality(self, df, n_components=8):
        """
        Reduce la dimensionalidad usando PCA
        """
        self.pca = PCA(n_components=n_components, random_state=42)
        df_reduced = self.pca.fit_transform(df)
        
        # Crear DataFrame con componentes principales
        columns = [f'PC_{i+1}' for i in range(n_components)]
        df_pca = pd.DataFrame(df_reduced, columns=columns)
        
        # Calcular varianza explicada
        explained_variance = self.pca.explained_variance_ratio_
        cumulative_variance = np.cumsum(explained_variance)
        
        print(f"📊 Varianza explicada por componentes principales:")
        for i, (var, cum_var) in enumerate(zip(explained_variance, cumulative_variance)):
            print(f"   PC_{i+1}: {var:.3f} ({cum_var:.3f} acumulado)")
        
        return df_pca
    
    def create_clustering_features(self, df):
        """
        Crea el conjunto final de características para clustering
        """
        # 1. Crear características derivadas
        df_enhanced = self.create_derived_features(df)
        
        # 2. Seleccionar mejores características
        df_selected = self.select_best_features(df_enhanced)
        
        # 3. Reducir dimensionalidad si es necesario
        if df_selected.shape[1] > 10:
            df_final = self.reduce_dimensionality(df_selected)
        else:
            df_final = df_selected
        
        return df_final
    
    def get_feature_importance(self):
        """
        Obtiene la importancia de las características
        """
        if self.feature_selector is not None:
            return self.feature_selector.scores_
        return None 