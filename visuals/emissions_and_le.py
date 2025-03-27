import pandas as pd 
import matplotlib.pyplot as plt
from visuals.funcs import *
import re 

df = pd.read_csv('./visuals/data.csv', encoding='latin1')
co2prod2022 = df['co2_prod_2022']
le2022 = df['le_2022']
hdi2022 = df['hdi_2022']

hdi_years = [c for c in df.columns if re.match(r'hdi_\d{4}', c)]
le_years = [c for c in df.columns if re.match(r'le_\d{4}', c)]
eys_years = [c for c in df.columns if re.match(r'eys_\d{4}', c)]
gnipc_years = [c for c in df.columns if re.match(r'gnipc_\d{4}', c)]



# store each visual / scatterplot as a variable that we can export into app.py
def co2_vs_le():
    fig, ax = plt.subplots()  # Create a Matplotlib figure and axes
    scatter_plot = ax.scatter(co2prod2022, le2022)  # Create the scatterplot on the axes
    ax.set_xlabel('CO2 Per Capita 2022 (Tons)')  # Set x-axis label
    ax.set_ylabel('Life Expectancy 2022')  # Set y-axis label
    ax.set_title('CO2 Per Capita vs Life Expectancy 2022')  # Set title

    return fig 

def hdi_vs_co2():
    fig, ax = plt.subplots()
    scatter_plot = ax.scatter(hdi2022, co2prod2022)
    ax.set_xlabel('HDI 2022')
    ax.set_ylabel('CO2 Per Capita 2022 (Tons)')
    ax.set_title('HDI vs CO2 Per Capita 2022')

    return fig 

def co2_vs_hdi_percent_change():
    data = df.copy()
    data['hdi_le'] = data.apply(lambda r: get_hdi_pop_pairs(r, hdi_years, le_years), axis=1)

    ts = data[['iso3','hdi_le']].explode('hdi_le')
    ts = pd.concat([ts.drop(['hdi_le'], axis=1), ts['hdi_le'].apply(pd.Series)], axis=1)

    ts['hdi_pct_change'] = ts.groupby('iso3')['hdi'].pct_change()
    ts['le_pct_change'] = ts.groupby('iso3')['le'].pct_change()
    
    fig, ax = plt.subplots()  

    plt.rcParams['lines.markersize'] = 5

    ax.scatter(ts['hdi_pct_change'], ts['le_pct_change'])
    ax.set_xlabel('HDI Percent Change')
    ax.set_ylabel('Life Expectancy Percent Change')
    ax.set_title('HDI Percent Change vs Life Expectancy Percent Change')
    
    return fig