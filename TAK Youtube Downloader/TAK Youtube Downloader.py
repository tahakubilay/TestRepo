from pytube import YouTube

print("Videoyu ses olarak mı video olarak mı indirmek istiyorsunuz? A= Video B= Ses ")
format = input("Bir tür seçin: ")
link=input("Linki giriniz: ")
yt = YouTube(link)

if format == "a":
    print("Video Başlığı: ",yt.title)
    print("Videonun izlenme sayısı: ",yt.views)
    print("Videonun uzunluğu: ", yt.length, "saniye")
    print("Açıklama: ",yt.description)
    print("Puan: ",yt.rating)
    ys= yt.streams.get_highest_resolution()
    print("Video indiriliyor")
    ys.download()
    print("Videoyu indirme işlemi tamamlandı")

elif format == "b":
    print("Video Başlığı: ",yt.title)
    print("Videonun izlenme sayısı: ",yt.views)
    print("Videonun uzunluğu: ", yt.length, "saniye")
    print("Açıklama: ",yt.description)
    print("Puan: ",yt.rating)
    fileaudio = yt.streams.get_audio_only()
    print("Ses indiriliyor")
    fileaudio.download()
    print("Ses indirme işlemi tamamlandı.")

else:
    Exception

pytube.Youtube('url here').streams.filter(only_audio=True).all()

#https://www.youtube.com/watch?v=wowlZfq43VI


#Video Başlığı
#Videonun izlenme sayısı
#Videonun uzunluğu saniye cinsinden
#Videonun Açıklaması
#Puan

#Bütün ses indirme çeşitleri
#print(yt.streams.filter(only_audio=True))

#Bütün video indirme çeşitleri
#print(yt.streams.filter(only_video=True))

#Bütün indirme biçimleri
#print(yt.streams)

#Bütün progressive biçimler
#print(yt.streams.filter(progressive=True))

#Bütün Yüksek Kaliteler
#print(yt.streams.get_highest_resolution())


