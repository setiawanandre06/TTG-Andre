import math

def piramida(jumlah_baris):
    try:
        value = int(jumlah_baris)
    except ValueError:
        print("Parameter yang di input harus integer")
        return
    
    subtractor = 1
    for idx in range(jumlah_baris):
        for idx2 in range(jumlah_baris*2-subtractor):
            print("*", end="")
        print("")
        subtractor += 2

def kelompok_bilangan_genap(jumlah_bilangan, jumlah_kelompok):
    if jumlah_kelompok > jumlah_bilangan:
        print("Jumlah kelompok tidak boleh lebih besar dari jumlah bilangan")

    list_angka = []
    list_angka_final = []
    angka = 0
    for idx in range(jumlah_bilangan):
        angka += 2
        list_angka.append(angka)

    angka_per_list = int(jumlah_bilangan / jumlah_kelompok)
    kelebihan = jumlah_bilangan % jumlah_kelompok
    jumlah_non_kelebihan = jumlah_kelompok - kelebihan

    counter = 0
    for idx in range(jumlah_non_kelebihan):
        list_split_angka = []
        for idx2 in range(angka_per_list):
            list_split_angka.append(list_angka[counter])
            counter += 1
        list_angka_final.append(list_split_angka)

    for idx in range(kelebihan):
        list_split_angka = []
        for idx2 in range(angka_per_list+1):
            list_split_angka.append(list_angka[counter])
            counter += 1
        list_angka_final.append(list_split_angka)

    print(list_angka_final)

piramida(5)
kelompok_bilangan_genap(8, 4)