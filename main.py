import pandas as pd
import matplotlib.pyplot as plt


# Read datas from csv-file
df = pd.read_csv('bird_population.csv')

# Print dates from dataframe
print(f'Total number of observations: {df.shape[0]}')
print('-------------------------------------')
print(f'Unique number of birds: {df.groupby('species')['count'].nunique()}')
print('-------------------------------------')
print(f'Unique dates of observation: {df.groupby('date')['count'].nunique()}')
print('-------------------------------------')

# Calculating the average number of birds seen
mean_count = df['count'].mean()
# Calculate the median number of birds seen
median_count = df['count'].median()
# Calculate the standard deviation of the number
std_count = df['count'].std()
print(f'Average number of birds seen: {mean_count}')
print(f'Median number of birds seen: {median_count}')
print(f'Standard deviation of number of birds seen: {std_count}')
print('-------------------------------------')
# Counting unique values and selecting the most frequent location
most_location = df['location'].value_counts().idxmax()
# Calculate the number of observations for the most frequent location
observations_count = df[df['location'] == most_location].shape[0]
print(f'Most common location for observation: {most_location}, {observations_count}')

# Grouping dates for plotter
birds_plot = df.groupby('species').size().reset_index(name='observations')
# Sorting of dates
birds_plot = birds_plot.sort_values(by='observations', ascending=False)
# Create graph
plt.figure(figsize=(10, 6))
# Setting up graph
plt.bar(birds_plot['species'], birds_plot['observations'], color='skyblue')
plt.xlabel('Kinds of Birds', fontsize=20)
plt.ylabel('Counts of observations', fontsize=20)
# Creating title of graph
plt.title('Distribution of counts of observations by bird species')
# Turning text of x-label
plt.xticks(rotation=90)
# Automatic chart resizing
plt.tight_layout()


# Converting a date column to datetime format
df['date'] = pd.to_datetime(df['date'])
# Grouping data by bird species
grouped_data = df.groupby('species')

# Plotting a graph for each bird species
plt.figure(figsize=(10, 6))
for species, species_data in grouped_data:
    species_data = species_data.sort_values(by='date')
    plt.plot(species_data['date'], species_data['count'], label=species, marker='o', linestyle='-')

# Customizing the appearance of the chart
plt.xlabel('Date')
plt.ylabel('Count of birds')
plt.title('Changes in bird population over time')
plt.xticks(rotation=45)
plt.legend(title='Kind of birds', loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
