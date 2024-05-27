#EMIR REFID
import sys
import os
import re
import shutil
import subprocess
import gzip
from datetime import datetime,timedelta
from time import sleep
import logging

substring_to_search_retrieval = 'ACK'
current_date = datetime.now() - timedelta(days = 1)

#format DDMMYYYY
current_date_str = current_date.strftime("%d%m%Y")

current_date_ack = current_date.strftime("%Y-%m-%d")

Submission = "G://SFTP//SUB.bat"
Retrieval = "G://SFTP//ACK.bat"
'''
if len(sys.argv)!=2:
    print("Usuage: python script.py <firm>")
    logging.error("Usuage: python script.py <firm>")
firm = sys.argv[1]
'''
#if sys.argv[1] == 'AAA':
source_path = "E://Handson//EMIR//"
processed_path = "E://Handson//EMIR//Submitted/"
temp_path = "E://Handson/EMIR/ACK_NACK/temp/"
ack_path = "E://Handson/EMIR/ACK_NACK"
log_path = "E://Handson/EMIR/CFL_EMIR_REFID_SUB_ACK.log"
submission_flow = "SUB" #call property file
retrieval_flow = "ACK"
#else:
#    print("Please give valid firm name")

logging.basicConfig(filename = log_path, level=logging.INFO)


if not os.path.exists(processed_path):
    os.makedirs(processed_path)
    print(f"Temp folder not present. {processed_path} created!")

if not os.path.exists(temp_path):
    os.makedirs(temp_path)
    print(f"Temp folder not present. {temp_path} created!")

################function definitions#######################
def sub_filenames_with_string(directory,conditions):
    try:
        filenames_dict = {condition: [] for condition in conditions}
        files = os.listdir(directory)
        print(files)
        for filename in files:
            if filename.endswith(".txt"):
                for condition,substring in conditions.items():
                    if substring in filename:
                        filenames_dict[condition].append(filename)
        print(filenames_dict)
        return filenames_dict
    except FileNotFoundError:
        logging.error("Directory not found")
    except Exception as e:
        logging.error(f"Error: {e}")

def ret_file_with_substring(temp,substring):
    for file in os.listdir(temp):
        if substring in file and current_date_ack in file:
            logging.info("\n----------------SFTP ACK file found!!!------------------\n")
            return file
        
def unzip_rename_ack(sftp_ack_path,sftp_ack_file,condtion,firm):
    try:
        sftp_ack_file = os.path.join(sftp_ack_path,sftp_ack_file)
        date_stamp = datetime.now().strftime("%d%m%Y_%H%M%S")
        output_file = sftp_ack_file[:-3]
        if not os.path.exists(sftp_ack_file):
            raise FileNotFoundError (f"File '{sftp_ack_file}' not found")
        with gzip.open(sftp_ack_file,'rb') as gzip_file:
            with open(output_file,'wb') as unzip_file:
                shutil.copyfileobj(gzip_file,unzip_file)
        print(f"File saved to {output_file}")

        renamed_file = f"RFT_ACK_NACK_ESMA_{firm}_ETD_{condition}_{date_stamp}.xml"
        renamed_file_path = os.path.join(sftp_ack_path,renamed_file)
        print(renamed_file_path)
        os.rename(output_file,renamed_file_path)
    except Exception as e:
        print(f"Error: {e}")
##############################################

#declaring conditions
conditions = {
    "Position": f"Position_{current_date_str}",
    "Transaction": f"Transaction_{current_date_str}"
}

filenames_dict = sub_filenames_with_string(source_path,conditions)

if any(filenames_dict.values()):
    print("Files are present in source folder!")
    logging.info("Files are present in source folder!")
else:
    print("No files present in source folder!")
    logging.error("No files present in source folder!")

for condition,filenames in filenames_dict.items():
    #iterate through list of filenames for each category
    for filename in filenames:
        logging.info(f"\n-------File Category: {condition}---------------\n")
        logging.info(f"Processing file: {filename}")

        try:
            logging.info("\n-------------Submission started----------------")
            #submit = subprocess.run([Submission,current_date_str,submission_flow],shell=True,check=True)
            print("Submission executed")
            shutil.move(os.path.join(source_path,filename),os.path.join(processed_path,filename))
            print("File moved to processed folder successfully")
            logging.info("File moved to processed folder successfully")
            logging.info("\n------------Submission Completed-------------------\n")

        except subprocess.CalledProcessError as e:
            print("Error with submission")
            logging.error(f"Error occured with submisstion. Please check {e}")
            exit()
        sleep(3)

        ret_file_present = False
        while ret_file_present != True:
            try:
                sftp_ack_file = ret_file_with_substring(temp_path,substring_to_search_retrieval)
                if sftp_ack_file:
                    logging.info(f"{sftp_ack_file} file present in temp path!")
                    print(f"{sftp_ack_file} file present in temp path!")
                    sleep(6)
                    shutil.move(os.path.join(temp_path,sftp_ack_file),ack_path)
                    logging.info("Moved retrieved file from temp to ack folder")
                    print("Moved retrieved file from temp to ack folder")
                    #unzip and rename ack file
                    unzip_rename_ack(ack_path,sftp_ack_file,condition,"CFL")
                    break
                else:
                    logging.info("\n-------------Retrieval started----------------")
                    #retrieve = subprocess.run([Retrieval,current_date_str,retrieval_flow],shell=True,check=True)
                    #logging.info(retrieve.stdout)
                    #logging.error(retrieve.stderr)
                    print("Retrieval executed")
                logging.info("\n-----------------Retrieval Completed--------------\n")
            except subprocess.CalledProcessError as e:
                print("Error with Retrieval")
                logging.error(f"Error occured with Retrieval. Please check {e}")
            sleep(12)

print("Submission and Retrieval completed!!")
