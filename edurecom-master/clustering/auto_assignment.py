import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import os

class AutoAssignment:
    """
    Sistema de asignación automática de grupos usando clustering
    """
    
    def __init__(self, model_path='clustering_model.pkl'):
        self.model_path = model_path
        self.clustering_model = None
        self.scaler = StandardScaler()
        self.feature_engineer = None
        self.cluster_mapping = None
        self.is_trained = False
        
    def train_model(self, clustering_engine, feature_engineer, cluster_mapping):
        """
        Entrena el modelo de asignación automática
        """
        self.clustering_model = clustering_engine.kmeans
        self.feature_engineer = feature_engineer
        self.cluster_mapping = cluster_mapping
        self.is_trained = True
        
        # Guardar modelo
        self.save_model()
        
        print("✅ Modelo de asignación automática entrenado y guardado")
        
    def save_model(self):
        """
        Guarda el modelo entrenado
        """
        model_data = {
            'clustering_model': self.clustering_model,
            'scaler': self.scaler,
            'feature_engineer': self.feature_engineer,
            'cluster_mapping': self.cluster_mapping,
            'is_trained': self.is_trained
        }
        
        joblib.dump(model_data, self.model_path)
        print(f"💾 Modelo guardado en: {self.model_path}")
        
    def load_model(self):
        """
        Carga el modelo entrenado
        """
        if os.path.exists(self.model_path):
            model_data = joblib.load(self.model_path)
            
            self.clustering_model = model_data['clustering_model']
            self.scaler = model_data['scaler']
            self.feature_engineer = model_data['feature_engineer']
            self.cluster_mapping = model_data['cluster_mapping']
            self.is_trained = model_data['is_trained']
            
            print(f"📂 Modelo cargado desde: {self.model_path}")
            return True
        else:
            print(f"❌ No se encontró el modelo en: {self.model_path}")
            return False
    
    def prepare_user_profile(self, user_profile):
        """
        Prepara el perfil del usuario para clustering
        """
        try:
            if not user_profile:
                print("❌ Error: Perfil de usuario es None")
                return None
            
            # Crear DataFrame con el perfil del usuario, manejando valores None
            profile_data = {
                'digital_tools_skill': [user_profile.digital_tools_skill or 3],
                'advanced_tic_skill': [user_profile.advanced_tic_skill or 3],
                'digital_citizenship_skill': [user_profile.digital_citizenship_skill or 3],
                'teaching_tech_skill': [user_profile.teaching_tech_skill or 3],
                'leadership_support': [user_profile.leadership_support or 3],
                'resource_support': [user_profile.resource_support or 3],
                'role': [user_profile.role or 'profesor'],
                'school_type': [user_profile.school_type or 'urbana'],
                'dependency': [user_profile.dependency or 'municipal'],
                'age_range': [user_profile.age_range or '31-40'],
                'learning_format': [user_profile.learning_format or 'en-linea'],
                'interest_digital_literacy': [getattr(user_profile, 'interest_digital_literacy', False) or False],
                'interest_educational_innovation': [getattr(user_profile, 'interest_educational_innovation', False) or False],
                'interest_leadership': [getattr(user_profile, 'interest_leadership', False) or False]
            }
            
            df = pd.DataFrame(profile_data)
            print(f"📊 Perfil preparado: {df.shape}")
            
            # Aplicar preprocesamiento
            if self.feature_engineer:
                try:
                    df_processed = self.feature_engineer.create_clustering_features(df)
                    print("✅ Características de clustering creadas")
                except Exception as e:
                    print(f"❌ Error creando características: {e}")
                    # Fallback a preprocesamiento básico
                    df_processed = self._basic_preprocessing(df)
            else:
                # Preprocesamiento básico si no hay feature engineer
                df_processed = self._basic_preprocessing(df)
            
            return df_processed
            
        except Exception as e:
            print(f"❌ Error en prepare_user_profile: {e}")
            return None
    
    def _basic_preprocessing(self, df):
        """
        Preprocesamiento básico cuando no hay feature engineer
        """
        try:
            numeric_cols = ['digital_tools_skill', 'advanced_tic_skill', 'digital_citizenship_skill', 
                           'teaching_tech_skill', 'leadership_support', 'resource_support']
            boolean_cols = ['interest_digital_literacy', 'interest_educational_innovation', 'interest_leadership']
            
            # Convertir booleanos a numéricos
            for col in boolean_cols:
                if col in df.columns:
                    df[col] = df[col].astype(int)
            
            # Normalizar variables numéricas
            if numeric_cols:
                df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])
                df_processed = df[numeric_cols + boolean_cols]
            else:
                df_processed = df
            
            print("✅ Preprocesamiento básico completado")
            return df_processed
            
        except Exception as e:
            print(f"❌ Error en preprocesamiento básico: {e}")
            return df
    
    def assign_group(self, user_profile):
        """
        Asigna automáticamente un grupo de formación al usuario
        """
        try:
            if not user_profile:
                print("❌ Error: Perfil de usuario es None")
                return self._manual_assignment(user_profile)
            
            if not self.is_trained:
                if not self.load_model():
                    print("❌ No se pudo cargar el modelo. Usando asignación manual.")
                    return self._manual_assignment(user_profile)
            
            # Preparar perfil del usuario
            try:
                profile_df = self.prepare_user_profile(user_profile)
                if profile_df is None or profile_df.empty:
                    print("❌ Error al preparar perfil del usuario")
                    return self._manual_assignment(user_profile)
            except Exception as e:
                print(f"❌ Error preparando perfil: {e}")
                return self._manual_assignment(user_profile)
            
            # Predecir cluster
            try:
                cluster_prediction = self.clustering_model.predict(profile_df)
                cluster_id = cluster_prediction[0]
                print(f"🔍 Cluster predicho: {cluster_id}")
            except Exception as e:
                print(f"❌ Error prediciendo cluster: {e}")
                return self._manual_assignment(user_profile)
            
            # Mapear cluster a grupo de formación
            if self.cluster_mapping and cluster_id in self.cluster_mapping:
                assigned_group = self.cluster_mapping[cluster_id]
                print(f"🤖 Asignación automática: Cluster {cluster_id} → {assigned_group}")
            else:
                # Fallback a asignación manual
                print(f"⚠️  Cluster {cluster_id} no encontrado en mapeo, usando manual")
                assigned_group = self._manual_assignment(user_profile)
            
            return assigned_group
            
        except Exception as e:
            print(f"❌ Error general en asignación automática: {e}")
            print("🔄 Usando asignación manual como fallback")
            return self._manual_assignment(user_profile)
    
    def _manual_assignment(self, user_profile):
        """
        Asignación manual basada en el algoritmo original
        """
        # Calcular promedio de habilidades digitales con manejo de None
        digital_skills = [
            user_profile.digital_tools_skill,
            user_profile.advanced_tic_skill,
            user_profile.digital_citizenship_skill,
            user_profile.teaching_tech_skill
        ]
        # Filtrar valores None y usar valor por defecto de 3 si todos son None
        valid_digital_skills = [skill for skill in digital_skills if skill is not None]
        if not valid_digital_skills:
            avg_digital_skills = 3  # Valor por defecto
        else:
            avg_digital_skills = sum(valid_digital_skills) / len(valid_digital_skills)
        
        # Calcular promedio de apoyo institucional con manejo de None
        institutional_support = [
            user_profile.leadership_support,
            user_profile.resource_support
        ]
        # Filtrar valores None y usar valor por defecto de 3 si todos son None
        valid_institutional_support = [support for support in institutional_support if support is not None]
        if not valid_institutional_support:
            avg_institutional_support = 3  # Valor por defecto
        else:
            avg_institutional_support = sum(valid_institutional_support) / len(valid_institutional_support)
        
        # Lógica de asignación
        if avg_digital_skills < 3:
            return "Alfabetización Digital Básica"
        elif avg_institutional_support < 3 or user_profile.interest_leadership:
            return "Fortalecimiento Institucional"
        elif user_profile.interest_educational_innovation:
            return "Innovación Educativa"
        else:
            return "Habilidades Digitales Avanzadas"
    
    def get_assignment_confidence(self, user_profile):
        """
        Calcula la confianza de la asignación automática
        """
        if not self.is_trained:
            return 0.0
        
        try:
            profile_df = self.prepare_user_profile(user_profile)
            
            # Calcular distancia al centroide más cercano
            cluster_prediction = self.clustering_model.predict(profile_df)
            cluster_id = cluster_prediction[0]
            
            # Distancia al centroide
            centroid = self.clustering_model.cluster_centers_[cluster_id]
            distance = np.linalg.norm(profile_df.values[0] - centroid)
            
            # Convertir distancia a confianza (menor distancia = mayor confianza)
            max_distance = np.max([np.linalg.norm(centroid) for centroid in self.clustering_model.cluster_centers_])
            confidence = 1 - (distance / max_distance)
            
            return max(0.0, min(1.0, confidence))
            
        except Exception as e:
            print(f"❌ Error calculando confianza: {e}")
            return 0.5  # Confianza media por defecto
    
    def compare_assignments(self, user_profile):
        """
        Compara asignación automática vs manual
        """
        auto_group = self.assign_group(user_profile)
        manual_group = self._manual_assignment(user_profile)
        confidence = self.get_assignment_confidence(user_profile)
        
        comparison = {
            'auto_assignment': auto_group,
            'manual_assignment': manual_group,
            'confidence': confidence,
            'agreement': auto_group == manual_group
        }
        
        print(f"📊 Comparación de asignaciones:")
        print(f"   Automática: {auto_group}")
        print(f"   Manual: {manual_group}")
        print(f"   Confianza: {confidence:.2f}")
        print(f"   Acuerdo: {'✅' if comparison['agreement'] else '❌'}")
        
        return comparison
    
    def get_model_info(self):
        """
        Obtiene información del modelo
        """
        if not self.is_trained:
            return {"status": "No entrenado"}
        
        info = {
            "status": "Entrenado",
            "model_path": self.model_path,
            "n_clusters": self.clustering_model.n_clusters if self.clustering_model else None,
            "cluster_mapping": self.cluster_mapping
        }
        
        return info 