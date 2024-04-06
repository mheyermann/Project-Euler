import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='blue', label='Data')

    # Step 3: Use linregress to get the slope and y-intercept
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x_future = np.arange(1880, 2051, 1)
    y_future = slope * x_future + intercept
    plt.plot(x_future, y_future, 'r', label='Best Fit 1880-2050')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Create a line of best fit for recent data through the year 2050
    x_recent_future = np.arange(2000, 2051, 1)
    y_recent_future = slope_recent * x_recent_future + intercept_recent
    plt.plot(x_recent_future, y_recent_future, 'g', label='Best Fit 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()