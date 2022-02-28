import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, axes = plt.subplots(figsize=(12, 6))
    axes.scatter('Year','CSIRO Adjusted Sea Level',data=df)

    # Create a linear regression with the data
    res = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    
    # Create a series from the first year reported to 2050
    ser_1880 = pd.Series(range(df['Year'].values.min(),2051))
    
    # Create first line of best fit
    axes.plot(ser_1880,(ser_1880.values) * res.slope + res.intercept,c='red')

    # Create a dataframe from 2000 to the last year reported
    df_2000 = df[df['Year'] >= 2000]
    
    # Create a linear regression from 2000
    res_2000 = linregress(df_2000['Year'],df_2000['CSIRO Adjusted Sea Level'])
    
     # Create a series from 200 to 2050
    ser_2000 = pd.Series(range(2000,2051))
    
    # Create second line of best fit
    axes.plot(ser_2000,(ser_2000.values) * res_2000.slope + res_2000.intercept,c='green')
    
    
    # Add labels and title
    axes.set_title('Rise in Sea Level')
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()