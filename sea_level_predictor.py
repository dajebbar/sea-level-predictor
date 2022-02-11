import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(14, 6))
    plt.scatter(data.Year, data["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    first_line = linregress(data.Year, data['CSIRO Adjusted Sea Level'])

    theta0 = np.arange(data.Year.min(), 2051)
    y_hat0 = theta0 * first_line.slope + first_line.intercept

    plt.plot(theta0, y_hat0)

    # Create second line of best fit
    df = data[data['Year'] >= 2000]
    second_line = linregress(
    df.Year, 
    df['CSIRO Adjusted Sea Level']
    )

    theta = np.arange(2000, 2051)
    y_hat = theta * second_line.slope + second_line.intercept

    plt.plot(theta, y_hat)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')


    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
