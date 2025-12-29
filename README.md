# 🩺 Diabet Tahmin API (MLOps Projesi)

Bu proje, uçtan uca (End-to-End) bir Makine Öğrenmesi dağıtım örneğidir. Random Forest algoritması kullanılarak eğitilen model, Dockerize edilerek Render üzerinde canlıya alınmıştır. Ayrıca GitHub Actions ile CI/CD süreçleri entegre edilmiştir.

## 🚀 Kullanılan Teknolojiler
* **Model:** Scikit-Learn (Random Forest)
* **API:** FastAPI
* **Container:** Docker
* **Deployment:** Render
* **Otomasyon:** GitHub Actions

## ⚙️ Nasıl Çalışır?
1. `train.py` dosyası veriyi çeker ve `diabetes_model.pkl` dosyasını oluşturur.
2. `main.py` API isteklerini karşılar.
3. Her `git push` işleminde GitHub Actions otomatik testleri çalıştırır.

## 💻 Lokal Kurulum
```bash
pip install -r requirements.txt
python train.py
uvicorn main:app --reload
