
import numpy as np
import random
import matplotlib.pyplot as plt
from genetik_operators import (
    birey_olustur,
    populasyon_olustur,
    tahmin_y,
    kontrol,
    uygunluk_hesapla,
    rulet_secim,
    rank_secim,
    tek_noktali_cap,
    mutasyon
)

def evrimsel_algoritma(populasyon, nesil_sayisi,
                        caprazlama_turu, secim_turu, mutasyon_ihtimali, mutasyon_buyuklugu):

    en_iyiler = []

    for nesil in range(nesil_sayisi):

        print(f"\n🔁 NESİL {nesil+1}")

        uygunluklar = np.array([uygunluk_hesapla(b) for b in populasyon])

        en_iyi_indeks = np.argmax(uygunluklar)
        elit_birey = populasyon[en_iyi_indeks].copy()
        elit_uygunluk = uygunluklar[en_iyi_indeks]

        en_iyiler.append(elit_uygunluk)

        print("Uygunluklar:", np.round(uygunluklar, 3))

        havuz = []
        for _ in range(len(populasyon)// 2):

            if secim_turu == "rulet":
                secilenler = rulet_secim(populasyon, uygunluklar, adet=2)
            elif secim_turu == "rank":
                secilenler = rank_secim(populasyon, uygunluklar, adet = 2)
            else:
                 raise ValueError("Hata: Seçim türü 'rulet' veya 'rank' olmalı.")

            havuz.append(secilenler)

        print("\n👥 Eşleme Havuzu:")

        for i, (p1, p2) in enumerate(havuz):
           print(f"  Ebeveyn {2*i+1}: {np.round(p1,1)}")
           print(f"  Ebeveyn {2*i+2}: {np.round(p2,1)}")


        yeni_bireyler = [elit_birey]

        while len(yeni_bireyler) < len(populasyon):
            p1, p2 = np.array(random.choice(havuz))
            if caprazlama_turu == "tek":
               c1, c2 = tek_noktali_cap(p1, p2)

            else:
               raise ValueError("Çaprazlama türü 'tek' olmalı.")

            c1 = mutasyon(c1, mutasyon_ihtimali, mutasyon_buyuklugu)
            c2 = mutasyon(c2, mutasyon_ihtimali, mutasyon_buyuklugu)
            yeni_bireyler.extend([c1, c2])

        populasyon = np.array(yeni_bireyler[:len(populasyon)])

        print("\n🏆 En iyi birey:", np.round(elit_birey, 1))
        print("Tahmini y:", tahmin_y(elit_birey).round(2))
        print("Uygunluk:", round(elit_uygunluk, 4))

        # Grafik çizgisini görmek için hedefi 100.000 yaptık
        if elit_uygunluk >= 1e5:
            print("✅ Hedefe ulaşıldı. Erken durdurma uygulandı.")
            break

    # Grafik Çizimi (Buradaki girinti hatası düzeltildi)
    plt.figure(figsize=(10,6))
    plt.plot(en_iyiler, marker='o', linestyle='-', color='b')
    plt.title("En İyi Uygunluk Değeri (Fitness) Değişimi")
    plt.xlabel("Nesil")
    plt.ylabel("Uygunluk (Fitness)")
    plt.grid(True)
    plt.show()
