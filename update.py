import time
import AutoUpdate
import os
import urllib.error
from getpass import getuser

__author__ = 'Arif "Helmsys"'

try:
    AutoUpdate.set_url("https://raw.githubusercontent.com/Arif-Helmsys/Testing/main/version.txt") # .txt dosyasının raw linki/raw link of the .txt file
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/Arif-Helmsys/Testing/main/exp.py") # .txt dosyasını okuttuktan sonra indirmesini istediğimiz bir program
    AutoUpdate.set_current_version("0.1") # .txt ye yazdığınız mevcut sürüm dışında herhangi bir sürüm numarası yazabiliriz
    print(AutoUpdate.is_up_to_date()) # Üstte yazdığımız sürüm .txt de yazılan sürümle uyuşmuyorsa yani güncel değilse False, Güncel ise True olarak ekrana yazdırır

    if not AutoUpdate.is_up_to_date(): # Eğer güncel değil ise
        print("İndirme İşlemi Başlıyor...")
        time.sleep(1)
        print("indiriliyor...")
        print(AutoUpdate.get_latest_version()) # .txt de ki sürüm  numarasını okuyup ekrana yazdırıyor
        if not os.path.exists("C:\\Users\\"+getuser()+"\\Desktop\\Updater"): # Masaüstünde Updater klasörü yoksa
            print("Klasör Oluşturuldu")
            os.makedirs("C:\\Users\\"+getuser()+"\\Desktop\\Updater") # Masaüstüne Updater klasörünü oluştur
            AutoUpdate.download("C:\\Users\\"+getuser()+"\\Desktop\\Updater\\updater.py") # Oluşturulan klasöre updater adını verdiğimiz .py dosyasını indir

        else: # Şayet Böyle bir klasör varsa
            AutoUpdate.download("C:\\Users\\"+getuser()+"\\Desktop\\Updater\\updater.py") # updater adını verdiğimiz .py dosyasını Önceden var olan klasöre indir

    elif AutoUpdate.is_up_to_date(): # Program Güncel ise
        print("Sürümünüz Güncel!")
except urllib.error.URLError:
    print("İnternet Bağlantınızı Kontrol Edin!")
