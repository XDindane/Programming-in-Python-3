#!/usr/bin/env python3

import sys

def main():
    maxwidth = 100 # max char in cell
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
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()

# separated logic
def print_start():
    print("<table border='1'>")

# separated logic
def print_end():
    print("</table>")

# cannot use split functions. Because commas can be in string.
def print_line(line, color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field: # if empty
            print("<td></td>")
        else:
            number = field.replace(",","")
            try:
                x = float(number) #pokud máme uzavřený řetězec, zkusíme přetypovat abychom zjistili jestli se jedná hodnotu uzavřenou do uvozovek
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError: # copy array
                field = field.title()
                field = field.replace(" A ", " a ")
                if len(field) <= maxwidth: # if length is less than max or cut it
                    field = escape_html(field)
                else:
                    field = "{0} ...".format(escape_html(field[:maxwidth]))
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

def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text
main()


    
