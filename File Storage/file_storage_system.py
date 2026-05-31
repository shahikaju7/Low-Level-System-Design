from enum import Enum
import uuid
class FileType(Enum):
    IMAGE="IMAGE"
    PDF="PDF"
    DOCUMENT="DOCUMENT"

class File:
    def __init__(self,name,size,filetype,content):
        self.fileid=str(uuid.uuid4())
        self.name=name
        self.size=size
        self.filetype=filetype
        self.content=content

class Folder:
    def __init__(self,name,owner):
        self.folderid=str(uuid.uuid4())
        self.fname=name
        self.owner=owner
        self.files=[]
        self.subfolder=[]
    def addfile(self,file):
        self.files.append(file)
    def getfile(self,file):
        for f in self.files:
            if f==file:
                return f
        return None
    
class User:
    def __init__(self,name,storagelimit):
        self.uid=str(uuid.uuid4())
        self.uname=name
        self.storagelimit=storagelimit
        self.root_folder=Folder("root", self)
        self.usedstorage=0
     
    def has_space(self,size):
        return self.storagelimit>=self.usedstorage+size
    def add_storage(self,size):
        self.usedstorage+=size
        
    def free_storage(self,size):
        self.usedstorage-=size

class FolderSystem:
     def uploadfile(self,file,folder,user):
         if user.has_space(file.size):
             folder.addfile(file)
             user.add_storage(file.size)
             print(f"Your {file.name} is successfully uploaded to {folder.fname}")
         else:
             raise Exception("You Reached your storage limit")
     
     
     def download(self,file,folder):
         return folder.getfile(file)
     
     def deletefile(self,file,folder,owner):
        if folder.owner != owner:
            raise Exception("Permission denied")
        folder.files.remove(file)
        owner.free_storage(file.size)
        print(f"{file.name} successfully deleted from {folder.fname}")
         
     def searchfile(self,name,folder):
        files=folder.files
        for f in files:
            if f.name==name:
                return f
        
        raise Exception(f"No files with {name} present in {folder}")
     
     def organize_file(self,file,folder1,folder2):
        folder1.files.remove(file)
        folder2.files.append(file)
        print(f"successfully orgranized {file.name} from {folder1.fname} to {folder2.fname}")
         
         
         


c1=FolderSystem()
f1 = File("Java", 10, FileType.PDF, "abcde")
f2 = File("Flower", 1, FileType.IMAGE, "abcde")
f3 = File("Python", 5, FileType.DOCUMENT, "abcde")
U1 = User("kajal", 15)
U2 = User("Ram", 10)
NewFolder=Folder("Study",U1)

NewFolder2=Folder("Flowers",U2)


c1.uploadfile(f1,NewFolder,U1)
c1.uploadfile(f2,NewFolder,U1)
c1.download(f1,NewFolder)
c1.searchfile("Java", NewFolder)
c1.deletefile(f1,NewFolder,U1)
print("Used storage after delete:", U1.usedstorage) 

c1.organize_file(f2,NewFolder,NewFolder2)


        
            
        