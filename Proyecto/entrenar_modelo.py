import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Leer dataset de características
df = pd.read_csv("features_eeg.csv")

# Variables de entrada
X = df.drop(columns=["clase", "archivo", "inicio_s", "fin_s"])

# Etiquetas
y = df["clase"]

# División entrenamiento/prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Modelo
modelo = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

# Entrenamiento
modelo.fit(X_train, y_train)

# Predicción
y_pred = modelo.predict(X_test)

# Resultados
accuracy = accuracy_score(y_test, y_pred)

print("\n==========================")
print("RESULTADOS DEL MODELO")
print("==========================")
print(f"Accuracy: {accuracy:.4f}")

print("\nReporte:")
print(classification_report(y_test, y_pred))

# Guardar modelo
joblib.dump(modelo, "modelo_estres_eeg.pkl")

print("\nModelo guardado como:")
print("modelo_estres_eeg.pkl")