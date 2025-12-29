# 1. Hafif Python
FROM python:3.9-slim

# 2. Klasör ayarla
WORKDIR /app

# 3. Kütüphaneleri yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kodları ve MODELİ kopyala 
# (Model küçük olduğu için direkt kopyalıyoruz, LFS'e gerek yok!)
COPY . .

# 5. Başlat
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]