from src.preprocess import load_data, preprocess
from src.train import train_model, save_model
from src.evaluate import evaluate

# Step 1: Load Data
df = load_data("C:\\Users\\Sai teja\\Desktop\\Projects andAssignments\\EdgeDetection\\CICIOT23\\train\\train.csv")
# Step 2: Preprocess
X, y, scaler, le = preprocess(df)

# Step 3: Train
model, X_test, y_test = train_model(X, y)

# Step 4: Evaluate
results = evaluate(model, X_test, y_test)

print("\nModel Performance:")
for k, v in results.items():
    print(f"{k}: {v:.4f}")

# Step 5: Save model
save_model(model)