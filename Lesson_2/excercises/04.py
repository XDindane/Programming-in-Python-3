#!/usr/bin/env python3


# usage from terminal: ./csv2html.py < input csv_file > output html_file


import sys
import xml.sax.saxutils

def main():
    maxwidth, format = process_options()

    if maxwidth is not None:
        print_start()
        count = 0
        while True: # loops over all line of input and sets color of each line
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, format)
                count += 1
            except EOFError:
                break
        print_end()


def process_options():
    maxwidth_arg = "maxwidth="
    format_arg = "format="
    maxwidth = 100
    format = ".0f"
    for arg in sys.argv[1:]:
        if arg in ["-h", "--help"]:
            print("""\
použití:
csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html

Parametr maxwidth je volitelné celé číslo; 
je-li zadáno, nastaví maximum počet znaků, 
které lze vypsat u řetězcových polí,
jinak se tato pole ořežou na {0} znaků.

Parametr format je formát pro čísla; 
není-li zadán, použije se "{1}".""".format(maxwidth, format))
            return None, None
        elif arg.startswith(maxwidth_arg):
            try:
                maxwidth = int(arg[len(maxwidth_arg):])
            except ValueError:
                pass
        elif arg.startswith(format_arg):
            format = arg[len(format_arg):]
    return maxwidth, format

# separated logic
def print_start():
    print("<table border='1'>")

# separated logic
def print_end():
    print("</table>")

# cannot use split functions. Because commas can be in string.
def print_line(line, color, maxwidth, format):
    print("<tr bgcolor='{0}'>".format(color))
    numberFormat = "<td align='right'>{{0:{0}}}</td>".format(format)
    fields = extract_fields(line)
    for field in fields:
        if not field: # if empty
            print("<td></td>")
        else:
            number = field.replace(",","")
            try:
                x = float(number) #pokud máme uzavřený řetězec, zkusíme přetypovat abychom zjistili jestli se jedná hodnotu uzavřenou do uvozovek
                print(numberFormat.format(round(x)))
            except ValueError: # copy array
                field = field.title()
                field = field.replace(" A ", " a ")
                if len(field) <= maxwidth: # if length is less than max or cut it
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start string closed to quotas
                quote = c
            elif quote == c: # end string closed to quotas
                quote = None
            else:
                field += c
            continue
        if quote is None and c == ",": # end of array
            fields.append(field)
            field = ""
        else:
            field += c # array accumulation
    if field:
        fields.append(field) # adding last array
    return fields

main()
