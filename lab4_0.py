import time

def isInt(s: str):
    toCheck = True
    try:
        int(s)
    except ValueError:
        toCheck = False
    return toCheck
def isBool(s: str):
    if s=="true" or s=="True" or s=="false" or s=="False":
        return True
    return False
def parseVal(s: str):
    i = 0
    while i < len(s) and s[i] != ':':
        i += 1
    i += 2
    if i < len(s):
        val = s[i:]
        if isInt(val) or isBool(val):
            return val
        return '"' + val + '"'
    return ""
def parseName(s: str):
    i = 0
    while i < len(s) and s[i] != ':':
        i += 1
    if s[:2] == "- ":
        return '"' + s[2:i] + '"'
    return '"' + s[:i] + '"'
def countSpaces(s: str):
    cnt = 0
    while cnt < len(s) and s[cnt] == ' ':
        cnt += 1
    return cnt

def main():
    srcPath = "/Users/ed/Documents/itmo/1infa/lab4/src.yaml"
    dstPath = "/Users/ed/Documents/itmo/1infa/lab4/dst_0.json"
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
                if spaces[i] == 2:  # 2 spaces    
                    if lines[i][0]=='-' and spaces[i-1]==2: # open list
                        wFile.write("[\n    {"+name+": "+val)
                    elif lines[i][0]=='-':  # continue list
                        wFile.write("},\n    {"+name+": "+val)
                    else:   # day
                        wFile.write("\n  {"+name+":")
                else:   # 4 spaces
                    wFile.write(",\n    "+name+": "+val)
            wFile.write("}]\n  }\n}")

if __name__ == "__main__":
    dstPath = "/Users/ed/Documents/itmo/1infa/lab4/lab4_3.txt"
    with open(dstPath, mode='w', encoding='utf-8') as wFile:
        start_time = time.time()
        main()
        d = (time.time() - start_time) * 1000
        wFile.write("lab4_0.py: %s (seconds*1000)\n" % d)