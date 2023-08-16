# Configuration Maker [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/Pr1meSuspec7/cfg-maker)

This script helps engineers to create a lot of configuration files start from an excel file.


### Requirements

This script tested on Linux/Windows with python3.7 or higher.  
The following packages are required:
 - numpy
 - pandas
 - xlrd
 - termcolor

It's recommended to crate a virtual environment, activate it and then install the packages:

For Windows:

```sh
> git clone https://github.com/Pr1meSuspec7/cfg-maker.git
> cd cfg-maker
> python -m venv VENV-NAME
> VENV-NAME\Scripts\activate.bat
> pip install -r requirements.txt
```

For Linux:

```sh
$ git clone https://github.com/Pr1meSuspec7/cfg-maker.git
$ cd cfg-maker
$ python -m venv VENV-NAME
$ source VENV-NAME/bin/activate
$ pip install -r requirements.txt
```
>NOTE: chose a name for virtual environment and replace the `VENV-NAME` string


### How it works

You need to create two files:
 - ***Excel file*** that contains parameters that must change in the configurations
 - ***Text file*** to use as a configuration template

The colums titles of the excel file and the variables of the template file must have the same strings because the script takes every row of the excel file and uses the values for replace every variables in the template file. Each row represents one different configuration file and his filename will be the 'HOSTNAME' field of the excel file.
New files will be stored in a new folder called "configurations" that is create in to working path.

Example excel file:

HOSTNAME | GIGABIT00   | GIGABIT01
-------- | ----------- | ---------
ROUTER1  | 192.168.1.1 | 10.0.1.1
ROUTER2  | 192.168.2.1 | 10.0.2.1
ROUTER3  | 192.168.3.1 | 10.0.3.1

Example template file:

	hostname NOMEHOST 
		
	interface GigabitEthernet0/0
	 no shut
	 ip address GIGABIT00 255.255.255.0
		
	interface GigabitEthernet0/1 
	 no shut
	 ip address GIGABIT01 255.255.255.0


### How to use

```sh
$ python cfg-maker.py
```

The prompt will ask you the name of excel file, sheet name in the excel and template file.
You can rename your files with the default values (**data.xlsx** for Excel file, **Sheet1** for sheet's Excel, **template.txt** for template file), or you can digit the name of your files present in to working folder.

```sh
If you want stop this script type: exit

Insert the name of the excel file [default: data.xlsx]:
Insert the name of the sheet in the excel file [default: Sheet1]:
Insert the name of the template file [default: template.txt]:
```

After run the script you'll find configuration files in to "configurations" folder.

```sh
Building configuration...
ROUTER1.cfg
ROUTER2.cfg
ROUTER3.cfg

!!! CONFIGURATIONS COMPLETED !!!

Check the folder --> /home/user/cfg-maker/configurations
```

Check configuration files, you can see the variables replace with table values:

```sh
$ cat /home/user/cfg-maker/configurations/ROUTER1.cfg

hostname ROUTER1 
	
interface GigabitEthernet0/0
 no shut
 ip address 192.168.1.1 255.255.255.0
	
interface GigabitEthernet0/1 
 no shut
 ip address 10.0.1.1 255.255.255.0
'''
