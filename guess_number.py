import random

# determine random number
random_number = random.randint(1,100)

# start game
print("Selamat datang di permainan Tebak Angka!")
print("Tebak angka antara 1 sampai 100")

guess = None

while guess != random_number:
    guess = int(input("Masukkan angka yang Anda pikirkan: "))
    if guess < random_number:
        print("Angka yang Anda masukkan terlalu kecil")
    elif guess > random_number:
        print("Angka yang Anda masukkan terlalu besar")
    else:
        print("Selamat! Anda berhasil menebak angka yang saya pikirkan!")