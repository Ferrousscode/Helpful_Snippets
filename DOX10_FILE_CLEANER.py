
import os

def cleanfile(file, target):
    listone = [] #Temporary, holding lines in file
    listtwo = [] #Refined (strange letters converted or deleted)
    for i in file:
        listone.append(i)


    listitem = "" #Temporary string, appended to listtwo
    for i in listone:
        for c in i:
            if c == '\x9b':
                listitem += "ø"
            elif c == '\x8f':
                listitem += "Å"
            elif c == '\x86':
                listitem += "å"
            elif c == '\x9d':
                listitem += "Ø"
            elif c == "Ä" or c == "Â" or c == "Á":
                listitem += "-"
            elif c == "³" or c == "Å" or c == "Ã" or c == "¿" or c == "´" or c == "Ú" or c == "À" or c == "Ù":
                listitem += "|"
            elif c == "":
                listitem += "Æ"
            elif c == '\x91':
                listitem += "æ"
            else:
                listitem += c
        listtwo.append(listitem)
        listitem = ""

    #From here, all strange letters is already converted or deleted,
    #further down we iterate to refine more, by removing spaces and newlines.

    listitem = ""  #Another temporary string to hold list items, appended to listthree.
    listthree = [] #Another new list, cleaner.

    #Iterating list two and removing new lines and spaces, compressing it further.
    for i in listtwo:
        for c in i:
            if c != '\n':
                listitem += c

        listthree.append(listitem)
        listitem = ""


    t = open(targetfiles + "\\" + target, "w")#, encoding='unicode_escape'

    listthree[0] = "STASJON: " + str(target) #Replacing weird chars on top with filename(station_name).

    docinfo = []

    for i in listthree:
        if len(i) > 120 and len(docinfo) < 10:
            docinfo.append(i)

    for i in docinfo:
        t.write(str(i))
        t.write('\n')


    for i in listthree:
        #print(i)
        if len(i) > 11 and len(i) < 120:
            t.write(str(i))
            t.write('\n')
        if len(i) > 120:
            t.write('\n')

    for i in docinfo:
        print(i)

    docinfo.clear()

    t.close()
    print("writing..")

directory = os.getcwd()
doxfiles = directory + '\\' + "DOX10RAWIO"
targetfiles = directory + '\\' + "DOX10CLEAN"
files = os.listdir(doxfiles)

for i in files:
    if ".txt" in i or ".TXT" in i:
        f = open(doxfiles + "\\" + str(i), "r",  encoding='unicode_escape')
        cleanfile(f,i)
        f.close()

print("done")

#f = open(doxfiles + "\\ELV" + ".txt", "r",  encoding='unicode_escape')
