#ATM PARA ÇEKME YATIRMA SORGULAMA PROGRAMI
#BAŞLANGIÇ BAKİYE:5000 TL
import time #zaman modülünü içe aktarıyoruz 
bakiye=5000 # BAKİYE DEĞİŞKENİ OLUŞTURUYORUZ 

while True: # DÖNGÜ EKLEME.HER İŞLEMDEN SONRA UYGULAMAYI BAŞA DÖNDÜRÜR
    işlem=int(input('işlem seçiniz yatırma 1 cekme 2 sorgulama 3: ')) # KULLANICIDAN GİRİŞ ALMA İNT TAM SAYI GİRİŞİ İÇİN
    
    if işlem == 1: # KOŞULLU İFADELER. işlem E GİRİLEN DEĞERİ KONTROL EDER == eşitse DEMEK GİRİLEN DEĞER KENDİNDEN SONRAKİNE EŞİTSE ÇALIŞIR.
        #VE SONRASINDAKİ ADIMA GEÇER
        yatırma=int(input('yatırılacak miktar giriniz : '))
        print('İŞLEM YAPILIYOR LÜTFEN BEKLEYİZ !!!!')
        time.sleep(1)#KENDİNDEN SONRAKİ DEĞERİ YAZMADAN ÖNCE BEKLEYCEĞİ SANİYE SÜRESİ 
        print(f' önceki bakiyeniz {bakiye} tl.\n yatırılan tutar {yatırma} tl.\nTOPLAM: {bakiye+yatırma} tl')#SÜSLÜ PARANTEZ İÇİNDEKİ DEĞERDE
        #HANGİ DEĞİŞKEN YAZIYORSA ONU EKRANA YAZAR.
        bakiye+=yatırma #DEĞİŞKENİ GİRİLEN DEĞER İLE TOPLAR +=
        
       
    elif işlem == 2: # KOŞULLU İFADELER. işlem E GİRİLEN DEĞERİ KONTROL EDER == eşitse DEMEK GİRİLEN DEĞER KENDİNDEN SONRAKİNE EŞİTSE ÇALIŞIR.
        #VE SONRASINDAKİ ADIMA GEÇER
        while True:
            çekilen=int(input('çekilecek tutar girin : '))
            if çekilen > bakiye :
                print(f'BAKİYE YETERSİZ!! MEVCUT BAKİYE: {bakiye} TL.')
                
            else:
                bakiye-=çekilen
                print('İŞLEM YAPILIYOR LÜTFEN BEKLEYİZ !!!!')
                time.sleep(3)
                print(f'çekmek istediğiniz tutar: {çekilen} tl.\nmevcut bakiye:{bakiye} tl.\nkalan tutar: {bakiye} tl.')
                break #DÖNGÜYÜ SONLANDIRIR   
    elif işlem  == 3:# KOŞULLU İFADELER. işlem E GİRİLEN DEĞERİ KONTROL EDER == eşitse DEMEK GİRİLEN DEĞER KENDİNDEN SONRAKİNE EŞİTSE ÇALIŞIR.
        #VE SONRASINDAKİ ADIMA GEÇER
        print('İŞLEM YAPILIYOR LÜTFEN BEKLEYİZ !!!!')
        time.sleep(1)
        print(f'bakiyeniz: {bakiye} tl')import time#zaman modülünü içe aktarıyoruz 
bakiye=5000 # BAKİYE DEĞİŞKENİ OLUŞTURUYORUZ 

while True: # DÖNGÜ EKLEME.HER İŞLEMDEN SONRA UYGULAMAYI BAŞA DÖNDÜRÜR
    işlem=int(input('işlem seçiniz yatırma 1 cekme 2 sorgulama 3: ')) # KULLANICIDAN GİRİŞ ALMA İNT TAM SAYI GİRİŞİ İÇİN
    
    if işlem == 1: # KOŞULLU İFADELER. işlem E GİRİLEN DEĞERİ KONTROL EDER == eşitse DEMEK GİRİLEN DEĞER KENDİNDEN SONRAKİNE EŞİTSE ÇALIŞIR.
        #VE SONRASINDAKİ ADIMA GEÇER
        yatırma=int(input('yatırılacak miktar giriniz : '))
        print('İŞLEM YAPILIYOR LÜTFEN BEKLEYİZ !!!!')
        time.sleep(1)#KENDİNDEN SONRAKİ DEĞERİ YAZMADAN ÖNCE BEKLEYCEĞİ SANİYE SÜRESİ 
        print(f' önceki bakiyeniz {bakiye} tl.\n yatırılan tutar {yatırma} tl.\nTOPLAM: {bakiye+yatırma} tl')#SÜSLÜ PARANTEZ İÇİNDEKİ DEĞERDE
        #HANGİ DEĞİŞKEN YAZIYORSA ONU EKRANA YAZAR.
        bakiye+=yatırma #DEĞİŞKENİ GİRİLEN DEĞER İLE TOPLAR +=
        
       
    elif işlem == 2: # KOŞULLU İFADELER. işlem E GİRİLEN DEĞERİ KONTROL EDER == eşitse DEMEK GİRİLEN DEĞER KENDİNDEN SONRAKİNE EŞİTSE ÇALIŞIR.
        #VE SONRASINDAKİ ADIMA GEÇER
        while True:
            çekilen=int(input('çekilecek tutar girin : '))
            if çekilen > bakiye :
                print(f'BAKİYE YETERSİZ!! MEVCUT BAKİYE: {bakiye} TL.')
                
            else:
                bakiye-=çekilen
                print('İŞLEM YAPILIYOR LÜTFEN BEKLEYİZ !!!!')
                time.sleep(3)
                print(f'çekmek istediğiniz tutar: {çekilen} tl.\nmevcut bakiye:{bakiye} tl.\nkalan tutar: {bakiye} tl.')
                break #DÖNGÜYÜ SONLANDIRIR   
    elif işlem  == 3:# KOŞULLU İFADELER. işlem E GİRİLEN DEĞERİ KONTROL EDER == eşitse DEMEK GİRİLEN DEĞER KENDİNDEN SONRAKİNE EŞİTSE ÇALIŞIR.
        #VE SONRASINDAKİ ADIMA GEÇER
        print('İŞLEM YAPILIYOR LÜTFEN BEKLEYİZ !!!!')
        time.sleep(1)
        print(f'bakiyeniz: {bakiye} tl')
