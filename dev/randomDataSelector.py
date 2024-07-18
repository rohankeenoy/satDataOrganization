'''Author: Rohan Keenoy
A script for randomly selecting MAXAR satelite data'''
import os
import random
import pandas as pd
import json

dirPath = "dev/no_pan_3yr_65pc"
subDir = ["Coastal"]
allOverviewImages = []
catalogId = ""

#create a global pandas df

df = pd.DataFrame

def randomSelectImage():
    arrLen = len(allOverviewImages)
    generated = random.randrange(0,arrLen-1,1)
    selected = allOverviewImages[generated]
    return selected

def process_file(filePath):
    # Define your processing logic here
    if "AllOverviewImages" in filePath:
        catalogImg = os.path.basename(filePath)
        allOverviewImages.append(catalogImg)
    elif "JSONFiles" in filePath:
        #extract the JSONfile with Naming convention from catalogImageId_subDir_index
        #copy the json file with naming convention catalogImageId_subDir_index
        pass
        
        
    elif "RequestFiles" in filePath:
        #open the csv and parse data for each csv for the catalogImageID
        pass
    


#need a function for traversing the data
def traverse_the_data():
    count = 0
    index = 0
    for subdir in subDir:
        #in the subdirectory for 3 regions
        subdir_path = os.path.join(dirPath, subdir)
        print(f"Files in {subdir_path}:")
        for root, dirs, files in os.walk(subdir_path):
            filesLen = len(files)
            print(filesLen)
            for fileName in files:
                if ".tif" in fileName:
                    if count <= filesLen:
                        print(fileName)
                        filePath = os.path.join(root, fileName)
                        process_file(filePath)
                        count+=1
                    if count == filesLen:
                        catalogId = randomSelectImage()
                        catalogId = catalogId.replace(".tif", "")
                        print(f"Selected CatalogID {catalogId}")
                elif ".geojson" in fileName:
                    print("json in file name and selected file name is still: ", catalogId)
                    
                elif ".csv" in fileName:
                    print("csv in filename")
                else:
                    pass
            #resets overView array
            print(f"WIPING ARRAY OverviewImages------------------------------------ Processing for index{root} is complete")
            allOverviewImages = []
            count = 0
        
            
#Copy data to a new folder with csv info, geoJSON, for it, and image. 


if __name__ == "__main__":
    traverse_the_data()
