#!/usr/bin/env python3

# nice method
def extract_from_tag(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer, start)
        return line[start:j]
    except ValueError:
        return None


# ugly method
def extract_from_tag_alternative(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    i = line.find(opener)
    if i != -1:
        start = i + len(opener)
        j= line.find(closer, start)
        if j != -1:
            return line[start:j]
    return None
        
print(extract_from_tag("red", "a beautifull <red>rose</red>"))
print(extract_from_tag_alternative("red", "beautifull <red>rose</red>"))

# ------------------------ partition
s = "usr/local/bin/firefox"

# nice
result = s.rpartition("/")
print(result)

# alternative and ugly
i = s.rfind("/")
if i == -1:
    result = "", "", s
else:
    result = s[:i], s[i], s[i + 1:] 
print(result)


# ----------------------- strip
s = "\t no-parking "
print(s.lstrip(), s.rstrip(), s.strip())

print("<[without brackets]>".strip("[]()<>"))

# ---------------------- split

record = "Lev N. Tolstoj*28.8.1828*20.11.1910"

fields = record.split("*")
print(fields)

born = fields[1].split(".")[2]
died = fields[2].split(".")[2]
print("lived for ", int(died) - int(born), " years")


# ------------------------ maketrans, translate

table = "".maketrans(
    "\N{bengali digit zero}"
    "\N{bengali digit one}"
    "\N{bengali digit two}"
    "\N{bengali digit three}"
    "\N{bengali digit four}"
    "\N{bengali digit five}"
    "\N{bengali digit six}"
    "\N{bengali digit seven}"
    "\N{bengali digit eight}"
    "\N{bengali digit nine}" , "0123456789")

print("20749".translate(table)) # 20749
print(
    "\N{bengali digit two}07\N{bengali digit four}\N{bengali digit nine}".translate(table)) # 20749





      
