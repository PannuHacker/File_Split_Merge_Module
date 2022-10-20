import os,time
from filesplit.split import Split
from filesplit.merge import Merge

class fileSplitMergeModule(object):
    def __init__(self):
        ##spliting Constents
        self.Split_Input_Dir = "/Users/devops/Desktop/DCIM/Camera01/exp/"
        self.Split_Output_Dir = "/Users/devops/Desktop/DCIM/Camera01/exp/files/"
        self.split_File_Name = "VID_20220920_102716_10_005.insv"
        self.each_File_Size = 100000000 ## it's a byte size (100 MB)
        ##meging Constents
        self.Merge_Input_Dir = "/Users/devops/Desktop/DCIM/Camera01/exp/files/"
        self.Merge_Output_Dir = "/Users/devops/Desktop/DCIM/Camera01/exp/"
        self.Merged_FileName = "mergedfile.bin"
######################################################################################################################################################################
    def cb(self,filepath: str, filesize: int):
        try:
            print(f'{filepath} : {filesize}')
        except:
            pass

######################################################################################################################################################################
    def Split(self,inFile,outDir,byteSize):
        try:
            split = Split(inFile,outDir)
            split.bysize(byteSize, includeheader=True, callback=self.cb)
            print("Spliting Finalizing")
            time.sleep(5)
            split.terminate = True
            print("Spliting Complete..")
        except Exception as err:
            print("Exception in startSpliting method :: {}".format(err))

######################################################################################################################################################################
    def Merge(self,inDir,outDir,fileName):
        try:
            merge = Merge(inputdir=inDir,outputdir=outDir,outputfilename=fileName)
            merge.merge(cleanup=True, callback=self.cb)
            print("Spliting Finalizing")
            time.sleep(5)
            merge.terminate = True
            print("Merge Complete..")  
        except Exception as err:
            print("Exception in startMerge method :: {}".format(err))

######################################################################################################################################################################
    def main(self):
        try:
            self.Split(os.path.join(self.Split_Input_Dir,self.split_File_Name),self.Split_Output_Dir,100000000)
            self.Merge(self.Merge_Input_Dir,self.Merge_Output_Dir,self.Merged_FileName)
        except Exception as err:
            print("Exception in main method :: {}".format(err))
            


if __name__ == '__main__':
    obj = fileSplitMergeModule()
    obj.main()