print("Ortalama Bulucuya Hoş Geldiniz")
a = 1
while a == 1:



    sayiogrenci = input("Veri Numarası giriniz (2-7 - çıkış): ")

    if sayiogrenci == "5":
        sayi1 = input("1. Sayı: ")
        sayi2 = input("2. Sayı: ")
        sayi3 = input("3. Sayı: ")
        sayi4 = input("4. Sayı: ")
        sayi5 = input("5. Sayı: ")
        print("Ortalama:", (int(sayi1) + int(sayi2) + int(sayi3) + int(sayi4) + int(sayi5)) / 5)
    elif sayiogrenci == "4":
        sayi1 = input("1. Sayı: ")
        sayi2 = input("2. Sayı: ")
        sayi3 = input("3. Sayı: ")
        sayi4 = input("4. Sayı: ")
        print("Ortalama:", (int(sayi1) + int(sayi2) + int(sayi3) + int(sayi4)) / 4)
    elif sayiogrenci == "3":
        sayi1 = input("1. Sayı: ")
        sayi2 = input("2. Sayı: ")
        sayi3 = input("3. Sayı: ")
        print("Ortalama:", (int(sayi1) + int(sayi2) + int(sayi3)) / 3)
    elif sayiogrenci == "2":
        sayi1 = input("1. Sayı: ")
        sayi2 = input("2. Sayı: ")
        print("Ortalama:", (int(sayi1) + int(sayi2)) / 2)
    elif sayiogrenci == "6":
        sayi1 = input("1. Sayı: ")
        sayi2 = input("2. Sayı: ")
        sayi3 = input("3. Sayı: ")
        sayi4 = input("4. Sayı: ")
        sayi5 = input("5. Sayı: ")
        sayi6 = input("6. Sayı: ")
        print("Ortalama:", (int(sayi1) + int(sayi2) + int(sayi3) + int(sayi4) + int(sayi5) + int(sayi6)) / 6)
    elif sayiogrenci == "7":
        sayi1 = input("1. Sayı: ")
        sayi2 = input("2. Sayı: ")
        sayi3 = input("3. Sayı: ")
        sayi4 = input("4. Sayı: ")
        sayi5 = input("5. Sayı: ")
        sayi6 = input("6. Sayı: ")
        sayi7 = input("7. Sayı: ")
        print("Ortalama:", (int(sayi1) + int(sayi2) + int(sayi3) + int(sayi4) + int(sayi5) + int(sayi6) + int(sayi7)) / 7)
    elif sayiogrenci == "çıkış":
        a = 2