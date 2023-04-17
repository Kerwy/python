import os
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB

# získání názvu složky
folder_name = os.path.basename(os.getcwd())

# rozdělení názvu složky na autora a album
author, album = folder_name.split(" - ")

# procházení všech mp3 souborů v aktuální složce
for file in os.listdir(os.getcwd()):
    if file.endswith(".mp3"):
        # otevření mp3 souboru a získání ID3 tagů
        audio = ID3(os.path.join(os.getcwd(), file))
        
        # doplnění ID3 tagů
        audio["TIT2"] = TIT2(encoding=3, text=os.path.splitext(file)[0])
        audio["TPE1"] = TPE1(encoding=3, text=author)
        audio["TALB"] = TALB(encoding=3, text=album)
        
        # uložení změn
        audio.save()