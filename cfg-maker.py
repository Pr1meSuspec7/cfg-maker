import os
from re import sub
from termcolor import colored
import pandas as pd
import platform

# Activate color output for Windows cmd
if platform.system() == 'Windows':
    os.system('color')


# Global variables
print('\n')
print('*********************************************************************************')
print('*********************************************************************************')
print('***                                                                           ***')
print('*** This script use an excel file with a template for generate configurations ***')
print('***                                                                           ***')
print('*********************************************************************************')
print('*********************************************************************************')
print('\n')
print(colored('If you want stop this script type:'), colored('exit', 'yellow'))
print('\n')
excelfile = str(input('Insert the name of the excel file [default: data.xlsx]:'))
if excelfile == 'exit':
    print(colored('Cancel by the user.', 'yellow'))
    quit()
elif not excelfile:
    excelfile = 'data.xlsx'
excelsheet = str(input('Insert the name of the sheet in the excel file [default: Sheet1]:'))
if excelsheet == 'exit':
    print(colored('Cancel by the user.', 'yellow'))
    quit()
elif not excelsheet:
    excelsheet = 'Sheet1'
templatebase = str(input('Insert the name of the template file [default: template.txt]:'))
if templatebase == 'exit':
    print(colored('Cancel by the user.', 'yellow'))
    quit()
elif not templatebase:
    templatebase = 'template.txt'


# Functions that check if files or sheet exist
def file_exist(files):
    if not os.path.isfile(files):
        print(colored("\nERROR ---> No such file or directory: " + files, 'red'))
        quit()

def sheet_exist(sheetname):
    try:
        xl.parse(sheetname)
    except:
        print(colored('\nThis sheet not exist: ' + sheetname, 'red'))
        quit()

# Check if files and sheet exist
files = [excelfile, templatebase]
for i in files:
    file_exist(i)

xl = pd.ExcelFile(excelfile)
sheet_exist(excelsheet)


# If not exist create new folder called "configurations" into working path
cwd = os.getcwd()
conf_folder = cwd + '/configurations'

if not os.path.exists(conf_folder):
    os.mkdir(conf_folder)
else:
    print(colored('\nFolder "configurations" already exist.\n', 'yellow'))


# Load the excel file, template file and extracts dictonary keys from columns of excel file
os.chdir(cwd)
xls = pd.read_excel(excelfile, sheet_name=excelsheet)
txt = open(templatebase, 'r+').read()
dictkeys = list(xls.columns)


# Function to replace template variables with excel sheet values 
def replace_content(dictionary, file):
    for dictionarykey, dictionaryvalue in list(dictionary.items()):
        file = sub(dictionarykey, str(dictionaryvalue), file)
    return file


# Function to create the target file using the HOSTNAME value of the excel sheet
def destfile(filename, filemodify):
    filecfg = filename + str('.cfg')
    newfile = open(filecfg, 'w')
    newfile.write(filemodify)
    newfile.close()
    print(filecfg)


# Function to write the conf file inside the new folder
def conf_creation():
    os.chdir(conf_folder)
    for index, row in xls.iterrows():
       routerparam = row.tolist()
       hostname = routerparam[0]
       dic = dict(zip(dictkeys, routerparam))
       result = replace_content(dic, txt)
       destfile(hostname, result)


# Main function
def main():
    print('\nBuilding configuration...')
    conf_creation()

    print(colored('\n!!! CONFIGURATIONS COMPLETED !!!\n', 'green'))
    print(colored('Check the folder --> ' + conf_folder, 'yellow'))


if __name__ == "__main__":
    main()
