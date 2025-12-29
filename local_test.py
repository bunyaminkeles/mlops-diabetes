import requests
import json

# Lokal sunucu adresi
BASE_URL = "http://127.0.0.1:8000"

print("--- 🏠 LOKAL API TESTİ BAŞLIYOR ---")

# 1. GET İsteği (Ana Sayfa Kontrolü)
try:
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        print("✅ Sunucu Ayakta:", response.json())
    else:
        print("❌ Sunucu Hatası:", response.status_code)
except Exception as e:
    print(f"❌ Bağlantı Hatası: {e}")
    print("İPUCU: 'uvicorn main:app --reload' komutunu çalıştırdın mı?")
    exit()

# 2. POST İsteği (Diyabet Tahmini)
# Örnek: Şeker hastası olma ihtimali yüksek bir veri
patient_data = {
    "preg": 1,
    "glucose": 90,
    "bp": 72,
    "skin": 35,
    "insulin": 0,
    "bmi": 33.6,
    "pedigree": 0.627,
    "age": 50
}

print(f"\n📤 Veri Gönderiliyor: {patient_data}")

try:
    response = requests.post(f"{BASE_URL}/predict", json=patient_data)
    
    if response.status_code == 200:
        result = response.json()
        print("\n📊 SONUÇ GELDİ:")
        print(f"   Durum: {result['prediction']}")
        print(f"   İhtimal: %{result['probability']}")
        print(f"   Ham Veri: {result}")
    else:
        print("❌ Hata:", response.text)

except Exception as e:
    print(f"❌ İstek Hatası: {e}")