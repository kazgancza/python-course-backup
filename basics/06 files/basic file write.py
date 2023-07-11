# "w" tworzy plik i zapisuje/usuwa zawartość i nadpisuje
fh = open("test.txt", "w")
fh.write("content1\n")
fh.write("content2\n")
fh.close()

# "a" dopisuje do pliku
fh2 = open("test.txt", "a")
fh2.write("content3\n")
fh2.close()