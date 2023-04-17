import os

# Název složky by měl být ve formátu "autor - název alba"
folder_name = os.path.basename(os.getcwd())

# Kontrola správného formátu názvu složky
if " - " not in folder_name:
    print("Název složky nemá správný formát (autor - název alba)")
    exit(1)

# Rozdělení názvu složky na autora a název alba
author, album = folder_name.split(" - ")
print("Autor:", author)
print("Album:", album)