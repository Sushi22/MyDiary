import os
import shutil
from shutil import *
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

    