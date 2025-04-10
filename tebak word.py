
import random
import os

list_kata = ['ayam','ular','python','bebek','progammer','coding','pelangi','coding','logaritma','aritmatika','komputer']
kata = random.choice(list_kata)

guesses = ''
turns = 12

os.system('cls')
print(f"{"Selamat Datang":^25}")
print(f"{"di Permainan Tebak Kata":^25}")
print(25*'=')

while turns > 0:

    failed = 0 

    for char in kata:
        if char in guesses:
            print(char)

        else:
            print('-')
            failed += 1

    if failed == 0:
        print(f"Kata: {kata}")
        print("Selamat anda berhasil menebak kata")
        break

    guess = input("Tebak kata : ")
    guesses += guess

    if guess not in kata:
        print(f"Salah,sisa putaran anda : {turns} putaran")
        turns -= 1

        if turns == 0:
            print("Anda gagal menebak kata")


print("Terima Kasih Sudah Menciba Program Kami")