import re
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

### BASIC PYTHON EXERCISES FOR DATA PROCESSING ###
# COVID-19 dataset: https://github.com/owid/covid-19-data/tree/master/public/data

# Data Preprocessing (Part 2)
#   Exercise 1: Read csv file to dictionary of countries and tuples of date and new cases.
#   Exercise 2: Same as exercise 1 but filter on valid country codes using REGEX. 
#   Exercise 3: Same as exercise 2 but create nested disctionaries to access cases as ['Norway']['2020-11-11']['new_cases']

# Data Analysis (Part 3)
#   Exercise 1: Weekly estimation of new cases per 100k. Returns float if successful or otherwise error handling message.
#   Exercise 2: Weekly estimation over time using 
#   Exercise 3:


# Data Analysis (Part 3)
#   Exercise 1: 
#   Exercise 2:
#   Exercise 3: 


# -------------- PART 2 --------------
#Part 2, exercise 1.
def read_data_1(filename):
    '''takes filename and inserts country names as keys and appends a tuple of date and new_cases 
    values to list in dictionary with corresponsing country key value '''
    
    #opens file
    file = open(filename, "r")
    
    #create empty dict
    dictionary = {}
    
    #reads line as chars, iterates through chars in line
    for row in file.readlines():
        row_variables = row.split(sep = ',')         #split into variables by delimiter ','  
        key = row_variables[2]                       #assign keys and vals by column index
        value = (row_variables[3], row_variables[5])
        dictionary.setdefault(key, []).append(value) #add values to value list
        
    file.close()
    
    return dictionary

    
#Part 2, Exercise 2.
def read_data_2(filename):
    '''takes filename and inserts country names that have VALID COUNTRY CODES as keys and appends a tuple of date and new_cases 
    values to list in dictionary with corresponsing country key value '''

    file = open(filename, "r")

    dictionary = {}
    regex = re.compile('^[A-Z]{3}$')

    #reads line as chars, iterates through chars in line
    for row in file.readlines():
        row_variables = row.split(sep = ',')         
        #inserts key and vals in dicts if regex matches the first column-value/valid country-code
        if regex.match(row_variables[0]):
            key = row_variables[2]
            value = (row_variables[3], row_variables[5])
            dictionary.setdefault(key, []).append(value)
    
    file.close()
    
    return dictionary

#Part 2, Exercise 3
def read_data_3(filename):
    '''takes filename and inserts country names that have VALID COUNTRY CODES as keys and appends a dictionary of dates as key and 
    a dictionary of column name and values'''

    file = open(filename, "r")
    column_names = [elem.strip() for elem in file.readline().split(',')][4:]    
    regex = re.compile('^[A-Z]{3}$')
    country_dictionary = {}

    #reads line as chars, iterates through chars in line
    for row in file.readlines():
        row_variables = row.split(sep = ',')

        country_name = row_variables[2]
        date = row_variables[3]  
        date_dictionary = {} # dictionary for row-specific date
        column_var_dictionary = {} # dictionary for row-specific column variables
        
        
        if regex.match(row_variables[0]):    
            
            #iterate through each column variable
            for i in range(len(column_names)):     
                
                column_name = column_names[i]
                column_value = row_variables[i+4].strip("\n")
                
                #filled zero value to empty data for the sake of having uniform data for part 3. 
                if column_value == "":
                    column_value = "0" 
                
                column_var_dictionary[column_name] = column_value  #insert column value at corresponding column name
        
        date_dictionary.setdefault(date,{})
        country_dictionary.setdefault(country_name,{})
        country_dictionary[country_name][date] = column_var_dictionary
        
    
    return country_dictionary



# -------------- PART 3 --------------
#Part 3, Exercise 1
def get_weekly_per_100k_for_country_date(covid_dictionary, country_name, date):
    '''Takes takes double-nested dictionary, country name and date as strings, calculates weekly 
    estimation of new cases per 100k according to specified arguments. Returns float if successful 
    or None + exception message if invalid argument input'''
    
    try:
        new_cases_smoothed_1m = covid_dictionary[country_name][date]["new_cases_smoothed_per_million"]
        weekly_estimate_100k = float(new_cases_smoothed_1m) * 0.7 
    except:
        weekly_estimate_100k = None
        print("Value not found for argumens: {}, {}. Check argument types and if arguments are valid".format(country_name, date))
    
    
    return weekly_estimate_100k

#Part 3, Exercise 2
def get_weekly_per_100k_for_country(covid_dictionary, country_name):
    '''Takes covid dictionary and country name input and returns two list of dates and values of 
    new cases calculated by get_weekly_per_100k_for_country_date. Formats strings to dates '''
    date_list = []
    weekly_per_100k_list = []
    
    for key, val in covid_dictionary[country_name].items():
        date = datetime.datetime.strptime(key, '%Y-%m-%d').date() #convert string to datetime. Only keep date
        date_list.append(date)
        weekly_estimate = get_weekly_per_100k_for_country_date(covid_dictionary, country_name, key)
        weekly_per_100k_list.append(weekly_estimate)    
    
    return date_list, weekly_per_100k_list


