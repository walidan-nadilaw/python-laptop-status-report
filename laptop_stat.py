import psutil #library untuk cek process dan system utilities

#mengukur pemakaian cpu dalam interval 1 detik
print(f"\nPemakaian CPU: {psutil.cpu_percent(interval=1)}%\n") 

#mengukur pemakaian memory
memory_info = psutil.virtual_memory()
print(f"Total Memory: {memory_info.total / (1024 ** 2):.2f} MB")
print(f"Memory yang dipakai: {memory_info.used / (1024 ** 2):.2f} MB")
print(f"Memory yang tersedia: {memory_info.available / (1024 ** 2):.2f} MB\n")


#mengukur status batre
battery = psutil.sensors_battery() #call function yang mengecek status batre

if battery is not None :
    print("Persentase Batre:", battery.percent ,"%") #attribut .percent, memanggil persentase batre sekarang

    if battery.power_plugged : print("sedang charger") #attribute .power_plugged, return true false tentang keadaan dicharger
    else : print("tidak sedang charger")

    def convertTime(seconds): #mengformat detik menjadi bentuk jam:menit:detik
        minutes, seconds = divmod(seconds, 60) #teturn tuple berisi jumlah menit dan sisa detik
        hours, minutes = divmod(minutes, 60) #return tuple berisi jumlah jam dan sisa menit
        return "%d:%02d:%02d" % (hours, minutes, seconds) #return jam:menit:detik yang sudah diformat

    print("sisa waktu batre:", convertTime(battery.secsleft),"\n") #panggil function

else:
    print("no battery information available")

"""
gw belum belajar penghapusan file, tetapi barusan belajar library psutil (process and system utilities).
library ini buat kita bisa akses informasi tentang penggungaan sistem (CPU, memori, disks, network, sensors, dll)
di sini, gw pakai untuk cek pemakaian cpu, sisa memory, dan status batre
"""