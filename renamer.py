import os

count = 1
for file in sorted(os.listdir(os.getcwd())):
    if file.endswith(".mp3"):
        os.rename(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), f"{count}.mp3"))
        count += 1