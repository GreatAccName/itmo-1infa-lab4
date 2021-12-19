import time
import re

def isInt(s: str):
    if re.match(r'[0-9]+$', s):
        return True
    return False
def isBool(s: str):
    if re.match(r'([Tt]rue)|([Ff]alse)', s):
        return True
    return False
def parseVal(s: str):
    if s[len(s)-1] == ':':
        return ""
    i = re.search(r':', s).start() + 2
    val = s[i:]
    if isInt(val) or isBool(val):
        return val
    return '"' + val + '"'
def parseName(s: str):
    res = re.split(r':', s)
    if re.match(r'- ', res[0]):
        return '"'+res[0][2:]+'"'
    else:
        return '"'+res[0]+'"'
def countSpaces(s: str):
    cnt = 0
    while cnt < len(s) and s[cnt] == ' ':
        cnt += 1
    return cnt

def main():
    srcPath = "/Users/ed/Documents/itmo/1infa/lab4/src.yaml"
    dstPath = "/Users/ed/Documents/itmo/1infa/lab4/dst_2.json"
    # open source file
    with open(srcPath, mode='r', encoding='utf-8') as rFile:
        # open the file to write
        with open(dstPath, mode='w', encoding='utf-8') as wFile:
            lines = []
            spaces = []
            for line in rFile:
                spaces += [countSpaces(line)]
                lines += [line.strip()]
            
            wFile.write("{"+parseName(lines[0])+":")
            for i in range(1, len(lines)):
                name = parseName(lines[i])
                val = parseVal(lines[i])
                if spaces[i] == 2: # 2 spaces    
                    if lines[i][0]=='-' and spaces[i-1]==2: # open list
                        wFile.write("[\n    {"+name+": "+val)
                    elif lines[i][0]=='-':  # continue list
                        wFile.write("},\n    {"+name+": "+val)
                    else: # day
                        wFile.write("\n  {"+name+":")
                else: # 4 spaces
                    wFile.write(",\n    "+name+": "+val)
            wFile.write("}]\n  }\n}")

if __name__ == "__main__":
    dstPath = "/Users/ed/Documents/itmo/1infa/lab4/lab4_3.txt"
    with open(dstPath, mode='a', encoding='utf-8') as wFile:
        start_time = time.time()
        main()
        d = (time.time() - start_time) * 1000
        wFile.write("lab4_2.py: %s (seconds*1000)\n" % d)