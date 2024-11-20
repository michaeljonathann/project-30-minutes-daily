print("====== Project Kalkulator ======")

# Function untuk operasi penjumlahan, pengurangan, perkalian, pembagian
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

# Interface sederhana
print("Pilih Operasi")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

operasi = int(input("Masukkan pilihan (1/2/3/4): ")) # input operation

# input number
num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

# Conditioning
if operasi == 1:
    print(num1, "+", num2, "=" , tambah(num1,num2))

elif operasi == 2:
    print(num1, "-", num2, "=", kurang(num1,num2))

elif operasi == 3:
    print(num1, "*", num2, "=", kali(num1,num2))

elif operasi == 4:
    print(num1, "/", num2, "=", bagi(num1,num2))

else:
    print("Pilihan tidak valid")