from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Modeli Yükle (Diskten hafızaya al)
# Dosya çok küçük olduğu için saniyenin onda birinde yüklenir.
model = joblib.load("diabetes_model.pkl")

app = FastAPI(title="Diabet Tahmin API")

# 2. Veri Formatını Tanımla
# Kullanıcıdan bu 8 bilgiyi istiyoruz
class PatientData(BaseModel):
    preg: int          # Hamilelik Sayısı
    glucose: int       # Glikoz
    bp: int            # Kan Basıncı
    skin: int          # Deri Kalınlığı
    insulin: int       # İnsülin
    bmi: float         # Vücut Kitle İndeksi
    pedigree: float    # Soyağacı Fonksiyonu
    age: int           # Yaş

@app.get("/")
def home():
    return {"message": "Diabet Testi API Çalışıyor! /predict endpointini kullanın."}

@app.post("/predict")
def predict_diabetes(data: PatientData):
    # Gelen veriyi modelin anlayacağı formata (liste) çevir
    features = [[
        data.preg, 
        data.glucose, 
        data.bp, 
        data.skin, 
        data.insulin, 
        data.bmi, 
        data.pedigree, 
        data.age
    ]]
    
    # Tahmin yap
    prediction = model.predict(features)[0]      # 0 veya 1 döner
    probability = model.predict_proba(features)[0][1] # Diyabet olma ihtimali (Örn: 0.72)

    # Sonucu yorumla
    result = "DIABETES (Şeker Hastası)" if prediction == 1 else "HEALTHY (Sağlıklı)"
    
    return {
        "prediction": result,
        "probability": round(probability * 100, 2), # Yüzdelik dilim
        "is_diabetic": bool(prediction)
    }