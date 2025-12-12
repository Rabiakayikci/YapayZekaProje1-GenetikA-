

import numpy as np
import random


def birey_olustur ():
   x1 = np.random.uniform (25,80) #25 ten başlattım çünkü x1 >25 koşulu var eksi puan yememesi için

   x2 = np.random.uniform (10,80)

   birey = np.array([x1,x2])
   return birey


def populasyon_olustur (populasyon_sayisi):
  pop= []

  for i in range (populasyon_sayisi):
    yeni = birey_olustur()
    pop.append(yeni)

  return pop


def tahmin_y (birey): #ağırlıklarımı fonksiyona koyup y değerini hesaplıyorum

    #benim fonksiyonum 2 değişkenli olduğu için 2 birey olacak, dizi şeklinde (x1,x2)
    x1= birey[0]
    x2= birey[1]

    y = 3*x1+ 2*x2+ x1*x2- 0.5 *(x2**2)
    return y


def kontrol (birey): #aykırı değerleri hesaplayıp eksiltme yapacağız
    x1= birey[0]
    x2= birey[1]

    hata_sayisi = 0
    if x1 < 25:
      hata_sayisi +=1

    if x1 + x2 > 100:
      hata_sayisi += 1

    return hata_sayisi

def uygunluk_hesapla (birey):

    as_puan = tahmin_y(birey)
    hata_tekrari = kontrol(birey)

    ceza_puani = hata_tekrari * 3000

    gercek_uyg = as_puan - ceza_puani
    return gercek_uyg


def rulet_secim (populasyon,uygunluklar, adet=2):

  uygunluklar = np.array(uygunluklar)

  min_puan = np.min(uygunluklar)

  if min_puan < 0:
      poz_uygunluklar = uygunluklar - min_puan +1    #rulette negatif değerler sıkıntı çıkarabileceği için dizideki en küçük değeri 1 yapacak şekilde pozitife döndürme yapıyoruz

  else:
     poz_uygunluklar= uygunluklar

  toplam_puan = np.sum(poz_uygunluklar)

  if toplam_puan == 0:
      rastegele_indeksler = np.random.choice(len(populasyon), size = adet) #populasyonun içinden adet kadar random bireyin indeksini seçer
      return populasyon[rastegele_indeksler]

  olasiliklar = poz_uygunluklar / toplam_puan
  secilen_indeksler = np.random.choice(len(populasyon), size = adet, p = olasiliklar) # hesaplanan olasıklara göre populasyondan seçim yapar
  return populasyon[secilen_indeksler]


def rank_secim (populasyon, uygunluklar, adet =2):
  N= len(populasyon)
  sirali_indeks = np.argsort(uygunluklar)  #Puanlara göre küçükten büyüğe sıralama yapar(ADRESLERİ SIRALAR)
  payda = N * (N+1) / 2
  secim_ihtimal = np.array([(i+1)/ payda for i in range(N)]) #rankların hepsi toplandı ve paydaya eşitlendi,pay kısmı ise hangi rankta olduğunu ifade eder o yüzden döngüye sokarak olasılıklarını hespladık

  ihtimaller = np.zeros(N)
  for i, orjinal_indeks in enumerate(sirali_indeks): #enumerate bize 2 değer verir
                                                            #1.döngü kaçıncı adımda
                                                            #2.orjinal dizide neredeyiz

    ihtimaller[orjinal_indeks] = secim_ihtimal[i]  # küçükten büyük değere göre sıralanmış adresleri sırayla gezer ve onların olasılıklarını düzenli bir şekilde ihtimaller dizisine yazar
  ihtimaller = ihtimaller / np.sum(ihtimaller)#olasılık değerlerinin toplamı 1 mi kontrol eder

  secilen_indeks = np.random.choice(len(populasyon), size = adet, p = ihtimaller)
  return populasyon[secilen_indeks]


def tek_noktali_cap(p1,p2):
  nokta = random.randint(1, len(p1)-1) #diziyi (p1 i)1'den başlayarak uzunluğundan 1 eksik kadar böler (bizim dizi 2 eleman olduğu için ikiye bölmüş oluyor) randint => bölme komutu
                                       #nokta değişkeni bir indis sayı tutar

  c1 = np.concatenate((p1[:nokta], p2[nokta:])) #p1[:nokta] => 0. indisten başla nokta indisine kadar git nokta indisini alma p2[nokta:] => nokta indisinden başla sonuna kadar al
                                                #concatenate => birleştir bunları
  c2 = np.concatenate((p2[:nokta], p1[nokta:]))

  return c1, c2

#benim uygulamam 2 veri kümesinden (x1,x2) oluşuyor bu yüzden iki noktalı çaprazlama yapamam bir bireyi başka bir şekilde bölemem


def mutasyon(birey, ihtimal, buyukluk):
  yeni_birey = birey.copy()

  for i in range(len(yeni_birey)):
      if np.random.rand() < ihtimal:
        degisim = buyukluk * (np.random.rand()-0.5)
        yeni_birey[i] += degisim

  yeni_birey[0] = np.clip(yeni_birey[0], 25, 80) #aykırı değer olmaması yani x1 > 25 x1<80 olma koşulunu aşmaması için düzenleme yapılır eğer 25'ten küçükse 25 olur
  yeni_birey[1] = np.clip(yeni_birey[1], 10, 80)
  return yeni_birey

