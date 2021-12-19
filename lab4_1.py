import time
import yaml
import json

def main():
    srcPath = "/Users/ed/Documents/itmo/1infa/lab4/src.yaml"
    dstPath = "/Users/ed/Documents/itmo/1infa/lab4/dst_1.json"
    # open source file
    with open(srcPath, mode='r', encoding='utf-8') as rFile:
        # open the file to write
        with open(dstPath, mode='w', encoding='utf-8') as wFile:
            y = yaml.safe_load(rFile)
            json.dump(y, wFile, ensure_ascii=False)

if __name__ == "__main__":
    dstPath = "/Users/ed/Documents/itmo/1infa/lab4/lab4_3.txt"
    with open(dstPath, mode='a', encoding='utf-8') as wFile:
        start_time = time.time()
        main()
        d = (time.time() - start_time) * 1000
        wFile.write("lab4_1.py: %s (seconds*1000)\n" % d)