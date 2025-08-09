import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

class ClusteringEngine:
    """
    Motor de clustering para segmentar usuarios educativos
    """
    
    def __init__(self, n_clusters=4, random_state=42):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.kmeans = None
        self.cluster_centers = None
        self.cluster_labels = None
        self.silhouette_score = None
        self.calinski_score = None
        
    def find_optimal_k(self, X, k_range=(2, 10)):
        """
        Encuentra el número óptimo de clusters usando el método del codo y Silhouette
        """
        inertias = []
        silhouette_scores = []
        calinski_scores = []
        
        print("🔍 Buscando número óptimo de clusters...")
        
        for k in range(k_range[0], k_range[1] + 1):
            # Entrenar K-Means
            kmeans = KMeans(n_clusters=k, random_state=self.random_state, n_init=10)
            kmeans.fit(X)
            
            # Calcular métricas
            inertias.append(kmeans.inertia_)
            silhouette_scores.append(silhouette_score(X, kmeans.labels_))
            calinski_scores.append(calinski_harabasz_score(X, kmeans.labels_))
            
            print(f"   K={k}: Inertia={kmeans.inertia_:.2f}, "
                  f"Silhouette={silhouette_scores[-1]:.3f}, "
                  f"Calinski={calinski_scores[-1]:.2f}")
        
        # Encontrar el codo (cambio más pronunciado en la inercia)
        inertia_changes = np.diff(inertias)
        elbow_k = np.argmin(inertia_changes) + k_range[0]
        
        # Encontrar mejor Silhouette
        best_silhouette_k = np.argmax(silhouette_scores) + k_range[0]
        
        # Encontrar mejor Calinski
        best_calinski_k = np.argmax(calinski_scores) + k_range[0]
        
        print(f"\n📊 Resultados:")
        print(f"   Codo (Inertia): K={elbow_k}")
        print(f"   Mejor Silhouette: K={best_silhouette_k}")
        print(f"   Mejor Calinski: K={best_calinski_k}")
        
        # Para nuestro caso, queremos 4 clusters específicos
        optimal_k = 4
        print(f"   🎯 Usando K={optimal_k} (grupos de formación específicos)")
        
        return optimal_k
    
    def train_clustering_model(self, X, n_clusters=None):
        """
        Entrena el modelo de clustering
        """
        if n_clusters is None:
            n_clusters = self.find_optimal_k(X)
        
        print(f"\n🚀 Entrenando modelo K-Means++ con {n_clusters} clusters...")
        
        # Entrenar K-Means++
        self.kmeans = KMeans(
            n_clusters=n_clusters,
            random_state=self.random_state,
            n_init=10,
            init='k-means++'
        )
        
        self.kmeans.fit(X)
        self.cluster_centers = self.kmeans.cluster_centers_
        self.cluster_labels = self.kmeans.labels_
        
        # Calcular métricas de calidad
        self.silhouette_score = silhouette_score(X, self.cluster_labels)
        self.calinski_score = calinski_harabasz_score(X, self.cluster_labels)
        
        print(f"✅ Modelo entrenado exitosamente")
        print(f"   Silhouette Score: {self.silhouette_score:.3f}")
        print(f"   Calinski-Harabasz Score: {self.calinski_score:.2f}")
        
        return self.kmeans
    
    def predict_cluster(self, X):
        """
        Predice el cluster para nuevos datos
        """
        if self.kmeans is None:
            raise ValueError("El modelo debe ser entrenado primero")
        
        return self.kmeans.predict(X)
    
    def analyze_clusters(self, X, feature_names=None):
        """
        Analiza las características de cada cluster
        """
        if self.kmeans is None:
            raise ValueError("El modelo debe ser entrenado primero")
        
        # Crear DataFrame con datos y clusters
        df_with_clusters = pd.DataFrame(X)
        if feature_names:
            df_with_clusters.columns = feature_names
        df_with_clusters['cluster'] = self.cluster_labels
        
        print(f"\n📊 Análisis de Clusters:")
        print(f"   Total de muestras: {len(df_with_clusters)}")
        
        # Distribución de clusters
        cluster_counts = Counter(self.cluster_labels)
        print(f"   Distribución de clusters:")
        for cluster_id, count in sorted(cluster_counts.items()):
            percentage = (count / len(df_with_clusters)) * 100
            print(f"     Cluster {cluster_id}: {count} muestras ({percentage:.1f}%)")
        
        # Características promedio por cluster
        print(f"\n📈 Características promedio por cluster:")
        cluster_means = df_with_clusters.groupby('cluster').mean()
        
        for cluster_id in range(self.n_clusters):
            print(f"\n   Cluster {cluster_id}:")
            cluster_data = cluster_means.loc[cluster_id]
            
            # Mostrar características más importantes
            if 'avg_digital_skills' in cluster_data.index:
                print(f"     Habilidades digitales promedio: {cluster_data['avg_digital_skills']:.2f}")
            if 'avg_institutional_support' in cluster_data.index:
                print(f"     Apoyo institucional promedio: {cluster_data['avg_institutional_support']:.2f}")
            if 'innovation_profile' in cluster_data.index:
                print(f"     Perfil de innovación: {cluster_data['innovation_profile']:.2f}")
            if 'leadership_profile' in cluster_data.index:
                print(f"     Perfil de liderazgo: {cluster_data['leadership_profile']:.2f}")
        
        return df_with_clusters
    
    def map_clusters_to_groups(self, cluster_analysis):
        """
        Mapea los clusters a los grupos de formación específicos
        """
        # Obtener características promedio por cluster
        cluster_means = cluster_analysis.groupby('cluster').mean()
        
        # Definir mapeo basado en características
        cluster_mapping = {}
        
        for cluster_id in range(self.n_clusters):
            cluster_data = cluster_means.loc[cluster_id]
            
            # Determinar grupo basado en características
            avg_digital_skills = cluster_data.get('avg_digital_skills', 0)
            avg_institutional_support = cluster_data.get('avg_institutional_support', 0)
            innovation_profile = cluster_data.get('innovation_profile', 0)
            leadership_profile = cluster_data.get('leadership_profile', 0)
            
            # Lógica de asignación basada en el algoritmo original
            if avg_digital_skills < 3:
                group = "Alfabetización Digital Básica"
            elif avg_institutional_support < 3 or leadership_profile > 2:
                group = "Fortalecimiento Institucional"
            elif innovation_profile > 2:
                group = "Innovación Educativa"
            else:
                group = "Habilidades Digitales Avanzadas"
            
            cluster_mapping[cluster_id] = group
            
            print(f"   Cluster {cluster_id} → {group}")
        
        return cluster_mapping
    
    def visualize_clusters(self, X, feature_names=None, save_path=None):
        """
        Visualiza los clusters usando las primeras 2 características
        """
        if self.kmeans is None:
            raise ValueError("El modelo debe ser entrenado primero")
        
        # Usar las primeras 2 características para visualización
        if X.shape[1] >= 2:
            X_vis = X[:, :2]
            feature_labels = feature_names[:2] if feature_names else ['Feature 1', 'Feature 2']
        else:
            # Si solo hay 1 característica, crear una segunda artificial
            X_vis = np.column_stack([X[:, 0], np.zeros_like(X[:, 0])])
            feature_labels = [feature_names[0] if feature_names else 'Feature 1', 'Feature 2']
        
        # Crear gráfico
        plt.figure(figsize=(10, 8))
        
        # Scatter plot por cluster
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
        for i in range(self.n_clusters):
            mask = self.cluster_labels == i
            plt.scatter(X_vis[mask, 0], X_vis[mask, 1], 
                       c=colors[i % len(colors)], 
                       label=f'Cluster {i}', 
                       alpha=0.7, s=50)
        
        # Centroides
        centers_vis = self.cluster_centers[:, :2]
        plt.scatter(centers_vis[:, 0], centers_vis[:, 1], 
                   c='black', marker='x', s=200, linewidths=3, 
                   label='Centroides')
        
        plt.xlabel(feature_labels[0])
        plt.ylabel(feature_labels[1])
        plt.title('Clustering de Usuarios Educativos')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"📊 Gráfico guardado en: {save_path}")
        
        plt.show()
        
    def get_cluster_centers(self):
        """
        Obtiene los centroides de los clusters
        """
        return self.cluster_centers
    
    def get_cluster_labels(self):
        """
        Obtiene las etiquetas de los clusters
        """
        return self.cluster_labels
    
    def get_model_metrics(self):
        """
        Obtiene las métricas del modelo
        """
        return {
            'silhouette_score': self.silhouette_score,
            'calinski_score': self.calinski_score,
            'n_clusters': self.n_clusters
        } 