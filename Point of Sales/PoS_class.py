#########################################
#   Point of Sales - Class & Functions  #
#########################################

#####################
#  Import Packages  #
#####################

from geopy.geocoders import Nominatim
import time
import pandas as pd
import time


#######################
#  Class & Functions  #
#######################

class PoS: #Define the Point of Sales Class
    
    #Initiate the Class
    def __init__(self, cities_df): 
        self.citydf = cities_df #Imported World Cities Dataset
        self.count_limit = None #Initial Count Limit
        self.posdf = pd.DataFrame.from_dict({"Country":[], "City":[], "Population":[], "Latitude":[], "Longitude":[], "Company":[], "Type":[]}) #Initial PoS Dataframe
    
    def reset_posdf(self):
        self.posdf = pd.DataFrame.from_dict({"Country":[], "City":[], "Population":[], "Latitude":[], "Longitude":[], "Company":[], "Type":[]}) #Initial PoS Dataframe

    #Append within an dictionnary
    def append_dict(self, dict, keys, values): 
        for key, val in zip(keys, values): #Iterate for each key and value
            dict[key].append(val)
        return dict
    
    #Functon that generate Point of Sales for a compnay
    def pos_generator_industry(self, company, company_type, pos_count):
        temp_dict = {"Country":[], "City":[], "Population":[], "Latitude":[], "Longitude":[], "Company":[], "Type":[]} #Define a temporary empty dictionnary
        start_time = time.time() #Set the Initial Time
        count = 0 #Set the Initial Counter
        for city, country, popul in zip(self.citydf['city'], self.citydf['country'], self.citydf['population']): #Iterate for each City from each Country within the City Dataset
            if count >= pos_count: #Check whether the Number of Generated Point of Sale is higher than the setted up Limit
                break #Break the loop
            else:
                try:
                    geolocator_city = Nominatim(user_agent="my_request") #Make an instance of Nominatim Class
                    loc= company + "," + city #Define the Location String
                    location = geolocator_city.geocode(loc) #Apply the Geocode Method to get the Point of Sale Location
                    
                    #Append the information of the current located Point of Sale
                    lst_values = [country, city, popul, location.latitude, location.longitude, company, company_type]
                    self.append_dict(temp_dict, list(temp_dict.keys()), lst_values)
            
                    #Reset the Initial Computation Time and incremente the Counter
                    start_time = time.time()
                    count +=1
                    
                except Exception:
                    if  time.time() - start_time > 20: #Check that no PoS were added since the last 60 seconds
                        break #Break the loop
                    else:
                        pass
                    
        self.posdf = self.posdf.append(pd.DataFrame.from_dict(temp_dict))
        
      
    #Functon that generate Point of Sales for multiple companies
    def pos_generator_industries(self, companies, companies_types, count_limit):
        for comp, type in zip(companies, companies_types): #Iterate for each company
            self.pos_generator_industry(comp, type, count_limit) #Perform the PoS Generator Functon for a company 
           
    #Function that generalize the Point of Sales Generator Functions   
    def pos_generator(self, comp, type, pos_count):
        if isinstance(comp, str) and isinstance(type, str): #Check whether there is a single company 
            self.pos_generator_industry(comp, type, pos_count) #Perform the PoS Generator Functon for a company    
            print("Point of Sales for Unique Company - Generated")
            
        elif isinstance(comp, list) and isinstance(type, list): #Check whether there are multiple companies 
            self.pos_generator_industries(comp, type, pos_count) #Perform the PoS Generator Functon for multiple companies 
            print("Point of Sales for Multiple Companies - Generated")

        else: #In case the format is not correct
            print("Point of Sales - Not Generated") #Pass
        
        #Drop duplicates
        self.posdf = self.posdf.drop_duplicates().reset_index(drop=True)
        
           
###################
#   End Program   #
###################