import os
import shutil
from shutil import *
from func_utility import *
import multiprocessing
from playsound import playsound

def save_to_directory(path,user_id):
    if(os.path.isdir('songs/{}/'.format(user_id))):
        folderPath = (os.getcwd() + "/songs/{}/".format(user_id)) #to get the path of the folder
    else:
        os.mkdir('songs/{}/'.format(user_id))
        folderPath = (os.getcwd() + "/songs/{}/".format(user_id)) #to get the path of the folder
    shutil.copy(path, folderPath)


def make_list(user_id):
    db_songs= get_songs(user_id)
    print(db_songs)
    folderPath = (os.getcwd() + "/songs/{}/".format(user_id))
    for i in db_songs:
        if os.path.isfile(os.getcwd() + "/songs/{}/{}".format(user_id,i.split("/")[4])):
            pass
        else:
            shutil.copy(i,folderPath)
    temp=[]
    for i in db_songs:
        temp.append(i.split("/")[4])

    for i in os.listdir("songs/{}/".format(user_id)):
        if i not in temp:
            os.remove("songs/{}/{}".format(user_id,i))

    songs=os.listdir("songs/{}/".format(user_id))
    return songs


    
class Play:
    p=None
    # def __init__(self,flag,song):
    #     self.flag=flag
    #     self.song=song

    #     print(song)
    #     print(flag)

    #     if(flag):
    #         self.play()
    #     else:
    #         self.pause()
    @staticmethod
    def trigger(*args):
        for i in args:
            print(i)
        if(len(args)!=0):
            Play.p = multiprocessing.Process(target=playsound, args=("songs/{}/{}".format(args[0],args[1]),))
            Play.p.start() 
        else:
            Play.p.terminate()

    