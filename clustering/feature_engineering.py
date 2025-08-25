"""
Feature Engineering para el sistema de clustering
"""
import pandas as pd
import numpy as np

class FeatureEngineer:
    """
    Clase para ingeniería de características del perfil de usuario
    """
    
    def __init__(self):
        self.feature_names = [
            'digital_tools_skill', 'advanced_tic_skill', 'digital_citizenship_skill', 
            'teaching_tech_skill', 'leadership_support', 'resource_support'
        ]
    
    def engineer_features(self, df):
        """
        Aplica ingeniería de características básica
        """
        try:
            # Crear copia para no modificar el original
            df_engineered = df.copy()
            
            # Asegurar que las columnas numéricas sean float
            for col in self.feature_names:
                if col in df_engineered.columns:
                    df_engineered[col] = pd.to_numeric(df_engineered[col], errors='coerce').fillna(3.0)
            
            # Normalizar características numéricas
            if len(df_engineered) > 0:
                df_engineered[self.feature_names] = df_engineered[self.feature_names].fillna(3.0)
            
            return df_engineered
            
        except Exception as e:
            print(f"Error en feature engineering: {e}")
            return df
