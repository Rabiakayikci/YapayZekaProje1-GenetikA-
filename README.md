
# 🧬 Genetik Algoritma ile bir amaç fonksiyonunun verilen kısıtlara göre optimizasyonu

Bu projede, genetik algoritma kullanarak bir fonksiyondaki ağırlıkları optimize edeceğiz. Amaç, en iyi çıktıyı bulana kadar ağırlıklar üzerinde oynama yapmaktır.

---

## 📌 Amaç Fonksiyonu

Fonksiyon:

    y =  3x₁ + 2x₂ + x₁x₂ - 0.5x₂

- `x₁, x₂,`: Girdiler (verilmiştir)
- `y`: Çıktı

---

## 🎯 Girişler ve Beklenen Çıktı

- **Girdiler (X)**: Rastgele belirlenecek.
- **Hedef Çıktı (y)**: En iyi olanı bulmak istiyoruz.

---

## ⚠️ Kısıtlar

Genetik algoritmanın çözüm üretirken uyması gereken kurallar:

1. `x₁ + x₂ ≤ 100`
2. `x₁ ≥ 25`

🔹 Her ihlal için uygunluğa 3000 puan ceza uygulanır.

---

## 📁 Dosya Yapısı

| Dosya Adı               | Açıklama                                           |
|------------------------|----------------------------------------------------|
| `genetik_operators.py` | Tüm genetik işlemleri içerir (seçim, mutasyon vb.) |
| `main.py`              | Algoritmanın çalıştırıldığı ana dosyadır           |
| `README.md`            | Bu açıklama dosyasıdır                             |

---


## 📦 Fonksiyon Açıklamaları (`genetik_operators.py`)

### `def birey_olustur ()`
Random değerlere sahip bireyler oluşturulur.

---

### `def populasyon_olustur (populasyon_sayisi)`
İstenilen sayıda bireyin içinde bulunduğu bir birey topluluğu oluşturur.

---

### `def tahmin_y (birey)`
Bireylerin değerleri amaç fonksiyonuna koyulup bir y çıktısı elde edilir.

---

### `def kontrol (birey)`
Verilen kısıtlamalar dikkate alınarak bir hata sayısı hesaplanır, hata tespit edildikçe artar.

---

### `def uygunluk_hesapla (birey)`
Bireyin fonksiyona koyulması sonucu elde edilen y değerinden, hata sayısı.3000 çıkartılarak(eğer hata varsa) bir uygunluk değeri hesaplanır.

---

### `def rulet_secim (populasyon,uygunluklar, adet=2)`
Önce uygunluk değerlerinde negatif değer kontrolü yapılır eğer negatif değer varsa en küçük değere 1 eklenerek bu değer bütün uygunluk değerlerine eklenir(pozitif şekilde).
Sonra toplam uygunluklar hesaplanır, eğer değer 0 ise 0/0 olmaması için içinden rastgele değerler alınır.
Eğer 0 değilse her uygunluğun kendi değeri toplam uygunluk değerine bölünerek olasılıklar elde edilir.
Son olarak p olasılığında adet size'ı kadar populasyondan Random değerler belirler.
---

### `def rank_secim (populasyon, uygunluklar, adet =2)`
Uygunluklar küçükten büyüğe sıralanır ama sıralanan şey bu uygunluk değerlerinin adresleridir.
Payda kısmına popülasyon büyüklüğünün toplamı yazılır(1+2+3+.....+N), pay kısmına ise rankların sırası yazılır. Buna göre bir olasılık hesaplanır her bir uygunluk için.
Daha sonrasında uygunluk adresleri ile bu olasılıklar birleştirilir.(küçükten büyük değere göre sıralanmış adresleri sırayla gezer ve onların olasılıklarını düzenli bir şekilde ihtimaller dizisine yazar.)
Sonra bu olasıklara göre seçilme ihtimalleri hesaplanır.
En son random bir şekilde p olasılığında adet size'ı kadar populasyondan Random değerler belirler.

---

### `def tek_noktali_cap(p1,p2)`
Diziyi belirli bir noktadan 2 parçaya bölerek yer değişimi işlemini gerçekleştirir.
Benim yaptığım örnek 2 veri kümesinden oluşuyor o yüzden tam ortadan 2 ye bölebiliyorum.

NOT: İki noktalı çaprazlama yapamıyorum çünkü veri kümesi 2 noktadan bölemem.

---

### `def mutasyon(birey, ihtimal, buyukluk)`
Random bir değer belirlenir ve eğer bu değer verilen ihtimalden küçükse buyuklukte bir değişim yapılır.
Bu değişim kopyası oluşturulmuş bireye eklenir ve mutasyonlu birey oluşturulur.


---

### 🔄 evrimsel_algoritma Fonksiyonu Açıklamaları

Fonksiyon, bir hedef çıktıya ulaşmak için genetik algoritma prensipleriyle ağırlık parametrelerini optimize eder.

🔸 Adımlar:
- Her nesilde uygunluk hesaplanır.
- En iyi birey korunur (elitizm).
- Seçim (rulet veya rank), çaprazlama (tek nokta) ve mutasyon uygulanır.
- Sonuçlar yazdırılır ve grafik çizilir.

🔸 Erken durdurma uygulanır: Eğer uygunluk çok iyiyse, işlem bitirilir.

🔸 Parametreler:
- populasyon: Başlangıç bireyleri
- agirlik_katsayilari: Katsayılar
- gercek_y: Hedef y değeri
- nesil_sayisi: Döngü sayısı
- caprazlama_turu: 'tek' veya 'iki'
- secim_turu: 'rulet' veya 'rank'
- mutasyon_ihtimali: 0-1 arası olasılık
- mutasyon_buyuklugu: Mutasyon boyutu
'''

### evrimsel_algoritma(populasyon, nesil_sayisi, secim_turu, mutasyon_ihtimali,mutasyon_buyuklugu)
Bütün bireylerin uygunlukları hesaplanır, en yüksek uygunluk değerine sahip bireyin indeksi alınır.
En yüksek uygunluk değerlerini de alır. En iyilere bu uygunluk değerlerini atar. (Virgülden sonra 3 basamak şeklinde)

### havuz = []
Havuzdan daha sonraki işlemlerde çift işlemler yapacağımız için havuzun maksimum sayısı popülasyonun yarısı olabilir.
Sonra çifter olarak seçtiğimiz bireyleri yine bizim seçitiğimiz rank yada rulet fonksiyonuna gönderiyoruz.
En son bunları seçilenler havuzuna ekliyoruz.

### Yeni nesil oluşturma

Önceden seçtiğimiz en iyi uygunluk değerlerine sahip bireylerin kopyası üzerinden işlem yapıyoruz.
Oluşturduğumuz havuzun içindeki bireylerin büyüklüğü popülasyonun büyüklüğünü aşana kadar seçim havuzundan random bireyleri toplar.
Tek noktalı çaprazlama yapılarak 2 yeni birey oluşturulur. Sonra bu bireyler mutasyon fonksiyonuna gönderilir.
Mutasyona uğramış yeni bireyler listeye eklenir.
Son olarak popülasyondak iyaşlı eski bireyleri silerek yeni mutasyona uğramış çocuk bireylerin kalmasını sağlıyoruz.

