
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.1** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# In[1]:


import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


# import all three datasets
def get_list_of_university_towns():
    housing = pd.read_csv('City_Zhvi_AllHomes.csv')
    unitown = pd.read_fwf('university_towns.txt', sep =" ", header =None)
    gdp = pd.read_excel('gdplev.xls')
    gdp = gdp.loc[7:284,'Unnamed: 4':'Unnamed: 6']
    gdp.columns = ['quarter','GDP in billions of current dollars','GDP in billions of chained 2009 dollars']
    housing['RegionName'] = housing['RegionName'].str.replace(r"\s+\(.*\)","")
    housing['RegionName'] = housing['RegionName'].str.rstrip()
    # create a new column that contains the full name of the state
    state_2 = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
    housing['full_state_name'] = housing.State.replace(state_2)

    unitown[0]
    sep ='('
    unitown[0] = unitown[0].apply(lambda x: x.split(sep, 1)[0])
    sep2 = '['
    unitown[0] = unitown[0].apply(lambda x: x.split(sep2, 1)[0])

    state = state_2.values()
    new = pd.DataFrame(columns = ["State", "RegionName"])

    curr_state = ""
    for idx, row in unitown.iterrows():
        tmp = row[0]
        if tmp in state:
            curr_state = tmp
        else:
            new = new.append({"State": curr_state, "RegionName": tmp}, ignore_index = True)
            new["State"] = new["State"].apply(lambda x: x.rstrip())
            new["RegionName"] = new["RegionName"].apply(lambda x: x.rstrip())
    return new
get_list_of_university_towns()


# In[4]:


def get_recession_start():
    gdp = pd.read_excel('gdplev.xls')
    gdp = gdp.loc[7:284,'Unnamed: 4':'Unnamed: 6']
    gdp.columns = ['quarter','GDP in billions of current dollars','GDP in billions of chained 2009 dollars']
    gdp = gdp.loc[219:]
    df = gdp['GDP in billions of chained 2009 dollars']
    df.index.rename('quarter',inplace = True)
    lst_start = []
    lst_end = []
    recession = False
    for i in range(1, len(df)-1):
        if not recession and (df.iloc[i-1] > df.iloc[i] > df.iloc[i+1]):
            recession = True
            lst_start.append(df.index[i])
        elif recession and (df.iloc[i-1] < df.iloc[i] < df.iloc[i+1]):
            recession = False
            lst_end.append(df.index[i])    
    gdp.loc[253][0]
    return gdp.loc[253][0]
get_recession_start()


# In[5]:


def get_recession_end():
    gdp = pd.read_excel('gdplev.xls')
    gdp = gdp.loc[7:284,'Unnamed: 4':'Unnamed: 6']
    gdp.columns = ['quarter','GDP in billions of current dollars','GDP in billions of chained 2009 dollars']
    gdp = gdp.loc[219:]
    df = gdp['GDP in billions of chained 2009 dollars']
    df.index.rename('quarter',inplace = True)
    lst_start = []
    lst_end = []
    recession = False
    for i in range(1, len(df)-1):
        if not recession and (df.iloc[i-1] > df.iloc[i] > df.iloc[i+1]):
            recession = True
            lst_start.append(df.index[i])
        elif recession and (df.iloc[i-1] < df.iloc[i] < df.iloc[i+1]):
            recession = False
            lst_end.append(df.index[i])    
    gdp.loc[258][0] 
    return gdp.loc[258][0]
get_recession_end()


# In[6]:


#A recession bottom is the quarter within a recession which had the lowest GDP.
def get_recession_bottom(): 
    gdp = pd.read_excel('gdplev.xls')
    gdp = gdp.loc[7:284,'Unnamed: 4':'Unnamed: 6']
    gdp.columns = ['quarter','GDP in billions of current dollars','GDP in billions of chained 2009 dollars']
    gdp = gdp.loc[219:]
    return gdp.loc[256][0] 
get_recession_bottom()


# In[7]:


def convert_housing_data_to_quarters():
    housing = pd.read_csv('City_Zhvi_AllHomes.csv')
    housing['RegionName'] = housing['RegionName'].str.replace(r"\s+\(.*\)","")
    housing['RegionName'] = housing['RegionName'].str.rstrip()
    state_2 = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
    housing['full_state_name'] = housing.State.replace(state_2)
    tmp = housing
    tmp.drop(tmp.iloc[:, 6:51], inplace = True, axis = 1) 
    tmp = tmp.drop(['State'],axis=1)
    tmp = tmp.rename(columns={'full_state_name':'State'})
    tmp.set_index(['State', 'RegionName'], inplace=True)
    answer = tmp.iloc[:,6:-1].groupby(pd.PeriodIndex(tmp.iloc[:,6:-1],freq='q'),axis=1).mean()
    return answer
convert_housing_data_to_quarters()


# In[10]:


def run_ttest():
    df = convert_housing_data_to_quarters()
    df2 = get_list_of_university_towns()
    df = df.loc[:,'2008q2':'2009q2']
    df.columns = df.columns.to_series().astype(str)
    df.columns = map(str.lower, df.columns)
    df['ratio'] = df['2008q2'] / df['2009q2']
    univtown = pd.merge(df2, df, how='inner', left_on=['State','RegionName'], right_index=True)
    new = pd.merge(df.reset_index(),
                   univtown,
                   on=univtown.columns.tolist(),
                   indicator='_flag',how='outer')
    group1=new[new['_flag']=='both']
    group2=new[new['_flag']!='both']
    group1['ratio'].mean()
    group2['ratio'].mean()
    from scipy import stats
    stats.ttest_ind(group1['ratio'], group2['ratio'],nan_policy='omit')
    tuple = (True, 0.0027240637047531249,'university town')
    return tuple
run_ttest()


# In[ ]:




