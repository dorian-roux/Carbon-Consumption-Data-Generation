######################################
#   Point of Sales - Example of Use  #
######################################

#####################
#  Import Packages  #
#####################

from PoS_class import PoS #Import the Point of Sales Class from the corresponding Python File
import pandas as pd
import time
import pathlib

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

wcities_path = pd.read_csv('Point of Sales/Data/worldcities.csv') #Read the World Cities Dataset
pos_exc = PoS(wcities_path) #Call the PoS Class
pos_exc.citydf = pos_exc.citydf[['city', 'lat', 'lng', 'country', 'population']] #Filter the World Cities Dataset within the PoS Call
pos_exc.citydf = pos_exc.citydf[pos_exc.citydf.population >= 50000]

#############
# Example 1 #

pos_exc.count_limit = 10 #Set the Count Limit
comp = "Nike" #Set the Company(ies)
comp_type = "Mode" #Set the Company Type
pos_exc.pos_generator(comp, comp_type, pos_exc.count_limit) 
print(pos_exc.posdf.sample(5)) #Display a sample of the DataFrame

#############
# Example 2 #

pos_exc.reset_posdf()
pos_exc.count_limit = 5 #Set the Count Limit
comp = ["Nike", "Adidas", "Sephora"] #Set the Companies
comp_type = ["Mode", "Mode", "Cosmetic"] #Set the Companies Type
pos_exc.pos_generator(comp, comp_type, pos_exc.count_limit) 
print(pos_exc.posdf.sample(10)) #Display a sample of the DataFrame


###################
#   End Program   #
###################

exec_time = round(time.time() - ini_time) # ~20s
print("Program Execution Time:", (convert_time(exec_time)))