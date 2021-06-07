import time
import sys
from pathlib import Path
if __name__ == "__main__":
    inputs = sys.argv[1:]
    diskLetter = inputs[0]
    disk = open(r"\\.\\" + diskLetter[0:2],'rb')
    disk.seek(0)
    rawData = disk.read(33554432).hex(sep=' ', bytes_per_sep=1)
    Path("C:\\GenSoudTools\\ExportsSDHC").mkdir(parents=True, exist_ok=True)
    text_file = open("C:\\GenSoudTools\\ExportsSDHC\\ExportSDHC" + time.strftime("_%d_%m_%Y_%H_%M_%S",time.localtime())  + ".txt", "w")
    text_file.write(rawData)
    text_file.close()

