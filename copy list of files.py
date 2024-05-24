#copy list of files
import shutil
import sys
from datetime import datetime,timedelta
import os

#Previous_date = sys.argv[1]
Previous_date = 16052024
#Previous_date = datetime.now() - timedelta (days=1)

file_name_list = [f"EMIR_REFID_ETD_Position_{Previous_date}.xml.txt",f"EMIR_REFID_ETD_Collateral_{Previous_date}.xml.txt",f"EMIR_REFID_ETD_Transaction_{Previous_date}.xml.txt"]

for filename in file_name_list:
    print('File name:  ',filename)
    source = r"E:\\Handson\\EMIR\\"+filename
    print("Source path: ",source)
    destination = r"E:\\Handson\\EMIR\\ACK_NACK\\"+filename
    print('Destination path: ',destination)
    shutil.copyfile(source,destination)

print("Files copied!!")

