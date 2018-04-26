#setting up the folder structure
import os


relative_folder = raw_input("Where do you want to set up the whole export utility?\nEnter the absolute path(for eg, C:/Users/BKulkarni/Documents):\n")

migration_folder_path = relative_folder+"/Migration"
codes_file_path = relative_folder+"/Migration/Codes/"
export_file_path = relative_folder+"/Migration/Export_files/"
log_file_path = relative_folder+"/Migration/Log_files/"
temporary_file_path = relative_folder+"/Migration/Temporary_files/"
import_control_file_path = relative_folder+"/Migration/Import_control_files/"

migration_file = migration_folder_path+"/export_path.txt"

if not os.path.exists(migration_folder_path):
    os.makedirs(migration_folder_path)

if not os.path.exists(codes_file_path):
    os.makedirs(codes_file_path)

if not os.path.exists(export_file_path):
    os.makedirs(export_file_path)

if not os.path.exists(log_file_path):
    os.makedirs(log_file_path)

if not os.path.exists(temporary_file_path):
    os.makedirs(temporary_file_path)

if not os.path.exists(import_control_file_path):
    os.makedirs(import_control_file_path)
	
os.chdir(migration_folder_path)
print("The folder structure is created at this path - "+os.getcwd())

f = open(codes_file_path+"path_of_export.txt","w+")
f.write(relative_folder)
f.close()