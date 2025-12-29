import joblib
import os

# Test: Model dosyası yerinde mi?
def test_model_exists():
    assert os.path.exists("diabetes_model.pkl"), "HATA: Model dosyası bulunamadı!"

# Test: Model gerçekten tahmin yapıyor mu?
def test_prediction():
    # Modeli yükle
    model = joblib.load("diabetes_model.pkl")
    
    # Örnek bir veri (Sağlıklı insan verisi)
    # [Hamilelik, Glikoz, Tansiyon, Deri, İnsülin, BMI, Soyağacı, Yaş]
    sample_data = [[1, 85, 66, 29, 0, 26.6, 0.351, 31]]
    
    # Tahmin al
    prediction = model.predict(sample_data)
    
    # Tahmin ya 0 ya 1 olmalı. Başka bir şey gelirse model bozuktur.
    assert prediction[0] in [0, 1], "HATA: Model geçersiz bir sınıf döndürdü!"
    
    print("✅ Testler Başarılı! Model sağlam.")

if __name__ == "__main__":
    test_model_exists()
    test_prediction()