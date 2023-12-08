#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
import re


# In[2]:


URL_5k_p1_2023 = 'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=1&dt=0&PageNo=1'


# In[3]:


response = requests.get(URL_5k_p1_2023)
response.raise_for_status()


# In[4]:


def get_names(response):
    soup = BeautifulSoup(response.content, "html.parser")
    values = soup.find_all('a', class_ = 'ltw-name', target = '_blank')
    extracted_names = [name.get_text() for name in values]
    names_series = pd.Series(extracted_names)
    return names_series

def get_ages(response, year):
    soup = BeautifulSoup(response.content, "html.parser")
    values = soup.find_all('td' ,class_ = 'd-none d-sm-table-cell')
    extracted_values = [age.get_text() for age in values]
    value_series = pd.Series(extracted_values)
    numeric_age_data = pd.to_numeric(value_series, errors='coerce')
    if (year == 2023):
        correct_age_data = numeric_age_data.iloc[3::5]
    elif(year == 2022):
        correct_age_data = numeric_age_data.iloc[2::5]
    elif(year == 2019):
        correct_age_data = numeric_age_data.iloc[4::8]
    elif (year == 2018):
        correct_age_data = numeric_age_data.iloc[4::8]
    elif (year == 2017 or year == 2016):
        correct_age_data = numeric_age_data.iloc[2::5]
    elif (year == 2015 or year == 2014):
        correct_age_data = numeric_age_data.iloc[2::5]
    elif (year == 2013):
        correct_age_data = numeric_age_data.iloc[2::5]
    
    correct_age_data.reset_index(drop=True, inplace=True)
    correct_age_data = correct_age_data.astype(int)
    return correct_age_data

def get_times(response, year):
    soup = BeautifulSoup(response.content, "html.parser")
    values = soup.find_all('td' ,class_ = 'd-none d-sm-table-cell ltw-time')
    extracted_values = [time.get_text() for time in values]
    value_series = pd.Series(extracted_values)
    if (year == 2015 or year == 2014):
        correct_time_data = value_series.iloc[0::2]
    if (year == 2013):
        correct_time_data = value_series.iloc[0::2]
    else:
        correct_time_data = value_series.iloc[1::2]
    correct_time_data.reset_index(drop=True, inplace=True)
    return correct_time_data

def get_gender(response):
    soup = BeautifulSoup(response.content, "html.parser")
    values = soup.find_all('a', class_ = 'ltw-name')
    extracted_values = [value.get_text() for value in values]
    value_series = pd.Series(extracted_values)
    correct_gender_data = value_series.iloc[2::3]
    correct_gender_data.reset_index(drop=True, inplace=True)
    return correct_gender_data


# In[5]:


def generate_dataframe(URL, distance, year):
    response = requests.get(URL)
    response.raise_for_status()
    names = get_names(response)
    ages = get_ages(response, year)
    times = get_times(response, year)
    genders = get_gender(response)
    df = pd.DataFrame({'Distance':distance, 
                       'Year':year,
                       'Name': names, 
                       'Age': ages, 
                       'Time': times, 
                       'Gender': genders 
                       })
    return df
    


# In[9]:


