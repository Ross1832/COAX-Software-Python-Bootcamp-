import urllib.request
import os
import shutil


def tiktok_to_gif(tiktok):
    urllib.request.urlretrieve(tiktok, 'TikTok-example-1.gif')
    source = f"/home/{os.getlogin()}/PycharmProjects/COAX Software_Python Bootcamp/TikTok-example-1.gif"
    dest = f"/home/{os.getlogin()}/Videos"
    try:
        shutil.move(source, dest)
    except:
        print("The file with the same name already exists\n")
        decision = input('Do you want to rename your gif name y/n\n')
        if decision == 'y':
            old = "TikTok-example-1.gif"
            new = input("please write the name of the file\n")
            new += ".gif"
            print(new)
            os.replace(old, new)
            source = f"/home/{os.getlogin()}/PycharmProjects/COAX Software_Python Bootcamp/{new}"
            shutil.move(source, dest)
        else:
            print("File was not renamed")


link = input("Provide please the link to the TikTok video\n")
tiktok_to_gif(link)
