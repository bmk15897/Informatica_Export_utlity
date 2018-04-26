# Export utility

This export utility is made in order to simplify the export of objects from Informatica. It will run using Python 2.7 .

## Prerequisites

### 1. Install Python 2.7 using the .msi installer provided in the package.
- while installing, make sure that you check the add to path option. Without adding the python to path, you won't be able to use python directly.
### 2. In the cmd, change your directory to package folder, 
####	2.1 Run the program "get-pip.py" using the command-
```
python get-pip.py
```
- this will install the pip utility required to install other modules.
####	2.2 Type the following- 
```
pip install -r requirements.txt
```
- this will install all the modules required to run the export utility.
####	2.3 Run the program "folder_structure.py" using the	command-
```
python folder_structure.py
```
- give the absolute path where you want to setup the whole folder structure.
- this will create the folder structure required.
### 3. Copy the codes from the "CodesToBeCopied" folder in the package to the "Codes" folder in the folder structure.
### 4. Now you are all set to use the export utility.

## Using the export utility

### 1. Open cmd with the path of the "Codes" folder as present working directory.
### 2. Run the program "Trigger_export.py" using the command-
```
python Trigger_export.py
```
- It will take inputs such as the username,password to access Informatica.
- It also requires the project name,application name,domain name from which the objects are to be exported.
- It will also ask for the absolute path of the release notes.
- If the project and the application names are existing, the program proceeds ahead otherwise, the program stops.
- An excel sheet is added to the released notes with a new tab named as "Resolution Specification". It is expected that for each application, there will be a separate release note.
- Developers are asked to change the resolutions according to their requirements. 
- After editing, follow the instructions. At the end of the this, you will have the .xml file named by project name and the import control file btoh of which are required to import into the target environment.

## Here is an example - 

For creating the folder structure - 
```
C:\Users\BKulkarni\Desktop\Final>folder_structure.py
Where do you want to set up the whole export utility?
Enter the absolute path(for eg, C:/Users/BKulkarni/Documents):
C:\Users\BKulkarni\Pictures\DEMO2
C:\Users\BKulkarni\Pictures\DEMO2\Migration
```
For running the export - 
```
C:\Users\BKulkarni\Desktop\Final>cd C:\Users\BKulkarni\Pictures\DEMO2\Migration
C:\Users\BKulkarni\Pictures\DEMO2\Migration>cd Codes
C:\Users\BKulkarni\Pictures\DEMO2\Migration\Codes>python Trigger_export.py
Enter username:your_username
Enter password:
Choose the souce domain name:
 1 - DEV
 2 - QA
 3 - PROD
1
Enter project name:some_project
Enter application name:some_application
Enter release notes absolute path and name (for eg: C:\Users\BKulkarni\Pictures\DEMO1\Excel_sheets\Try.xlsx):C:\Users\BKulkarni\Pictures\DEMO1\Excel_sheets\Try.xlsx
Listing projects.
Checking if project exists.
Project exists.
Listing applications.
Checking if application exists.
Application exists.
Preparing for export..
Exporting objects.
Export completed.
Export file created successfully.

Creating the excel sheet..
The excel sheet has been created for your application in the release notes..
Press any key to continue . . .
Edit the excel file, save it and close.

Enter y or Y to continue and press enter. (To exit, press n/N)
y
Creating the import control file..
The Import control file has been created.