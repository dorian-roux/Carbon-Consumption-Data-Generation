########################################
#   Carbon Impact - Class & Functions  #
########################################

#####################
#  Import Packages  #
#####################

import numpy as np
import random
import pandas as pd
import seaborn as sns
import datetime
import matplotlib.pyplot as plt
import warnings
from dateutil.relativedelta import relativedelta
import string


#######################
#  Class & Functions  #
#######################

class CI_Generator: #Define the Point of Sales Class
    def __init__(self, apps_df):
        self.name = "Data Generation"
        self.app_df = apps_df #Imported World Cities Dataset

        #Begin and End Date
        self.initial_date = datetime.datetime(2021, 1, 1, 9, 0) #2021-1-1 9AM
        self.duration = (0,1,0)
        self.end_date = self.initial_date + relativedelta(year = self.duration[0], month = self.duration[1], day = self.duration[2])
        self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  #Weekdays
        self.work_hours = (9,18)
    
        #Choices
        self.empl = random.randint(5,10) #Generate X employees
        self.empl_roles_info = [("Data Scientist", 0.5, 0.75), ("Data Analyst", 0.2, 0.4), ("Community Manager", 0.2, 0.5), ("Human Resources", 0.1, 0.25)]
        self.outlier_ratio = 0.95 #5% of the data (day) are gonna be outliers
        
        #Settings
        self.setting = ["Add", "Remove", "Modify"]
        self.split_role()
        
       
    def split_role(self):
        lst_roles, lst_rappears, lst_rcons = [], [], []
        for role, rappear, rcons in self.empl_roles_info:
            lst_roles.append(role)
            lst_rappears.append(rappear)
            lst_rcons.append(rcons)
        self.empl_roles = lst_roles
        self.empl_roles_appearance = lst_rappears
        self.empl_roles_consumption = lst_rcons
    
    def split_cpmtprle(self):
        lst_consprle, lst_ratios = [], []
        for cnsprle, ratio in self.empl_cpmtprle_info:
            lst_consprle.append(cnsprle)
            lst_ratios.append(ratio)
        self.empl_cpmtprle = lst_consprle
        self.empl_cpmtprle_ratio = lst_ratios
        

    def manage_role(self, setting, arg_role, arg_rappear = -1, arg_rcons = -1):
        
        if arg_rappear == -1:
            arg_rappear = round(random.uniform(0,1),2)
        if arg_rcons == -1:
            arg_rcons = round(random.uniform(0,1),2)
        
        if setting ==  "Add":
            if isinstance(arg_role, str):
                self.add_role(arg_role, arg_rappear, arg_rcons)
            else:
                for role, rappear, rcons in zip(arg_role, arg_rappear, arg_rcons):
                    self.add_role(role, rappear, rcons)
                    
        elif setting == "Modify":
            if isinstance(arg_role, str):
                self.modify_role(arg_role, arg_rappear, arg_rcons)
            else:
                for role, rappear, rcons in zip(arg_role, arg_rappear, arg_rcons):
                    self.modify_role(role, rappear, rcons)
                    
        elif setting == "Remove":
            if isinstance(arg_role, str):
                self.remove_role(arg_role)
            else:
                for role in arg_role:
                    self.remove_role(role)  
                    
    def add_role(self, role, rappear, rcons):
        if len(list(filter(lambda a: a[0] != role, self.empl_roles_info))) == len(self.empl_roles_info): 
            self.empl_roles_info.append((role, rappear, rcons))
            self.update_role_appearance()
            self.split_role()
        else:
            print("The Role is already existing!")

    def modify_role(self, role, nw_ratio = -1, nw_cons = -1):
        if len(list(filter(lambda a: a[0] != role, self.empl_roles_info))) == len(self.empl_roles_info): 
            print("The Generator does not include this role!")
        else:
            for idx, role_rappear in enumerate(self.empl_roles_info):
                if role_rappear[0] == role and nw_ratio >= 0 and nw_cons >= 0:
                    self.empl_roles_info[idx] = (role, nw_ratio, nw_cons)
                elif role_rappear[0] == role and nw_ratio >= 0 and nw_cons < 0:
                    self.empl_roles_info[idx] = (role, nw_ratio, role_rappear[2])
                elif role_rappear[0] == role and nw_ratio >= 0 and nw_cons >= 0:
                    self.empl_roles_info[idx] = (role, role_rappear[1], nw_cons)
                else:
                    pass
            self.update_role_appearance()
            self.split_role()
            
    def remove_role(self, role):
        if len(list(filter(lambda a: a[0] != role, self.empl_roles_info))) == len(self.empl_roles_info): 
           print("The Generator does not include this role!")
        else:
            self.empl_roles_info = list(filter(lambda a: a[0] != role, self.empl_roles_info))
            self.update_role_appearance()
            self.split_role()

    def update_role_appearance(self):
        ratios_appear = [ratio for _, ratio, _ in self.empl_roles_info]
        rappear = 1 / sum(ratios_appear)
        self.empl_roles_info = [(role, round(rappear * prev_ratio,3), rcons) for role, prev_ratio, rcons in self.empl_roles_info]
        self.empl_roles_info = sorted(self.empl_roles_info, key=lambda pair: pair[1], reverse=True)

        
    ##################
    # Other Function #
    ##################
    
    #Function to append the value to the corresponding dictionnary key
    def append_dict(self, data_dict, lst_key, lst_value):
        for key, val in zip(lst_key, lst_value):
            data_dict[key].append(val)
        return data_dict
  
      
    #Function that generate values corresponding to some conditions
    def generate_values(self, user_browser, user_vconf, moment, use_app=False):
        
        w_state = "Working"
        rand_act = random.random()
        
        if use_app == True:
            
            if moment == "Low":            
                conditions_act = [rand_act <= 0.50, 0.50 < rand_act <= 0.90, 0.90 < rand_act]
                back_cons = random.uniform(0, 0.1)

            elif moment == "Medium-Low":
                conditions_act = [rand_act <= 0.40, 0.40 < rand_act <= 0.70, 0.70 < rand_act]
                back_cons = random.uniform(0.05, 0.15)
            
            elif moment == "Medium-High":
                conditions_act = [rand_act < 0.30, 0.30 <= rand_act < 0.60, 0.60 <= rand_act]
                back_cons = random.uniform(0.1, 0.2)
                
            elif moment == "High": #moment == "High"
                conditions_act = [rand_act < 0.10, 0.10 <= rand_act < 0.50, 0.50 <= rand_act]
                back_cons = random.uniform(0.15, 0.25)
            
            
            choice_act = ['Basic Research', 'Newsfeed', 'Video Conferencing']
            act = np.select(conditions_act, choice_act)
            
            conditions_app = [act == 'Basic Research', act == 'Newsfeed', act == 'Video Conferencing']
            choice_app = [user_browser, random.choice(np.unique(self.app_df.Application[self.app_df.Actions == act])), random.choice(user_vconf)]
            app = np.select(conditions_app, choice_app)    

            carbon = float(self.app_df.Carbon_Impact[self.app_df.Application == app])
            back_cons = random.uniform(0.05, 0.1)

            conditions_duration = [act == 'Basic Research', act == 'Newsfeed', act == 'Video Conferencing']
            choice_duration = [random.randint(1, 5), random.randint(1,10), random.randint(20, 90)]
            duration = np.select(conditions_duration, choice_duration)
            
        else:

            if moment == "Late" or moment == "Day Off" or moment == "Lunch Break":
                w_state = moment
            
            conditions = [moment == "Low", moment == "Medium-Low", moment == "Medium-High", moment == "High", 
                          moment == "Late", moment == "Day Off", moment == "Lunch Break"]
            choice_conds = [(None, None, 0, random.uniform(0, 0.1), random.randint(5,20)), 
                            (None, None, 0, random.uniform(0.05, 0.15), random.randint(5,20)),
                            (None, None, 0, random.uniform(0.1, 0.2), random.randint(5,20)),
                            (None, None, 0, random.uniform(0.15, 0.25), random.randint(5,20)),
                            (None, None, 0, random.uniform(0, 0.2), None),
                            (None, None, 0, random.uniform(0, 0.1), None),
                            (None, None, 0, random.uniform(0.15, 0.3), random.randint(30, 90))]  
            act, app, carbon, back_cons, duration = np.select(conditions, choice_conds)
            
        return w_state, app, act, carbon, back_cons, duration
        
        
    def choice_cons_outlier(self, string, substr):
        rem_str = [str for str in string if any(sub in str for sub in substr)]
        return random.choice([str for str in string if str not in rem_str])
  
  
    #######################
    # Generation Function #
    #######################
    
    def Generation(self):
      
        general_dict = dict({"Employee ID":[], "Employee Role":[], "Employee Daily Consumption Level": [],
        "Full Date":[], "Working State":[], "Action Type":[], "App":[], "Time Spent":[],
        "App Carbon Impact":[], "Background Consumption":[], "Daily Consumption":[]
        })
        
        for _ in range(self.empl):
            employee_identifier = str(0) +''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])
            employee_role = "".join(random.choices([role for role, _, _ in self.empl_roles_info], [ratio for _,ratio, _ in self.empl_roles_info]))
            employee_cons = self.empl_roles_info[[self.empl_roles_info[i][0] for i in range(len(self.empl_roles_info))].index(employee_role)][2]
            current_day = self.initial_date.replace(hour=self.work_hours[0]) #Set the Initial Date
            user_browser = random.choice(np.unique(self.app_df.Application[self.app_df.Actions == "Basic Research"])) #Select a single Browser
            user_vconf = [random.choice(np.unique(self.app_df.Application[self.app_df.Actions == "Video Conferencing"])) for _ in range(2)] #Select up to two different Video Conferencing App

            while current_day <= self.end_date.replace(hour=self.work_hours[1]):
                constype_day = str(np.select([0 <= employee_cons <= 0.25, 0.25 < employee_cons <= 0.5, 0.5 < employee_cons <= 0.75, 0.75 < employee_cons <= 1],
                                             ['Low', 'Medium-Low', 'Medium-High', 'High']))
                outlier_day = True if random.random() > self.outlier_ratio else False
                
                if outlier_day == True:
                    constype_day = self.choice_cons_outlier(['Low', 'Medium-Low', 'Medium-High', 'High'], constype_day.split("-"))
                else:
                    pass
                
                          
                end_day = datetime.datetime(current_day.year, current_day.month, current_day.day, self.work_hours[1]) #Set the Daily End Work Hours
                daily_cons = 0 #Set the Daily Carbon Consumption as 0
                true_start = current_day + relativedelta(minutes=random.randint(-30, 30)) #Define the True Time (when the employee arrives at the Office)
                lunch_break = False #Set the "Lunch Break" Boolean at False
                ini_time = current_day if true_start > current_day else true_start #Define the Initial Time depending on a Condition

                #Check if the employee is Late
                if ini_time < true_start: #Check that the Initial Time is lower than the True Time
                    w_state, act, app, carbon, back_cons, _ = self.generate_values(user_browser, user_vconf, "Late")  
                    for d in range(1, int((true_start - current_day).seconds/60)+1): #Loop for the Time the Employee is Late
                        daily_cons += carbon + back_cons
                        lst_values = [employee_identifier, employee_role, constype_day, ini_time, w_state, act, app, d, carbon, back_cons, daily_cons]
                        self.append_dict(general_dict, list(general_dict.keys()), lst_values)
                        ini_time += relativedelta(minutes=1) #Incremente the Current Time by a minute
                else:
                    pass

                while ini_time <= end_day: #Loop for the Day
                    
                    if self.weekdays[current_day.weekday()] == "Sunday" or self.weekdays[current_day.weekday()] == "Saturday" and random.random() < 0.8:
                        w_state, act, app, carbon, back_cons, _ = self.generate_values(user_browser, user_vconf, "Day Off")
                        for d in range(1, int((end_day - current_day).seconds/60) + 1):
                            daily_cons += carbon + back_cons
                            lst_values = [employee_identifier, employee_role, constype_day, ini_time, w_state, act, app, d, carbon, back_cons, daily_cons]
                            self.append_dict(general_dict, list(general_dict.keys()), lst_values)
                            ini_time += relativedelta(minutes=1) #Incremente the Current Time by a minute
                    else:
                        use_app = True if ((constype_day == 'Low' and random.random() <= 0.15) or (constype_day == 'Medium-Low' and random.random() <= 0.3) or  (constype_day == 'Medium-High' and random.random() <= 0.6) or (constype_day == 'High' and random.random() <= 0.85)) else False               
                        w_state, act, app, carbon, back_cons, duration = self.generate_values(user_browser, user_vconf, constype_day, use_app)
                        for d in range(1, duration + 1):
                            daily_cons += carbon + back_cons
                            lst_values = [employee_identifier, employee_role, constype_day, ini_time, w_state, act, app, d, carbon, back_cons, daily_cons]
                            self.append_dict(general_dict, list(general_dict.keys()), lst_values)
                            ini_time += relativedelta(minutes=1) #Incremente the Current Time by a minute
                            
                            if lunch_break == False:
                                if (ini_time.hour > 11 and ini_time.minute >= 15) and d/duration > 0.75:
                                    lunch_break = True
                                    w_state, act, app, carbon, back_cons, duration = self.generate_values(user_browser, user_vconf, "Lunch Break")
                                    for d in range(1, duration + 1):
                                        daily_cons += carbon + back_cons
                                        lst_values = [employee_identifier, employee_role, constype_day, ini_time, w_state, act, app, d, carbon, back_cons, daily_cons]
                                        self.append_dict(general_dict, list(general_dict.keys()), lst_values)
                                        ini_time += relativedelta(minutes=1) #Incremente the Current Time by a minute
                                    break
                            else:
                                pass
                current_day += relativedelta(days=1)
        self.generator = pd.DataFrame.from_dict(general_dict)                           


        self.generator["Date"] = pd.to_datetime(self.generator["Full Date"]).dt.date
        quantile_lst = list(self.generator.groupby(["Employee Daily Consumption Level", "Date"])["Daily Consumption"].max().reset_index(name = "Max Consumption")["Max Consumption"].quantile([0.25, 0.5, 0.75]).reset_index(name = "Quantile")["Quantile"])
        quantile_lst

        temp_df = self.generator.groupby(["Employee ID", "Date"])["Daily Consumption"].max().reset_index(name = "Daily Consumption")


        conditions = [
            (temp_df['Daily Consumption'] < quantile_lst[0]),
            (temp_df['Daily Consumption'] >= quantile_lst[0]) & (temp_df['Daily Consumption'] < quantile_lst[1]),
            (temp_df['Daily Consumption'] >= quantile_lst[1]) & (temp_df['Daily Consumption'] < quantile_lst[2]),
            (temp_df['Daily Consumption'] >= quantile_lst[2])
        ]
        values = ["Low", "Medium-Low", "Medium-High", "High"]

        temp_df['True Employee Daily Consumption Level'] = np.select(conditions, values)

        self.generator = self.generator.merge(temp_df[["Employee ID", "Date", "True Employee Daily Consumption Level"]], how='left', on=['Employee ID', 'Date'])


    def Generate_Time_df(self):
        dict_time = dict({"Full Date":[], "Date": [], "Year":[], "Month":[], "Day":[], "Weekday":[], "Week Number":[], "Time":[]})
        for fdate in self.generator['Full Date']:
            date, year, month, day, weekday, week_num, time_hm = self.generate_time_data(fdate)
            self.append_dict(dict_time, list(dict_time.keys()), [fdate, date, year, month, day, weekday, week_num, time_hm])
        self.time_df = pd.DataFrame.from_dict(dict_time)
        

    #############################
    # Generation Visualizations #
    #############################
       
    def Produce_Viz(self):
        self.Viz_Displot()
        self.Viz_Barplot()
        self.Viz_PieChart()
        
    def Viz_Displot(self):
        sns.set_theme(style="whitegrid")
        sns.set_style("white")
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        plt.rc('font',family='Times New Roman')

        df = self.generator.groupby(["Employee ID", "Employee Role", "Date"])["Daily Consumption"].max().reset_index(name = "True Daily Consumption")
        ax = sns.displot(data=df, x="True Daily Consumption", hue="Employee Role", kind="kde", legend = False,
                        height=8, aspect = 2, multiple="fill", clip=(0, None), palette="ch:rot=-.25,hue=1,light=.75")

        plt.xticks(fontsize = 18)
        plt.yticks(fontsize = 18)
        plt.xlabel("Daily Consumption (gEqCO2)", fontsize = 22)
        plt.ylabel("Density", fontsize = 22)
        plt.legend(labels = np.unique(self.generator["Employee Role"]), title='Employee Role',title_fontsize=18, loc='center', bbox_to_anchor=(1.11, 0.5), shadow=True, prop={'size':15, 'family': 'Times New Roman' }, labelspacing=0.5)
        plt.title("Distribution of the Daily Consumption per Employee Role", size = 25)
        plt.tight_layout()
        plt.show()
    
    def Viz_Barplot(self):
        sns.set_theme(style="whitegrid")
        sns.set_style("white")
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        plt.rc('font',family='Times New Roman')
        plt.figure(figsize=(16, 9))

        df = self.generator.groupby(["Employee ID", "Employee Role", "Date"])["Daily Consumption"].max().reset_index(name = "True Daily Consumption")
        df["Month"] = pd.to_datetime(df["Date"]).dt.month_name()
        ax = sns.boxplot(x="Month", y="True Daily Consumption", hue="Employee Role", data=df, palette="crest", linewidth=2.5)


        plt.xticks(fontsize = 18)
        plt.yticks(fontsize = 18)
        plt.xlabel("Month", fontsize = 22)
        plt.ylabel("Daily Consumption (gEqCO2)", fontsize = 22)
        plt.legend(title='Employee Role',title_fontsize=16, loc='upper left', shadow=True, prop={'size':14, 'family': 'Times New Roman' }, labelspacing=0.2)
        plt.title("Comparison of Months Carbon Consumption per Employee Role", size = 25)
        plt.tight_layout()
        plt.show()
        
    def Viz_PieChart(self):
        sns.set_theme(style="whitegrid")
        sns.set_style("white")
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        plt.rc('font',family='Times New Roman')
        plt.figure(figsize=(16, 9))

        df = self.generator.groupby(["Employee ID", "Employee Role", "Date"])["Daily Consumption"].max().reset_index(name = "True Daily Consumption")
        df = df.groupby(['Employee Role'])["Employee ID"].count().reset_index(name = "Count")

        colors = sns.color_palette('crest')[0:5]
        plt.pie(df.Count, labels = np.unique(df["Employee Role"]), colors = colors, autopct='%.0f%%', textprops={"fontsize":20}, wedgeprops={'edgecolor':'k', 'linestyle': 'dashdot',    
                'antialiased':True} )
        plt.title("Proportion of Employees Roles", size = 25)

        sns.despine()

        plt.tight_layout()
        
        
###################
#   End Program   #
###################