import time
import sys

if __name__ == "__main__":
    inputs = sys.argv[1:]
    diskLetter = inputs[0]
    disk = open(r"\\.\\" + diskLetter[0:2],'rb')
    disk.seek(0)
    rawData = disk.read(16777216).hex(sep=' ', bytes_per_sep=1)
    text_file = open("C:\\result\\ExportSDHC.txt", "w")
    text_file.write(rawData)
    text_file.close()