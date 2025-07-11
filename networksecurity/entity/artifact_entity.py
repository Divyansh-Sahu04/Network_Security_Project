"""
In a machine learning or data science project, the artifact file or artifacts folder refers to:
Files or objects produced at various stages of the ML pipeline — like data preprocessing, feature 
engineering, model training, evaluation, etc. — which are saved for later reuse, traceability, or deployment.
"""

from dataclasses import dataclass
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
