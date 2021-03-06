import shutil
import os
import time

#Getting into the Downloads folder.
# print(os.environ)
#os.chdir(os.environ['HOME']+'/Downloads')

os.chdir('C://Users//roshan.bagdiya//Downloads')
#Creating lists for the file-types.
vids = ['.mp4','.mkv','.avi','.mpg','.mov','.wmv']
pics = ['.gif','.jpg','.png']
sounds = ['.aac', '.mp3','.wma' ,'.wav','.json','.txt']
compressed = ['.zip','.rar','.tar','.tar.gz','.tgz','.bz','.z','.tgz','.tar.bz2']
books = ['.pdf','.epub','docx','doc','pptx','ppt']
ExcelCsv = ['.xlsx','.xls','.csv']
others = ['.html','.py','.exe']
fileTypes = [vids,pics,sounds,compressed,books,ExcelCsv,others]

#Lists for putting the correct files in.
vidsList = []
picsList = []
soundsList = []
compressedList = []
booksList = []
ExcelCsvList =[]
othersList=[]
lists = [vidsList,picsList,soundsList,compressedList,booksList,ExcelCsvList,othersList]



#Creating directories if necessary.
def Directories(Type):
    if os.path.isdir(Type):
        print "-Directory '%s' already exists." % Type
    else:
        print "Creating directory '%s'..." % Type
        os.mkdir(Type)

#Getting the files.
def getFiles(Type,List):
    for file in os.listdir(os.getcwd()):
        for item in Type:
            if file.endswith(item):
                List.append(file)

#Showing and moving the files.
def Move(List,folder):
    moved = 0
    for item in List:
        print "Moving %r to %r..." % (item,folder)
        shutil.move(item,folder)
        time.sleep(0.1)
        moved += 1
    if moved == 0:
        print "No items needed to be moved."
        time.sleep(3)
    else:
        pass
def Final():
    folders = ['Vids','Pics','Sounds','Compressed','Books','ExcelCsv','others']
    for i in range(len(folders)):
        Directories(folders[i])
        getFiles(fileTypes[i],lists[i])
        Move(lists[i],folders[i])
Final()