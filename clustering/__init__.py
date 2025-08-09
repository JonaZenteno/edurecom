# Clustering module for CourseConnect
from .data_preprocessing import DataPreprocessor
from .feature_engineering import FeatureEngineer
from .clustering_engine import ClusteringEngine
from .auto_assignment import AutoAssignment

__all__ = [
    'DataPreprocessor',
    'FeatureEngineer', 
    'ClusteringEngine',
    'AutoAssignment'
] 