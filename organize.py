'''
Created on Dec 26, 2019

@author: marcoshung
'''
import os
from pathlib import Path
from posix import getcwd
directories = {"Documents" : [".pdf", ".txt",".doc", ".xlsx", ".docx"],
               "Images" : [".jpg", ".jpeg", ".png"],
               "Videos" : [".mp4", ".mov", ".flv"],
               "DO NOT CHANGE" : [".py", ".java"],
               }

def getDirectory(string):
    for category, suffixes in directories.items():
        for suffix in suffixes:
            if(suffix == string):
                return category
            
    return "MISC"
def organizeDirectory():
    for item in os.scandir():
        filePath = Path(item)
        if(filePath.is_dir()):
            continue
        fileType = filePath.suffix.lower()
        directory = getDirectory(fileType)
        if(directory == "DO NOT CHANGE"):
            continue
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
    
def organizeDocuments():
    print(getcwd())
    os.chdir('Documents')
    path = getcwd()
    for item in os.scandir():
        filePath = Path(item)
        if(filePath.is_dir()):
            continue
        directory = ""
        if(filePath.name.lower().__contains__("cover letter")):
            directory += "Job Apps/Cover Letter"
        elif(filePath.name.lower().__contains__("resume")):
            directory += "Job Apps/Resumes"
        else:
            directory += "Misc."
        directoryPath = Path(directory)
        filePath.rename(directoryPath.joinpath(filePath))
    for item in os.scandir():
        print(item.name)
        
organizeDirectory()
organizeDocuments()