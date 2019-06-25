print "ProlabII-Proje3 Uygulamasi"

ayaKadarGecenGun = 0

def ArtikYil(yil):
    if (yil%4==0 and yil%100!=0 or yil%400==0):
        return 1
    else:
        return 0

gun = input("Gun giriniz: ")
ay = input("Ay giriniz: ")
yil = input("Yil giriniz: ")

yildakiGunler = (365*yil) + (yil/4) 

i=1
while (i<ay):
    if (i<=7):
        if (i==2):
            ayaKadarGecenGun = ayaKadarGecenGun + 28 + ArtikYil(yil)
        elif (i%2==0):
            ayaKadarGecenGun = ayaKadarGecenGun + 30
        else:
            ayaKadarGecenGun = ayaKadarGecenGun + 31
    else:
        if (i%2==0):
            ayaKadarGecenGun = ayaKadarGecenGun + 31
        else:
            ayaKadarGecenGun = ayaKadarGecenGun + 30
    i=i+1


toplamGun = ayaKadarGecenGun + gun + yildakiGunler

hangiGun = (toplamGun%7)-2

if (hangiGun==0):
    print "Pazar"
elif (hangiGun==1):
    print "Pazartesi"
elif (hangiGun==2):
    print "Sali"
elif (hangiGun==3):
    print "Carsamba"
elif (hangiGun==4):
    print "Persembe"
elif (hangiGun==5 or hangiGun==-2):
    print "Cuma"
else:
    print "Cumartesi"
























