# Kopiuje pliki wideo dzieląc je na pionowe, poziome i kwadratowe
# Foldery muszą być wcześniej stworzone
# Nie może być innych plików i folderów

import os
import cv2
import shutil

sourcePath = ""
os.chdir(sourcePath)

filesList = list(os.listdir())
filesList.remove("horizontal")
filesList.remove("vertical")
filesList.remove("square")


def copyFiles():
    for file in filesList:
        video = cv2.VideoCapture(file)
        height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = video.get(cv2.CAP_PROP_FRAME_WIDTH)

        if height > width:
            shutil.copy(f"{sourcePath}\\{file}", f"{sourcePath}\\vertical")
        elif height < width:
            shutil.copy(f"{sourcePath}\\{file}", f"{sourcePath}\\horizontal")
        else:
            shutil.copy(f"{sourcePath}\\{file}", f"{sourcePath}\\square")

copyFiles()
