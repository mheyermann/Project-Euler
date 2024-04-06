import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Import data
df = pd.read_csv('medical_examination.csv').set_index('id')

# Add 'overweight' column
BMI = df['weight']/(df['height']/100)**2
df['overweight'] = BMI
df.loc[df['overweight'] <= 25, 'overweight'] = 0
df.loc[df['overweight'] > 25, 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat[df_cat['variable'] == 'cardio'].rename(columns={'value': 'cardio'})
    df_cat = df_cat.drop(columns=['variable'])

    # Flattening the multi-level column index
    values = df_cat.groupby('cardio').agg(lambda x: [(x == 0).sum(), (x == 1).sum()])

# Displaying the result 
    variable = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    cardio = [0, 1]
    value = [0, 1, 0, 1]

# Initialize an empty list to hold dictionaries
    data = []

# Populate the DataFrame
    for c in cardio:
        for v in value:
            row = {'Cardio': c, 'value': v}
            for var in variable:
                row[var] = values.loc[c, var][v]
            data.append(row)

# Convert the list of dictionaries to a DataFrame
    df_cat = pd.DataFrame(data)

# Remove duplicate rows
    df_cat = df_cat.drop_duplicates().reset_index(drop=True)

# Melt the DataFrame to long format
    df_cat = pd.melt(df_cat, id_vars=['Cardio', 'value'], value_vars=variable, 
                            var_name='variable', value_name='Count')

# Convert 'value' column to string type
    df_cat['value'] = df_cat['value'].astype(str)
# Define the order of 'Variable' values
    order = sorted(df_cat['variable'].unique())

# Draw the catplot with 'sns.catplot()'
# Plotting
    g = sns.catplot(
        data=df_cat,
        x='variable',
        y='Count',
        hue='value',
        kind='bar',
        col='Cardio',
        col_wrap=2,
        height=6,
        aspect=1.5,
        dodge=True,
        order=order
    )
    g.set_axis_labels("variable", "total")
    g.set_xticklabels(rotation=0)
    g.set_titles(col_template="Cardio = {col_name}")
    

    plt.tight_layout()
    plt.show()




    # Get the figure for the output
    fig = g


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['ap_lo'] <= df['ap_hi']) & (df['weight'] <= df['weight'].quantile(0.975))]
    df_heat = df_heat.reset_index(drop=False)
    corr = df_heat.corr(method='pearson')


    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool), k=0)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, mask=mask, fmt=".1f", cmap='coolwarm', vmin=-0.1, vmax=0.3, square=True)

    # Display the plot
    plt.tight_layout()
    plt.show()


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
