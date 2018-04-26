#Main program that has to be run

#Should be in the directory where this program is stored.
#python Trigger_export.py project_name application_name
#For example, python Trigger_export.py GOLD_DATA_LAKE app_GOLD_LZ
#The paths int the below program need to be changed
#if required, the domain name,model repository name, DIS name can also be passed as cmdline arguments(not yet provided)


#This program creates the export of the objects specified in the application, then creates an excel sheet so as to force the developer 
#make the necessary changes.
#After editing, 'y' or 'Y' has to be pressed and entered.
#The import_control_file will be generated using the excel data as its base.

import os,sys
import Excel_creation
import kintry
import Import_control_file_creation
import getpass


user_name = raw_input("Enter username:")
password = getpass.getpass("Enter password:")
d_name = raw_input("Choose the souce domain name:\n 1 - DEV\n 2 - QA\n 3 - PROD\n")
project_name=raw_input("Enter project name:")
application_name=raw_input("Enter application name:")
release_notes_file=raw_input("Enter release notes absolute path and name (for eg: C:\Users\BKulkarni\Pictures\DEMO1\Excel_sheets\Try.xlsx):")
domain_name = "DMN_INFA_EII_DEV"
dis_name = "DATAINT_EII_DEV"
repository_name = "MDLREP_EII_DEV"

if d_name==1:
	domain_name = "DMN_INFA_EII_DEV"
	dis_name = "DATAINT_EII_DEV"
	repository_name = "MDLREP_EII_DEV"
elif d_name==2:
	domain_name = "DMN_INFA_EII_QA"
	dis_name = "DATAINT_EII_QA"
	repository_name = "MDLREP_EII_QA"
elif d_name ==3:
	domain_name = "DMN_INFA_EII_PRD"
	dis_name = "DATAINT_EII_PRD"
	repository_name = "MDLREP_EII_PRD"

with open("path_of_export.txt","r") as f:
	relative_folder = f.read()+"/Migration"

codes_file_path = relative_folder+"/Codes/"
export_file_path = relative_folder+"/Export_files/"
log_file_path = relative_folder+"/Log_files/"
temporary_file_path = relative_folder+"/Temporary_files/"
import_control_file_path = relative_folder+"/Import_control_files/"

print("\n\nProceeding with the export.. Do not close this window.")


try:
	#path change required, path to infacmd
	os.chdir("C:/Informatica/10.2.0/clients/DeveloperClient/infacmd")
	#checking if project exists
	#listing projects
	project_exists_flag = 0
	application_exists_flag = 0
	
	print("Before proceeding ahead, please close the release notes excel workbook.")
	os.system("pause")
	
	print("Listing projects.")
	print("Checking if project exists.")
	os.system("infacmd.bat mrs ListProjects -dn "+domain_name+" -un "+user_name+" -pd "+password+" -sn "+repository_name+" > "+temporary_file_path+"projects_list.txt")
	with open(temporary_file_path+"projects_list.txt") as f:
		for line in f:
			if line.rstrip('\n')==project_name:
				print("Project exists.")
				project_exists_flag = 1
				break
		else:
			print("Project does not exist.")
	print("Listing applications.")
	print("Checking if application exists.")
	os.system("infacmd.bat dis ListApplications -dn "+domain_name+" -un "+user_name+" -pd "+password+" -sn "+dis_name+" > "+temporary_file_path+"applications_list.txt")
	with open(temporary_file_path+"applications_list.txt") as f:
		for line in f:
			if line.rstrip('\n')==application_name:
				print("Application exists.")
				application_exists_flag = 1
				break
		else:
			print("Application does not exist.")
	if project_exists_flag == 1 and application_exists_flag == 1:
		print("Preparing for export..")
		print("Exporting objects.")
		os.system("infacmd.bat oie ExportObjects -dn "+domain_name+" -un "+user_name+" -pd "+password+" -pn "+project_name+" -rs "+repository_name+" -fp "+export_file_path+project_name+".xml -ow true > "+log_file_path+project_name+"_export_output.txt")
		print("Export completed.")
		print("Export file created successfully.\n ")
		os.system("infacmd.bat dis ListApplicationObjects -dn "+domain_name+" -sn "+dis_name+" -un "+user_name+" -pd "+password+" -a "+application_name+" -lt true > "+temporary_file_path+application_name+"_list.txt")
		os.chdir(codes_file_path)
		print("Creating the excel sheet..")
		Excel_creation.scan_application_objects_list(temporary_file_path+application_name+"_list.txt",release_notes_file)	
		flag = 'n'
		print("The excel sheet has been created for your application in the release notes..")
		kintry.show_alert(application_name)
		print("Edit only the resolutions in the excel file, save it and close.\n")
		os.system("pause")
		flag = raw_input("Enter y or Y to continue and press enter. (To exit, press n/N)\n")
		if(flag=="Y" or flag=="y"):
			print("Creating the import control file..")
			Import_control_file_creation.import_control_file_creation_function(import_control_file_path+application_name,release_notes_file)
			print("The Import control file has been created.\n")
		elif(flag=="N" or flag=="n"):
			print("Exiting.")
	else:
		print("Exiting.")
except OSError as e:
	print("Unfortunately some error occured."+e)
	
	
