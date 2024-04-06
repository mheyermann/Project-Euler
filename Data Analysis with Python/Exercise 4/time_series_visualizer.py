import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    # Create the plot
    fig = plt.figure(figsize=(10, 6))
    df['value'].plot(linewidth=1)  # Plot the 'value' column as a line

    # Set plot elements
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.grid(True)  # Add grid lines for better readability
    plt.tight_layout()  # Adjust spacing to prevent overlapping elements
    plt.gcf().autofmt_xdate()

    # Display the plot
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)  # Resetting index to make 'date' a column
    df_bar['date'] = pd.to_datetime(df_bar['date'])  # Convert 'date' to datetime type
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()

    
    # Setting the order of months
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['month'] = pd.Categorical(df_bar['month'].apply(lambda x: months_order[x-1]), categories=months_order)

    # Convert data types to float explicitly
    df_bar['value'] = df_bar['value'].astype(float)

    # Drawing the bar plot
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(data=df_bar, x='year', y='value', hue='month')

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', loc='upper left')

    # Display the plot
    plt.show()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 7))
     # Year-wise Box Plot (Trend)
    sns.boxplot(x=df_box['year'], y=df_box['value'], ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot (Seasonality)
    # Set the order of months
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    sns.boxplot(x=df_box['month'], y=df_box['value'], order=months_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Adjust layout to prevent overlap
    plt.tight_layout()



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
