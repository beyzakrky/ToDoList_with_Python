#Kütüphaneler ve dosya
import json
import os

FILE_NAME = "gorevler.txt"
#Bu kod bloğu ile yüklenen dosyayı okuruz.
def dosya_oku():
    """Dosyadan görevleri okur ve liste olarak döndürür."""
    # Bu fonksiyon sayesinde dosyadan görevleri okuyoruz ve daha sonra liste olarak return ediyoruz.
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                # Dosya boşsa veya geçersizse hata almamak için kontrol yapıyoruz.
                icerik = file.read()
                if icerik.strip():
                    görevler = json.loads(icerik)
                    # Kullanıcıya geri bildirim veriyoruz.
                    print("Görevler başarıyla yüklendi.\n")
                    return görevler
        except Exception as e:
            print(f"Dosya okunurken bir hata oluştu: {e}")
            # Hata varsa belirtiyoruz.

    print("Görev dosyası bulunamadı veya okunamadı. Yeni bir liste oluşturuldu.\n")
    return []

#Dosya kaydedilir ki üstünde işlem yapılabilsin.
def dosya_kaydet(gorevler):
    """Görev listesini utf-8 formatında metin dosyasına kaydeder."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(gorevler, file, ensure_ascii=False, indent=4)
   #Yine hata mesajı.
    except Exception as e:
        print(f"Dosya kaydedilirken bir hata oluştu: {e}")

# Bu fonksiyon sayesinde görevlerin öncelik sırası belirlenebilir ve ona göre sıralama yapılabilir.
def gorevleri_listele(gorevler, siralama_kriteri=None):
    """Mevcut görevleri numaralandırarak listeler ve isteğe bağlı sıralar."""
    if not gorevler:
        print("Henüz görev bulunmamaktadır.")
        return

    listelenecek = gorevler.copy()

    # Belirli kriterlere göre sıralama yapıyoruz. Öncelik sıralaması olmalı.
    if siralama_kriteri == 'oncelik':
        oncelik_sirasi = {'Yüksek': 1, 'Orta': 2, 'Düşük': 3}
        listelenecek.sort(key=lambda x: oncelik_sirasi.get(x.get('oncelik', 'Düşük'), 3))
    elif siralama_kriteri == 'durum':
        listelenecek.sort(key=lambda x: x.get('tamamlandi', False))

    print("\n" + "-"*40)
    print(f"{'No':<4} | {'Görev':<30} | {'Öncelik':<8} | {'Tarih':<10} | {'Durum'}")
    print("-" * 75)

    for idx, gorev in enumerate(listelenecek, 1):
        durum = "[X]" if gorev.get('tamamlandi') else "[ ]"
        metin = gorev.get('metin', '')[:28] + ".." if len(gorev.get('metin', '')) > 30 else gorev.get('metin', '')
        oncelik = gorev.get('oncelik', '-')
        tarih = gorev.get('tarih', '-')

        print(f"{idx:<4} | {metin:<30} | {oncelik:<8} | {tarih:<10} | {durum}")
    print("-" * 75 + "\n")

#Bu kod bloğu kullanıcıya yeni görev ekleme imkanı sunar. Bu sayede de to-do list'imizi genişletmiş oluruz.
def gorev_ekle(gorevler):
    """Yeni bir görev ekler ve dosyaya kaydeder."""
    metin = input("Yeni görev: ").strip()
    #Eğer hiçbir şey yazılmazsa hata vermesi gerekir.
    if not metin:
        print("Hata: Boş görev eklenemez!")
        return

    # Öncelik seviyesi
    oncelik = input("Öncelik Seviyesi (Yüksek/Orta/Düşük) [Boş geçilebilir]: ").strip().capitalize()
    if oncelik not in ['Yüksek', 'Orta', 'Düşük']:
        oncelik = 'Belirtilmedi'

    #Son tarih eklenebilir. Bu özellik istenirse boş geçilebilir.
    tarih = input("Son Tarih (GG/AA/YYYY) [Boş geçilebilir]: ").strip()
    if not tarih:
        tarih = 'Belirtilmedi'

    yeni_gorev = {
        "metin": metin,
        "oncelik": oncelik,
        "tarih": tarih,
        "tamamlandi": False
    }

    gorevler.append(yeni_gorev)
    print(f"'{metin}' görevi eklendi.")
    dosya_kaydet(gorevler)

# Yeni eklenecek görevleri veya daha önceki görevlerin özelliklerini, önceliklerini düzenlemek için kullanılan fonksiyon kod bloğu.
def gorev_duzenle(gorevler):
    """Mevcut bir görevi düzenler, tamamlandı olarak işaretler veya önceliğini günceller."""
    gorevleri_listele(gorevler)
    if not gorevler:
        return

    try:
        secim = int(input("Düzenlemek istediğiniz görevin numarası: "))
        if 1 <= secim <= len(gorevler):
            hedef_gorev = gorevler[secim - 1]

            print("\n--- İŞLEM SEÇENEKLERİ ---")
            print("1. Metni/Detayları Düzenle")
            print("2. Tamamlandı/Tamamlanmadı Olarak İşaretle")
            print("3. Öncelik Seviyesini Değiştir")  # Yeni eklenen seçenek

            alt_secim = input("İşlem seçiniz (1/2/3): ").strip()

            if alt_secim == '1':
                yeni_metin = input(f"Yeni görev metni ({hedef_gorev['metin']}): ").strip()
                if yeni_metin:
                    hedef_gorev['metin'] = yeni_metin
                    dosya_kaydet(gorevler)
                    print("Görev başarıyla güncellendi.")
                else:
                    print("Hata: Boş görev eklenemez!")

            elif alt_secim == '2':
                hedef_gorev['tamamlandi'] = not hedef_gorev['tamamlandi']
                durum = "Tamamlandı" if hedef_gorev['tamamlandi'] else "Tamamlanmadı"
                dosya_kaydet(gorevler)
                print(f"Görev durumu '{durum}' olarak güncellendi.")

            elif alt_secim == '3':
                # Öncelik değiştirme bloğu
                mevcut_oncelik = hedef_gorev.get('oncelik', 'Belirtilmedi')
                yeni_oncelik = input(f"Yeni Öncelik Seviyesi (Yüksek/Orta/Düşük) [Mevcut: {mevcut_oncelik}]: ").strip().capitalize()

                if yeni_oncelik in ['Yüksek', 'Orta', 'Düşük']:
                    hedef_gorev['oncelik'] = yeni_oncelik
                    dosya_kaydet(gorevler)
                    print(f"Görev önceliği '{yeni_oncelik}' olarak başarıyla güncellendi.")
                else:
                    print("Hata: Geçersiz bir öncelik seviyesi girdiniz. İşlem iptal edildi.")
            else:
                print("Geçersiz seçim.")
        else:
            print("Geçersiz görev numarası!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")

# Belki kullanıcı bir görevi bitirip silmek isteyecek. Bu nedenle görev_sil fonksiyonu ekliyoruz.
def gorev_sil(gorevler):
    """Mevcut bir görevi siler."""
    gorevleri_listele(gorevler)
    if not gorevler:
        return

    try:
        secim = int(input("Silmek istediğiniz görevin numarası: "))
        if 1 <= secim <= len(gorevler):
            silinen = gorevler.pop(secim - 1)
            print(f"'{silinen['metin']}' görevi silindi.")
            dosya_kaydet(gorevler)
        else:
            print("Geçersiz görev numarası!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
    
def ana_menu():
    """Ana program döngüsü."""
    print("--- To-Do List Uygulamasına Hoş Geldiniz! ---")
    gorevler = dosya_oku()

    while True:
        print("\n=== ANA MENÜ ===")
        print("1. Görevleri Listele")
        print("2. Yeni Görev Ekle")
        print("3. Görev Düzenle / Tamamla")
        print("4. Görev Sil")
        print("5. Görevleri Sırala (Önceliğe Göre)")
        print("6. Çıkış")

        secim = input("\nSeçiminiz (1-6): ").strip()

        if secim == '1':
            gorevleri_listele(gorevler)
        elif secim == '2':
            gorev_ekle(gorevler)
        elif secim == '3':
            gorev_duzenle(gorevler)
        elif secim == '4':
            gorev_sil(gorevler)
        elif secim == '5':
            gorevleri_listele(gorevler, siralama_kriteri='oncelik')
        elif secim == '6':
            print("Programdan çıkılıyor. İyi çalışmalar!")
            break
        else:
            print("Geçersiz bir seçim yaptınız, lütfen tekrar deneyin.")

if __name__ == "__main__":
    ana_menu()

