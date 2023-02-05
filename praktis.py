import time

while True:
        #Form LOGIN
        print("Login admin\n")
        user = input("Username: ")
        pwd = input("Password: ")
        if user == 'admin' and pwd == 'bylukisman':
            print("Checking")
            time.sleep(1.5)
            print("Login Berhasil\n")
            break
        else:
            print("Checking")
            time.sleep(1.0)
            print("Login Gagal.\n")

def main():
    # Membaca jumlah uang dari file
    try:
        with open("saldooo.txt", "r") as f:
            balance = int(f.readline().strip())
    except:
        # Jika file tidak ada atau korup, buat file baru dengan saldo 0
        balance = 0
        with open("saldooo.txt", "w") as f:
            f.write("0")
    
    while True:
        # Tampilkan menu utama
        print("\n\nPilih opsi:")
        print("1. Lihat saldo")
        print("2. Tambah uang")
        print("3. Kurangi uang")
        print("4. Keluar")
        choice = input("\nMasukkan pilihan: ")
        
        if choice == "1":
            # Tampilkan saldo saat ini
            print("Saldo:", balance)
        elif choice == "2":
            # Tambah uang
            amount = int(input("Masukkan jumlah uang: "))
            balance += amount
            print("Saldo anda bertambah ", amount)
        elif choice == "3":
            # Kurangi uang
            amount = int(input("Masukkan jumlah uang: "))
            if amount > balance:
                print("Saldo anda kurang")
            else:
                balance -= amount
                print("Uang keluar", amount)
        elif choice == "4":
            # Keluar dari program
            print("kamu telah keluar dari Program.")
            break
        else:
            # Pilihan salah
            print("Pilihan tidak ada.")
        
        # Simpan saldo ke file
        with open("saldooo.txt", "w") as f:
            f.write(str(balance))

if __name__ == "__main__":
    main()
