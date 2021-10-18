# LIST
listKode = []
jenisPotong = []
listHarga = []
banyakPotong = []
listJumlah = []

# KETERANGAN
print("""
=============================
    GEROBAK FRIED CHICKEN
=============================
Kode\tJenis Potong\tHarga
D\tDada\t\t2500
P\tPaha\t\t2000
S\tSayap\t\t1500
=============================
    """)

# LOGIN


def login():
    print("-----------------------")
    masuk = input("Masuk Y/N : ")
    print("-----------------------")
    if masuk == "y" or masuk == "Y":
        print("SELAMAT DATANG")
    else:
        print("Terima Kasih")
        exit()


login()

print("=========================")
# INPUT
banyakJenis = int(input("Banyak Jenis : "))

if banyakJenis <= 3:
    for i in range(banyakJenis):
        print("Jenis ke - " + str(i + 1))
        listKode.append(input("Kode Potong D/P/S : "))
        banyakPotong.append(int(input("Banyak Potong : ")))
else:
    print("Tidak Bisa Lebih Dari 3 Jenis")
    login()

# PROSES
for i in range(banyakJenis):
    if listKode[i] == "D":
        jenisPotong.append("Dada")
        listHarga.append(2500)
    elif listKode[i] == "P":
        jenisPotong.append("Paha")
        listHarga.append(2000)
    else:
        jenisPotong.append("Sayap")
        listHarga.append(1500)

for i in range(banyakJenis):
    listJumlah.append(banyakPotong[i] * listHarga[i])

print("""
----------------------------------------------------------
        GEROBAK FRIED CHICKEN
----------------------------------------------------------
No.  Jenis Potong  Harga Satuan  Banyak Beli  Jumlah Harga
----------------------------------------------------------
    """)

for i in range(banyakJenis):
    print("{}\t{}\t\t{}\t\t{}\t{}".format
          (i + 1, jenisPotong[i], listHarga[i], banyakPotong[i], listJumlah[i]))

print("-----------------------------\n")


def operasi():
    print("Pajak 10%   :  " + str(pajak))
    print("Total Bayar : " + str(totalBayar))


def pembayaran():
    bayar = float(input("Uang Pembayaran : "))
    kembalian = bayar - totalBayar
    print("Kembalian : " + str(kembalian))


if banyakJenis == 1:
    pajak = listJumlah[0] * 0.1
    totalBayar = listJumlah[0] + pajak
    print("Jumlah Bayar: " + str(listJumlah[0]))
    operasi()
    pembayaran()
elif banyakJenis >= 2:
    tambah = float(listJumlah[0] + listJumlah[1])
    pajak = tambah * 0.1
    totalBayar = tambah + pajak
    print("Jumlah Bayar: " + str(tambah))
    operasi()
    pembayaran()
else:
    tambah = float(listJumlah[0] + listJumlah[1] + listJumlah[2])
    pajak = tambah * 0.1
    totalBayar = tambah + pajak
    print("Jumlah Bayar: " + str(tambah))
    operasi()
    pembayaran()
