import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

print("1. Veri Seti Yükleniyor...")
# Pima Indians Diabetes Dataset (İnternetten direkt çekiyoruz)
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ['preg', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
df = pd.read_csv(url, names=column_names)

print(f"   Veri boyutu: {df.shape}")

# 2. Veriyi Hazırla (X ve y)
X = df.drop('label', axis=1)  # Girdiler
y = df['label']               # Çıktı (0: Sağlıklı, 1: Diyabet)

# Eğitim ve Test olarak ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Modeli Eğit (Random Forest)
print("2. Model Eğitiliyor...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Test Et
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"   Model Doğruluğu (Accuracy): %{accuracy * 100:.2f}")

# 5. Modeli Kaydet
print("3. Model Kaydediliyor...")
joblib.dump(model, "diabetes_model.pkl")
print("✅ BAŞARILI! Model 'diabetes_model.pkl' olarak kaydedildi.")