url_5K_2023 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=1',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=1&dt=0&PageNo=2',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=1&dt=0&PageNo=3',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=1&dt=0&PageNo=4',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=1&dt=0&PageNo=5',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=1&dt=0&PageNo=6',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=1&dt=0&PageNo=7',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=1&dt=0&PageNo=8',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=1&dt=0&PageNo=9',]
url_10K_2023 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=2&dt=0&PageNo=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=2&dt=0&PageNo=3',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=2&dt=0&PageNo=4',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=2&dt=0&PageNo=5',]
url_5K_2022 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=6103',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=1&dt=0&PageNo=2',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=1&dt=0&PageNo=3',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=1&dt=0&PageNo=4',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=1&dt=0&PageNo=5',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=1&dt=0&PageNo=6',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=1&dt=0&PageNo=7',]
url_10K_2022 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=2&dt=0&PageNo=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=2&dt=0&PageNo=3',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=2&dt=0&PageNo=4',]
url_5K_2019 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=6072',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6072&EId=1&dt=0&PageNo=2',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6072&EId=1&dt=0&PageNo=3',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6072&EId=1&dt=0&PageNo=4',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6072&EId=1&dt=0&PageNo=5',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6072&EId=1&dt=0&PageNo=6',]
url_10K_2019 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=6072&EId=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6072&EId=2&dt=0&PageNo=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6072&EId=2&dt=0&PageNo=3',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6072&EId=2&dt=0&PageNo=4',]
url_5K_2018 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=6047',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=1&dt=0&PageNo=2',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=1&dt=0&PageNo=3',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=1&dt=0&PageNo=4',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=1&dt=0&PageNo=5',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=1&dt=0&PageNo=6',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=1&dt=0&PageNo=7',]
url_10K_2018 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=2&dt=0&PageNo=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=2&dt=0&PageNo=3',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=2&dt=0&PageNo=4',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047&EId=2&dt=0&PageNo=5',]
url_5K_2017 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=6024',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6024&EId=1&dt=0&PageNo=2',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6024&EId=1&dt=0&PageNo=3',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=6024&EId=1&dt=0&PageNo=4',]
url_10K_2017 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=6024&EId=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6024&EId=2&dt=0&PageNo=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=6024&EId=2&dt=0&PageNo=3',]
url_5K_2016 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=188',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=188&EId=1&dt=0&PageNo=2',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=188&EId=1&dt=0&PageNo=3',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=188&EId=1&dt=0&PageNo=4',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=188&EId=1&dt=0&PageNo=5',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=188&EId=1&dt=0&PageNo=6',]
url_10K_2016 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=188&EId=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=188&EId=2&dt=0&PageNo=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=188&EId=2&dt=0&PageNo=3',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=188&EId=2&dt=0&PageNo=4',]
url_5K_2015 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=148',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=1&dt=0&PageNo=2',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=1&dt=0&PageNo=3',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=1&dt=0&PageNo=4',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=1&dt=0&PageNo=5',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=1&dt=0&PageNo=6',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=1&dt=0&PageNo=7',]
url_10K_2015 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=2&dt=0&PageNo=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=2&dt=0&PageNo=3',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=2&dt=0&PageNo=4',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=2&dt=0&PageNo=5',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=2&dt=0&PageNo=6',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=148&EId=2&dt=0&PageNo=7',]
url_5K_2014 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=92',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=1&dt=0&PageNo=2',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=1&dt=0&PageNo=3',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=1&dt=0&PageNo=4',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=1&dt=0&PageNo=5',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=1&dt=0&PageNo=6',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=1&dt=0&PageNo=7',
               'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=1&dt=0&PageNo=8',]
url_10K_2014 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=2&dt=0&PageNo=2',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=2&dt=0&PageNo=3',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=2&dt=0&PageNo=4',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=2&dt=0&PageNo=5',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=2&dt=0&PageNo=6',
                'https://results.changeofpace.com/results.aspx?CId=16356&RId=92&EId=2&dt=0&PageNo=7',]
url_5K_2013 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=30',]
url_10K_2013 = ['https://results.changeofpace.com/results.aspx?CId=16356&RId=30&EId=2',]


# In[10]:


years = [2023, 2022, 2019, 2018, 2017, 2016, 2015, 2014, 2013]
doc_types = ['5K', '10K']
dfs = {f"df_{year}_{doc_type}": pd.DataFrame() for year in years for doc_type in doc_types}
for year in years:
    for doc_type in doc_types:
        for url in globals()[f"url_{doc_type}_{year}"]:
            df = generate_dataframe(url, doc_type, year)
            dfs[f"df_{year}_{doc_type}"] = pd.concat([dfs[f"df_{year}_{doc_type}"], df], ignore_index=True)
all_dfs = pd.concat(dfs.values(),axis=0)


# In[11]:


all_dfs.to_csv('all_data.csv', index=False)


# In[194]:


URL = 'https://results.changeofpace.com/results.aspx?CId=16356&RId=6121&EId=2&dt=0&PageNo=2'
df = generate_dataframe(URL, '5K', 2023)
df


# In[120]:


URL = 'https://results.changeofpace.com/results.aspx?CId=16356&RId=6103&EId=2'
df = generate_dataframe(URL, '10K', 2022)
df


# In[121]:


URL = 'https://results.changeofpace.com/results.aspx?CId=16356&RId=6072'
df = generate_dataframe(URL, '5K', 2019)
df.dropna()


# In[122]:


URL = 'https://results.changeofpace.com/results.aspx?CId=16356&RId=6047'
df = generate_dataframe(URL, '5K', 2018)
df.dropna()


# In[128]:


URL = 'https://results.changeofpace.com/results.aspx?CId=16356&RId=6024'
df = generate_dataframe(URL, '5K', 2017)
df.dropna()


# In[137]:


URL = 'https://results.changeofpace.com/results.aspx?CId=16356&RId=188'
df = generate_dataframe(URL, '5K', 2016)
df.dropna()

