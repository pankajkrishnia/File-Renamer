import os
def makeMePretty(path,ignoreme,format):
    with open(ignoreme) as f:
        ignorefiles = f.read()
    os.chdir(path)

    # handling all other files except format files
    for i in os.listdir(path):
        if i.endswith(format) or i in ignorefiles:
            continue
        else:
            k = i.capitalize()
            os.rename(i,k)

    # handling format files
    j=1
    for i in os.listdir(path):
        if i in ignorefiles:
            continue
        elif i.endswith(format):
            os.rename(i,f"{j}{format}")
            j +=1


if __name__ == '__main__':
    path = input("Input path of the folder : ")
    ignore = "ignore.txt"
    format = ".jpg"
    makeMePretty(path,ignore,format)