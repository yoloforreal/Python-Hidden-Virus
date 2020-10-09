import os
from faker import *
from time import sleep

fk = Faker()

version = 1.4
os.system('clear')
print("R    U     N")
print('[1] Get description of this file')
print('[2] Check for updates (recommended)')
print('[3] Run')
option_1 = float(input("Choose an option: "))

if option_1 == 1:
    print('RUN is a file which can run multiple apps, and do things that app store cannot. For example, RUN can pay for any app you want, find credit card numbers, and find information on any app. Removes and patches limitaitons on original app store.')

if option_1 == 2:
    print('Checking for updates...')
    if version == 1.2:
        sleep(0.2)
        print("No updates found.")
        print("All is good.")
    else:
        sleep(2)
        input("Update found, would you like to update now?")
        sleep(1)
        print("Updating...")
        sleep(2)
        print('Updated Succesfully!')
        sleep(1)
        print('ERROR!')
        sleep(0.5)
        print('Virus found!')
        sleep(0.2)
        print('Strange extension running "RUN.py" and accessing files.')
        sleep(0.01)
        print('Attempting auto-delete...')
        sleep(0.01)
        print('Deleting main data...')
        sleep(1)
        print('Auto-delete failed.')
        sleep(1)
        print('Attempting to delete small data...')
        sleep(1)
        print('Success!')
        sleep(1)
        print(fk.name())
        input('Do you reconinze this person? ➣')
        sleep(1)
        print('Deleting...')
        sleep(1)
        print("Other people linked found!")
        sleep(1)
        for j in range(10):
            print(fk.name())
            sleep(0.01)
        sleep(1)
        print('Suspicious adresses found!')
        sleep(0.01)
        print('Deleting...')
        sleep(0.01)
        for k in range(10):
            print(fk.address())
            sleep(0.01)
            print(fk.text())
        print('Deleted!')
        sleep(0.05)
        os.system('clear')

if option_1 == 3:
    print('This will check your python files to see if you have anything bad or any mispelledd / bad lines in your python code.')
    sleep(5)
    print('Checking your python files...')
    sleep(2)
    print('Unable to check your files. Please do the manual alternative.')
    import start


if option_1 == 4:
    print('infected')
    sleep(0.4)
    os.system('clear')
    import start