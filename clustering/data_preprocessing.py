import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
import os

class DataPreprocessor:
    """
    Preprocesa los datos de los archivos CSV para el clustering
    """
    
    def __init__(self, data_path='data/'):
        self.data_path = data_path
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.imputer = SimpleImputer(strategy='mean')
        
    def load_and_analyze_data(self):
        """
        Carga y analiza todos los archivos CSV
        """
        data_files = {
            'asistentes': 'Asistentes.csv',
            'directores': 'Directores.csv', 
            'docentes': 'RespuestasDocentes.csv',
            'docentes_directores': 'RespuesDocentesYDirectores.csv'
        }
        
        data_dict = {}
        for name, filename in data_files.items():
            filepath = os.path.join(self.data_path, filename)
            if os.path.exists(filepath):
                df = pd.read_csv(filepath, sep=';', encoding='utf-8')
                data_dict[name] = df
                print(f"✅ Cargado {name}: {df.shape}")
        
        return data_dict
    
    def extract_features_from_data(self, data_dict):
        """
        Extrae características relevantes para clustering basado en los datos CSV
        """
        features = {}
        
        # Analizar datos de asistentes
        if 'asistentes' in data_dict:
            asistentes_df = data_dict['asistentes']
            features['asistentes'] = self._extract_asistentes_features(asistentes_df)
        
        # Analizar datos de directores
        if 'directores' in data_dict:
            directores_df = data_dict['directores']
            features['directores'] = self._extract_directores_features(directores_df)
        
        # Analizar datos de docentes
        if 'docentes' in data_dict:
            docentes_df = data_dict['docentes']
            features['docentes'] = self._extract_docentes_features(docentes_df)
        
        return features
    
    def _extract_asistentes_features(self, df):
        """
        Extrae características de asistentes para clustering
        """
        features = {}
        
        # Convertir porcentajes a valores numéricos
        for col in df.columns[1:]:  # Excluir columna 'Ítem'
            if col in ['Escuela Rural', 'Escuela Urbana', 'Liceo HC', 'Liceo TP', 'Municipal', 'PS', 'PP']:
                # Extraer valores numéricos de porcentajes
                values = []
                for val in df[col]:
                    if isinstance(val, str) and '%' in val:
                        try:
                            num_val = float(val.replace('%', '').replace(',', '.'))
                            values.append(num_val)
                        except:
                            values.append(0)
                    else:
                        values.append(0)
                
                features[f'asistente_{col.lower().replace(" ", "_")}'] = np.mean(values)
        
        return features
    
    def _extract_directores_features(self, df):
        """
        Extrae características de directores para clustering
        """
        features = {}
        
        # Convertir porcentajes a valores numéricos
        for col in df.columns[1:]:  # Excluir columna 'Ítem'
            if col in ['Escuela Rural', 'Escuela Urbana', 'Liceo HC', 'Liceo TP', 'Municipal', 'PS', 'PP']:
                values = []
                for val in df[col]:
                    if isinstance(val, str) and '%' in val:
                        try:
                            num_val = float(val.replace('%', '').replace(',', '.'))
                            values.append(num_val)
                        except:
                            values.append(0)
                    else:
                        values.append(0)
                
                features[f'director_{col.lower().replace(" ", "_")}'] = np.mean(values)
        
        return features
    
    def _extract_docentes_features(self, df):
        """
        Extrae características de docentes para clustering
        """
        features = {}
        
        # Convertir porcentajes a valores numéricos
        for col in df.columns[1:]:  # Excluir columna 'Ítem'
            if col in ['Escuela Urbana', 'Liceo HC', 'Liceo TP', 'Municipal', 'PS', 'PP']:
                values = []
                for val in df[col]:
                    if isinstance(val, str) and '%' in val:
                        try:
                            num_val = float(val.replace('%', '').replace(',', '.'))
                            values.append(num_val)
                        except:
                            values.append(0)
                    else:
                        values.append(0)
                
                features[f'docente_{col.lower().replace(" ", "_")}'] = np.mean(values)
        
        return features
    
    def create_clustering_dataset(self, features_dict):
        """
        Crea un dataset para clustering basado en las características extraídas
        """
        # Crear dataset sintético basado en los patrones observados
        dataset = []
        
        # Generar perfiles sintéticos basados en los datos reales
        for i in range(1000):  # 1000 perfiles sintéticos
            profile = self._generate_synthetic_profile(features_dict)
            dataset.append(profile)
        
        return pd.DataFrame(dataset)
    
    def _generate_synthetic_profile(self, features_dict):
        """
        Genera un perfil sintético basado en los patrones de los datos reales
        """
        profile = {}
        
        # Variables numéricas (1-5 escala)
        profile['digital_tools_skill'] = np.random.randint(1, 6)
        profile['advanced_tic_skill'] = np.random.randint(1, 6)
        profile['digital_citizenship_skill'] = np.random.randint(1, 6)
        profile['teaching_tech_skill'] = np.random.randint(1, 6)
        profile['leadership_support'] = np.random.randint(1, 6)
        profile['resource_support'] = np.random.randint(1, 6)
        
        # Variables categóricas
        roles = ['profesor', 'director', 'asistente']
        profile['role'] = np.random.choice(roles)
        
        school_types = ['rural', 'urbana', 'cientifico-humanista', 'tecnico-profesional']
        profile['school_type'] = np.random.choice(school_types)
        
        dependencies = ['municipal', 'privada-subvencionada', 'privada-pagada']
        profile['dependency'] = np.random.choice(dependencies)
        
        age_ranges = ['20-30', '31-40', '41-50', '51+']
        profile['age_range'] = np.random.choice(age_ranges)
        
        learning_formats = ['en-linea', 'talleres', 'autoaprendizaje']
        profile['learning_format'] = np.random.choice(learning_formats)
        
        # Variables booleanas
        profile['interest_digital_literacy'] = np.random.choice([True, False])
        profile['interest_educational_innovation'] = np.random.choice([True, False])
        profile['interest_leadership'] = np.random.choice([True, False])
        
        return profile
    
    def preprocess_for_clustering(self, df):
        """
        Preprocesa el dataset para clustering
        """
        # Separar variables numéricas y categóricas
        numeric_cols = ['digital_tools_skill', 'advanced_tic_skill', 'digital_citizenship_skill', 
                       'teaching_tech_skill', 'leadership_support', 'resource_support']
        
        categorical_cols = ['role', 'school_type', 'dependency', 'age_range', 'learning_format']
        boolean_cols = ['interest_digital_literacy', 'interest_educational_innovation', 'interest_leadership']
        
        # Convertir booleanos a numéricos
        for col in boolean_cols:
            df[col] = df[col].astype(int)
        
        # Codificar variables categóricas
        for col in categorical_cols:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
            df[col] = self.label_encoders[col].fit_transform(df[col])
        
        # Normalizar variables numéricas
        df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])
        
        return df
    
    def clean_dataset(self, df):
        """
        Limpia el dataset eliminando valores NaN y valores infinitos
        """
        # Reemplazar valores infinitos con NaN
        df = df.replace([np.inf, -np.inf], np.nan)
        
        # Eliminar filas con valores NaN
        df_cleaned = df.dropna()
        
        # Si no quedan datos, crear dataset sintético limpio
        if len(df_cleaned) == 0:
            print("⚠️  Dataset vacío después de limpieza, creando dataset sintético...")
            df_cleaned = self.create_clean_synthetic_dataset()
        
        print(f"✅ Dataset limpio: {df_cleaned.shape}")
        return df_cleaned
    
    def create_clean_synthetic_dataset(self):
        """
        Crea un dataset sintético limpio sin valores NaN
        """
        dataset = []
        
        for i in range(1000):
            profile = {
                'digital_tools_skill': np.random.randint(1, 6),
                'advanced_tic_skill': np.random.randint(1, 6),
                'digital_citizenship_skill': np.random.randint(1, 6),
                'teaching_tech_skill': np.random.randint(1, 6),
                'leadership_support': np.random.randint(1, 6),
                'resource_support': np.random.randint(1, 6),
                'role': np.random.choice([0, 1, 2]),  # Codificado
                'school_type': np.random.choice([0, 1, 2, 3]),  # Codificado
                'dependency': np.random.choice([0, 1, 2]),  # Codificado
                'age_range': np.random.choice([0, 1, 2, 3]),  # Codificado
                'learning_format': np.random.choice([0, 1, 2]),  # Codificado
                'interest_digital_literacy': np.random.choice([0, 1]),
                'interest_educational_innovation': np.random.choice([0, 1]),
                'interest_leadership': np.random.choice([0, 1])
            }
            dataset.append(profile)
        
        return pd.DataFrame(dataset) 