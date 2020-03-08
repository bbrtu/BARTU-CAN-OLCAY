boy=float(input("Boyunuzu giriniz: "))
kilo=float(input("Kilonuzu giriniz: "))
bki=kilo/((boy/100)**2)
print("Vücut kitle indeks'iniz {}".format(round(bki,2)))
print("Durumunuz: ")
if bki <=18.5:
    print("Zayıfsınız.")
    print("{} Kilo almanız gerekiyor".format(round(18.5*((boy/100)**2)-kilo,2)))
elif bki <=24.9:
    print("Sağlıklısınız.")
elif bki<=29.9:
    print("Fazla kilolusunuz.")
    print("{} Kilo vermeniz gerekiyor".format(round(kilo-24.9*((boy / 100) ** 2)),2))
elif bki<=39.9:
    print("Obezsiniz.")
    print("{} Kilo vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
else:
    print("Aşırı obezsiniz.")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))


