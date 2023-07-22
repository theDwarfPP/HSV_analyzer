import os

rootpath = 'D:\\shanghai_resized'
filelist = os.listdir(rootpath)
for filename in filelist:
    path1 = rootpath + os.sep + filename
    for filename2 in os.listdir(path1):
        path2 = path1 + os.sep + filename2
        i = 1
        for photoname in os.listdir(path2):
            oldname = path2 + os.sep + photoname
            newname = path2 + os.sep + str(i) + '.' + photoname.split('.')[-1]
            os.rename(oldname,newname)
            i += 1

