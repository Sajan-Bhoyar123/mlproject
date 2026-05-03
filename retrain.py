"""
Retrain script - regenerates artifacts/model.pkl and artifacts/preprocessor.pkl
using the current scikit-learn version so they are compatible.
"""
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

print("=" * 50)
print("Step 1: Data Ingestion")
print("=" * 50)
obj = DataIngestion()
train_data, test_data = obj.initiate_data_ingestion()
print(f"Train: {train_data}")
print(f"Test:  {test_data}")

print("\n" + "=" * 50)
print("Step 2: Data Transformation")
print("=" * 50)
data_transformation = DataTransformation()
train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data, test_data)
print(f"Preprocessor saved: {preprocessor_path}")

print("\n" + "=" * 50)
print("Step 3: Model Training")
print("=" * 50)
model_trainer = ModelTrainer()
r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
print(f"\n✅ Training complete! Best model R2 score: {r2_score:.4f}")
print("New model.pkl and preprocessor.pkl saved to artifacts/")
