import exam
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

'''Comments:
 - Some code could be more compact, but is divided in parts for readability and debugging.
 - Comments in code for considerations of why a certain logic, decision, or function was used.
 - In exercise 4.3 I assumed that since curriculum comprises dataframes and the panda package, 
     I could use the pd.DataFrame.Pivot() function as other logics/functions were not specified.
- all imported packages have been covered in the curriculum.
'''

#Exercise 2.1
covid_dict_1 = exam.read_data_1("owid-covid-data.csv")


#Exercise 2.2
covid_dict_2 = exam.read_data_2("owid-covid-data.csv")


#Exercise 2.3
covid_dict_3 = exam.read_data_3("owid-covid-data.csv")
print("ex 2.3 output Denmark,2020-10-20,new_cases: {}".format(covid_dict_3["Denmark"]["2020-10-20"]["new_cases"]))


#Exercise 3.1
print(exam.get_weekly_per_100k_for_country_date(covid_dict_3, "Czech Republic", '2020-10-20'))


#Exercise 3.2
dates, values = exam.get_weekly_per_100k_for_country(covid_dict_3, "Czech Republic")
print(dates[100], values[100])


#Exercise 3.3
exam.plot_weekly_per_100k_for_country(covid_dict_3, "Czech Republic")
plt.savefig('weekly_cases_cze.png')


#Exercise 4.1
df = exam.read_into_dataframe('owid-covid-data.csv')
df_selected_countries = exam.read_into_dataframe('owid-covid-data.csv', ['Austria', 'Belarus', 
                                    'Belgium', 'Bulgaria', 'Czech Republic', 'Denmark', 'Finland', 
                                    'France', 'Germany', 'Greece', 'Hungary', 'Italy', 'Netherlands', 
                                    'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 
                                    'Slovakia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 
                                    'United Kingdom','United States'])


#Exercise 4.2
weekly_per_100k = exam.get_weekly_per_100k(df_selected_countries)


#Exercise 4.3
country_vs_date = exam.get_weekly_per_100k_country_vs_date(weekly_per_100k)



fig, ax = plt.subplots()
x_vals = matplotlib.dates.date2num(pd.to_datetime(country_vs_date.columns))
aspect_ratio = (country_vs_date.shape[1] /country_vs_date.shape[0]*7)
plt.imshow(country_vs_date.values, aspect=aspect_ratio, extent=[x_vals[0], x_vals[-1], 0, country_vs_date.shape[0]])
ax.xaxis_date()
fig.autofmt_xdate()
ax.set_yticks(np.arange(country_vs_date.values.shape[0])+0.5)
ax.set_yticklabels(country_vs_date.index[::-1])
plt.colorbar()
plt.savefig('weekly_new_cases_per_100k.png')
