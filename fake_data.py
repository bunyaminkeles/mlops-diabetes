import random
import csv
import os

# Dosya adı
FILE_NAME = "data.csv"

# Rastgele ama "mantıklı" veri üretme fonksiyonu
def generate_patient():
    preg = random.randint(0, 10)        # Hamilelik
    glucose = random.randint(70, 190)   # Şeker
    bp = random.randint(50, 100)        # Tansiyon
    skin = random.randint(15, 50)       # Deri
    insulin = random.randint(0, 300)    # İnsülin
    bmi = round(random.uniform(18.0, 45.0), 1) # Vücut Kitle Endeksi
    pedigree = round(random.uniform(0.1, 2.5), 3) # Soyağacı
    age = random.randint(21, 80)        # Yaş
    
    # Basit bir mantıkla "Hasta mı?" sonucunu uyduralım
    # Şekeri ve BMI'ı yüksekse hasta olma ihtimali artsın
    if glucose > 140 and bmi > 30:
        outcome = 1
    elif random.random() > 0.8: # %20 ihtimalle rastgele hasta olsun
        outcome = 1
    else:
        outcome = 0
        
    return [preg, glucose, bp, skin, insulin, bmi, pedigree, age, outcome]

def append_to_csv():
    # Yeni bir hasta üret
    new_patient = generate_patient()
    
    # Dosyaya ekle (append mode: 'a')
    with open(FILE_NAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_patient)
        
    print(f"✅ Yeni sahte hasta eklendi: {new_patient}")

if __name__ == "__main__":
    # Eğer dosya yoksa önce oluşturmasın, hata versin (önceki adımları korumak için)
    if os.path.exists(FILE_NAME):
        append_to_csv()
    else:
        print("❌ data.csv bulunamadı! Lütfen önce train.py'yi çalıştır.")