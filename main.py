#Bismillaxi rohmani rohim
#Kerakli kutubxonalar
try:
    import zipfile
    import time
 
    import os
    
except ImportError:
    pass
    print("Iltimos kuting!\nKutubxonalar yukalnish jarayonida")
    print("Zip faylni kutubxonasini yuklash boshlandi..")
    
#Dastur kodi
ishora = True
while ishora:
    pass
    print("DIQQAT! Siz ZIP fayl yaratmoqchi bo'lsangiz fayl nomining ohiriga faylnomi.zip yozishni unutmang!")
    to_zip_filename = zipfile.ZipFile(input('Faylga nom bering: '),'w')
    
    to_zip_filename.write(input("Path yani yo'lini ko'rsating: "))

    to_zip_filename.close()
    savol = input("Dastur to'xtasinmi [Ha] [Yo'q]")
    if savol == 'Y' or 'Yo\'q':
        print("Davom etilyapti..")  
    if savol == 'H' or 'Ha':
        ishora = False
        os.system('exit')