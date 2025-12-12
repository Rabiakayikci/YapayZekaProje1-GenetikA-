
import numpy as np
import genetik_operators as ga
import evrim_motoru as motor

def main():
    print("="*50)
    print("🧬 GENETİK ALGORİTMA BAŞLATILIYOR 🧬")
    print("="*50)


    try:

        pop_sayisi = int(input("Popülasyon Sayısı (Örn: 20): "))
        nesil_sayisi = int(input("Nesil Sayısı (Örn: 50): "))
        secim_turu = input("Seçim Türü (rulet / rank): ").lower()
        mut_ihtimal = float(input("Mutasyon İhtimali (0.1): "))
        mut_buyukluk = float(input("Mutasyon Büyüklüğü (2.0): "))
    except ValueError:
        print("Hata: Lütfen sayısal değer giriniz.")
        return

    print(f"
✅ {pop_sayisi} birey oluşturuluyor...")


    populasyon = ga.populasyon_olustur(pop_sayisi)
    populasyon = np.array(populasyon)#indeklseme hatası almamak için numpy dizisine çeviriyoruz

    print("🚀 Evrim Motoru Ateşleniyor...")



    motor.evrimsel_algoritma(
        populasyon=populasyon,         # Bizim oluşturduğumuz popülasyon
        nesil_sayisi=nesil_sayisi,
        caprazlama_turu="tek",         #'tek nokta' sabit
        secim_turu=secim_turu,
        mutasyon_ihtimali=mut_ihtimal,
        mutasyon_buyuklugu=mut_buyukluk
    )

if __name__ == "__main__":  #kodunun hem tek başına çalışabilen bir program hem de başka programlar tarafından kullanılabilen bir kütüphane olmasını sağlar.
    main()

    