#Part 3, Exercise 3
def plot_weekly_per_100k_for_country(covid_dictionary, country_name):
    '''Takes covid dictionary and country name, and utilize get_weekly_per_100k() to get data about weekly  '''
    #get x and y values
    x_dates, y_weekly_estimates = get_weekly_per_100k_for_country(covid_dictionary, country_name)
    
    #create lineplot 
    fig = plt.figure()
    ax = plt.axes()
    
    plt.plot(x_dates, y_weekly_estimates)
    
    #a: limits x-axis to only one tickmark
    ax.xaxis.set_major_locator(mdates.MonthLocator()) 
    
    # b: layout of x-axis labels
    fig.autofmt_xdate() 
    
    #c: constant dotted line at y=20
    plt.axhline(y=20, color='gray', linestyle='--')
    
    #d: title with string formatted for country name
    plt.title('Weekly cases per 100k for {}'.format(country_name), fontsize=10)
    
    #e: axis labels
    ax.set_xlabel('time')
    ax.set_ylabel('new weekly cases (per 100k)')
    
    #I chose to keep all the date values, even though some 5 data points in csv is missing.
    #If there were more data points missing I would consider to remove dates to get a more detailed
    #plot. I chose to keep zero values to show possible correlations when plotted with additional y-values. 
    
    return fig, ax


# -------------- PART 4 --------------
#Part 4, Exercise 1
def read_into_dataframe(filename, countries = None):
    '''loads csv to dataframe, removes invalid location by iso_code (NaN and non-3-digit),
    and filter the dataframe for locations not matching the given countries input.'''
    #a: load csv as dataframe
    df = pd.read_csv(filename)
    df = df[df['iso_code'].notna()]   #removed apprx. 300 rows with iso_code = 'NaN' 
    regex = re.compile('^[A-Z]{3}$')
    index_list = []
    
    #get indices for rows where iso_code is not valid
    iso_column = df.loc[: ,'iso_code']
    for i in range(len(iso_column)):
        if not regex.match(iso_column[i]):
            index_list.append(i)
    
    #b: remove rows of index in index_list
    new_df = df.drop(df.index[index_list])
    
    #c: format 'date' column from string to datetime
    new_df['date'] = pd.to_datetime(new_df['date'], format ='%Y-%m-%d')
    
    #d: filter dataframe according to countries input, had to iterate items because iteration like 
    #over range(len(column)) crashed at the same place every time. Substituted this with a counter instead. 
    if countries != None:
        country_indices = []
        counter = 0
        country_column = new_df.location
        for country in country_column:
            counter += 1
            if country not in countries:
                country_indices.append(counter-1)
        
        new_df = new_df.drop(new_df.index[country_indices])
    
    return new_df
    
#Part 4, Exercise 2
def get_weekly_per_100k(dataframe):
    '''Takes a dataframe of covid data, extracts new_cases_per_million column, 
    groups by country and reshape for a week, and calculates weekly sum per 100k people 
    based on a weekly average. Returns new dataframe with weekly data points. '''
    
    #get only relevant columns
    df = dataframe[['location', 'date', 'new_cases_per_million']]
    
    #a: index to date values
    df.set_index('date', inplace = True)
    
    
    #b: get weekly dates every sunday from start date
    idx = pd.date_range('2020-01-05', '2020-10-22', freq ='W-SUN')
    new_df = pd.DataFrame(np.ones(len(idx)),index = idx) #'empty' dataframe with resized shape    
    new_df = df.groupby('location').resample('W').mean()
    #Produces summed data points for every week(sundays). I chose to keep the 'future' data point 
    #/incomplete week '2020-10-25' as removal would mean a loss in the most recent data points.
    
    
    #b+d: rescale average to 100k and get averaged sum over week.
    new_df.new_cases_per_million = new_df.new_cases_per_million.mul(0.7, fill_value = 0)
    new_df.rename(columns={'new_cases_per_million': 'weekly_new_cases_per_100k'}, inplace = True)
    
    #c:reset index to original
    new_df = new_df.reset_index()
    
    return new_df

#Part 4, Exercise 3
def get_weekly_per_100k_country_vs_date(dataframe):
    ''' Receives dataframe with columns location, dates of any frequency and new_cases_per_100k, 
    returns panda.pivot() where '''
    
    new_df = dataframe.pivot(index='location', columns='date', values = 'weekly_new_cases_per_100k')
    
    return new_df

    
    
    
