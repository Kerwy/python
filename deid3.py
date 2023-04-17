from mutagen.id3 import ID3
import os

def remove_id3_tags():
    # získání aktuální složky
    path = os.getcwd()
    # získání seznamu souborů v dané složce
    files = os.listdir(path)
    # odstranění ID3 tagu ze souborů
    for file in files:
        if file.endswith(".mp3"):
            audio = ID3(os.path.join(path, file))
            audio.delete()
            audio.save()

remove_id3_tags()