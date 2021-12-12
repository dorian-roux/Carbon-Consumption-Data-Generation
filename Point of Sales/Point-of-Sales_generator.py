#######################################
#   Point of Sales - Data Generator   #
#######################################


#####################
#  Import Packages  #
#####################

from geopy.geocoders import Nominatim
import time
import pandas as pd
import time
import os
import numpy as np

data_path = "Data/" #Set the initial data_path
ini_time = time.time() #Set the initial time of the execution



###############
#  Functions  #
###############

#Function that create a folder in the corresponding path (if it does not exists)
def create_folder(path):
    path_splt = path.split("/")
    curr_path = "" 
    for idx in range(len(path_splt)):  
        curr_path += path_splt[idx] + "/"   
        try:
            os.mkdir(curr_path)
        except:
            pass
    
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


#Function that append the values to the corresponding dictionnary keys
def append_dict(data_dict, lst_key, lst_value):
    for key, val in zip(lst_key, lst_value): #Iterate for each key and value
        data_dict[key].append(val) #Append the value to the corresponding key
    return data_dict


#Functon that generate Point of Sales for a compnay
def pos_generator_industry(cities, industry, industry_type, count_limit):
    temp_dict = {"Country":[], "City":[], "Population":[], "Latitude":[], "Longitude":[], "Company":[], "Type":[]} #Define an temporary empty dictionnary
    start_time = time.time() #Set the Initial Time
    count = 0 #Set the initial Counter
    for city, country, popul in zip(cities.city, cities.country, cities.population): #Iterate for each city from each country within the city dataset
        if count > count_limit: #Check whether the number of generated Point of Sale is higher than the setted up Limit
            break #Break the loop
        else:
            try:
                geolocator_city = Nominatim(user_agent="my_request") #Make an instance of Nominatim Class
                loc= industry + "," + city #Define the Location String
                location = geolocator_city.geocode(loc) #Apply the Geocode Method to get the Point of Sale Location
                
                #Append the information of the current located Point of Sale
                lst_values = [country, city, popul, location.latitude, location.longitude, industry, industry_type]
                append_dict(temp_dict, list(temp_dict.keys()), lst_values)
        
                #Reset the Initial Computation Time and incremente the Counter
                start_time = time.time()
                count +=1
                
            except Exception:
                if  time.time() - start_time > 60: #Check that no PoS were added since the last 60 seconds
                    break #Break the loop
                else:
                    pass
        
    #Manage dictionnary
    dict_company = str(industry) #Define a dictionnary name
    globals()[dict_company] = temp_dict #Set the dictionnary name as the PoS dictionnary (!Not Useful)
    lst_dict_company.append(dict_company) #Append the dictionarry name into the corresponding list
    lst_dict.append(globals()[dict_company]) #Append the dictionnary into the corresponding list
    
    #Iterate for each key of the general dictionnary 
    for k in list(pos_dict.keys()):
        pos_dict[k].extend([val for val in temp_dict.get(k)]) #Extend the general dictionnary with the newly created one
            
            
#Functon that generate Point of Sales for multiple companies
def pos_generator_industries(cities, industries, industries_type, count_limit):
    for comp, type in zip(industries, industries_type): #Iterate for each company
        pos_generator_industry(cities, comp, type, count_limit) #Perform the PoS Generator Functon for a company 
         
                
#Function that generalize the Point of Sales Generator Functions   
def pos_generator(cities, comp, type, pos_count):
    global pos_dict, lst_dict, lst_dict_company #Globalize some variables (such as dict, lists)
    if isinstance(pos_count, list): #Check whether the counter is a list
        pass
    else: #If not
        pos_count = [pos_count] #Transform the variable into a list
        
    for count_limit in pos_count: #Iterate for each counter
        if isinstance(comp, str) and isinstance(type, str): #Check whether there is a single company 
            pos_generator_industry(cities, comp, type, count_limit) #Perform the PoS Generator Functon for a company 
            
        elif isinstance(comp, list) and isinstance(type, list): #Check whether there are multiple companies 
            pos_generator_industries(cities, comp, type, count_limit) #Perform the PoS Generator Functon for multiple companies 
        else: #In case the format is not correct
            pass #Pass
            
        
                                
###########################
#   Initial Information   #
###########################

#Read the Worlcities Dataset (https://simplemaps.com/data/world-cities, Creative Commons Attribution 4.0)
wcities = pd.read_csv('Data/worldcities.csv')
wcities = wcities[['city', 'lat', 'lng', 'country', 'population']] #Keep only the useful columns
cities_h50k = wcities[wcities.population >= 50000] #Keep cities that have over 50,000 inhabithants

#Define lists of companies from different sectors and corresponding sectors
dict_company = dict({
    "Mode":["Nike", "Zara"],  
    "Cosmetic":["Sephora", "MAC Cosmetics"],  
    "Luxury":["Cartier", "Prada"], 
    "Car":["Volkswagen", "Renault"],  
    "Tech":["Apple", "Orange"]  
})

company_name, company_type = [], []
for key, val in zip(dict_company.keys(), dict_company.values()):
    company_name.extend(val)
    company_type.extend([key] * len(val))
 
#######################################
#   Generate Point of Sales Dataset   #
#######################################

#Create a dictionnary of all the information
pos_dict = dict({"Country":[], "City":[], "Population":[], "Latitude":[], "Longitude":[], "Company":[], "Type":[]}) #Set general PoS dictionnary
lst_dict, lst_dict_company = [], [] #Set empty lists
pos_count = 15 #Set a PoS Count Limit
pos_generator(cities_h50k, company_name, company_type, pos_count) #Perform the PoS generalized generator

#Create all sub-Dataframes from the List of Dictionnaries
for company_name, company_dict in zip(lst_dict_company, lst_dict): #Iterate over the companies list and companies PoS dictionnary
    
    db_company = 'pos_{}'.format(company_name) #Set a dataframe company name
    data_subtypepath = data_path + 'SubData/' + np.unique(company_dict['Type'])[0] #Set the company type path
    data_subpath = data_subtypepath + "/" + company_name #Set the company path
    create_folder(data_subpath) #Execute the folder(s) creation
    sub_dataframe = pd.DataFrame.from_dict(company_dict) #Build the company dataframe from the company dictionnary 
    data_csv_path = data_subpath + "/" + db_company + ".csv" #Set the company dataframe (.csv) path
    
    #Check Existing File
    if os.path.exists(data_csv_path): #Check whether the file (.csv) path exists
        temp_data = pd.read_csv(data_csv_path) #If so, open the file
        if len(temp_data) > len(sub_dataframe): #Check whether the existing file has a higher length than the generated one
            data_csv_path.replace('.csv', '_{}PoS.csv'.format(len(sub_dataframe))) #If so, replace the generated dataframe file path (displaying its length)
        else:
            new_path = data_csv_path #If not, modify the path of the existing file and save it
            temp_data.to_csv(new_path.replace('.csv', '_{}PoS.csv'.format(len(temp_data)))) 
    else:
        pass #If the file does not exist, pass
    sub_dataframe.to_csv(data_csv_path) #Save the generated dataframe in its corresponding path


#Create the General PoS Dataframe from the PoS Dictionnary
pos_db = pd.DataFrame.from_dict(pos_dict)
print(len(pos_db))
print(pos_db.head())

#Export the Dataframe to CSV
pos_db.to_csv(data_path + "pos_db.csv")



###################
#   End Program   #
###################

exec_time = round(time.time() - ini_time)
print("Program Execution Time:", (convert_time(exec_time)))