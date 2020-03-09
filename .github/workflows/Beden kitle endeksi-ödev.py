
agirlik = float( input("Lütfen ağırlığınızı giriniz (kg): ") )

boy = float( input("Lütfen boyunuzu giriniz (cm):") )
boy = boy / 100.0  
bki = agirlik / (boy * boy)
c=25

b=c*(boy*boy)

a=agirlik-b



print("BKİ değeri: ", bki)


if bki <18.5:
    print("Zayıfsınız")
    print("Sağlıklı biçimde kilo alabilirsiniz")
   
    if boy<1.40:
         # Belki de çocuk?
         print("Çocuklar için BKİ formülü farklıdır.")         
elif bki < 25:
    print("Sağlıklısınız")
   
elif bki <30:
    print("Az kilolusunuz")
    
elif bki<35:
    print("Dikkat! 1. Obez")
   
    
elif bki<40:
    print("Dikkat! 2. Obez")
       
else:
    print("Dikkat 3. Obez")

if bki <18.5:
    
    
    print(a," kilo almanız gerekiyor" )
            
elif bki < 25:
    print("Sağlıklı yaşam")

elif bki <30:
    print(a," kilo vermeniz gerekiyor.")

elif bki<35:
    print (a," kilo vermeniz gerekiyor.")
    
elif bki<40:
    print(a," kilo vermeniz gerekiyor.")
   
else:
    print(a," kilo vermeniz gerekiyor.")