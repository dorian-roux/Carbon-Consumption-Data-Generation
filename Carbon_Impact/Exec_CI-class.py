#####################################
#   Carbon Impact - Example of Use  #
#####################################

#####################
#  Import Packages  #
#####################

from CI_class import CI_Generator #Import the Point of Sales Class from the corresponding Python File
import pandas as pd
import time
import pathlib
import datetime

ini_time = time.time() #Set the initial time of the execution
script_abspath = pathlib.Path(__file__).parent.absolute() #Define the absolute path of the .py script
data_abspath = script_abspath.joinpath(pathlib.Path("Data")) #Define the absolute path of the Data folder 

###############
#  Functions  #
###############

#Function that convert a time (in seconds) into hours, minutes and seconds
def convert_time(time_sec):
    hour, minute = 3600, 60
    n_hours, remainder = divmod(time_sec, hour)
    n_minutes, seconds = divmod(remainder, minute)
    
    if n_hours == 0 and n_minutes == 0:
        string_time = "%s seconds" % (seconds)
    elif n_hours == 0 and n_minutes != 0:
        string_time = "%smin " % (n_minutes) + "%ss" % (seconds)
    else:
        string_time = "%sh " % (n_hours) + "%smin " % (n_minutes) + "%ss" % (seconds)

    return string_time


###############
#  Execution  #
###############

apps_footprints = pd.read_csv(data_abspath.joinpath(pathlib.Path("apps.csv")), delimiter=";")  #Read the Aops Dataset
CIG = CI_Generator(apps_footprints)

#1 - Check the Settings
print("Settings:", CIG.setting)

#2 - Check the Existing Role
print("Employees Roles:", CIG.empl_roles_info)

#3.1 - Add a Role
CIG.manage_role("Add", "Data Analyst", 0.5, 0.6)
print("New Data Analyst Role:", CIG.empl_roles_info)

#3.2 - Modify a Role
CIG.manage_role("Modify", "Data Analyst", 0.3)
print("Modify Data Analyst Role:", CIG.empl_roles_info)

#3.3 - Remove a Role
CIG.manage_role("Remove", "Data Analyst")
print("Remove Data Analyst Role:", CIG.empl_roles_info)

#4.1 - Set the Initial and End Date
CIG.initial_date = datetime.datetime(2021,1,1)
CIG.end_date = datetime.datetime(2021,3,1)

#4.2 - Set the Initial Number of Employees
CIG.empl = 5


## Perform the Data Generation
CIG.Generation()
print(len(CIG.generator), CIG.generator.sample(10))

## Perform the Viz
# CIG.Produce_Viz()


###################
#   End Program   #
###################

exec_time = round(time.time() - ini_time) # ~20s
print("Program Execution Time:", (convert_time(exec_time)))