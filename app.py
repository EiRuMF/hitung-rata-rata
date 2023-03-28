input_str = input("Masukkan nilai numerik, pisahkan dengan koma :",)

nilai_list = input_str.split(",")

nilai_list = [float(nilai)for nilai in nilai_list]

rata_rata = sum(nilai_list) / len(nilai_list)

print("Nilai rata-ratanya adaklah: ", rata_rata)