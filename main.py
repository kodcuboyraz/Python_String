print("Baba meraba") # Ekrana yazı yazdırır.
isim = "Ahmet"
mesaj = "hasanBaba"
mesaj2 = "nasılsın"

print(mesaj + " " + mesaj2)
print(mesaj[4])  # mesaj isimli değişkenin 4. indisindeki harfi yazdırır
print(mesaj[2:5]) # mesaj isimli değişkeni 2. indisinden 5. indisine kadar yazdırır
print(mesaj[::2]) # mesaj isimli değişkenin 2'nin katları olan indislerini yazdırır
print(mesaj[::-1]) # mesaj isimli değişkeni tersten yazdırır
print(mesaj.upper()) # mesaj isimli değişkenin harflerini büyük yazdırır
print(mesaj.lower()) # mesaj isimli değişkenin harflerini küçük yazdırır
print(mesaj.capitalize()) # baş harflerini büyük yazdırır
print(mesaj.startswith("ba")) # yazdığımız string ba ile mi başlıyor diye denetliyor
print(mesaj.endswith("a")) # yazdığımız string en son a harfi ile bitiyor
print(len(mesaj + mesaj2)) # yazdığımız mesajların uzunluklarını topluyor
print("{} , {}".format(isim , mesaj2))
print(f" {isim} {mesaj2} dedi")