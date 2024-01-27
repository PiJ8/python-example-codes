#Example of plot chart from 3 csv data source

from matplotlib import pyplot
import csv
import math
import statistics
import random

#Extra markers
global_economy_crises_years = [
    {"name": "Great Depression", "start_year": 1929, "end_year": 1939},
    {"name": "1970s Oil Crisis", "start_year": 1973, "end_year": 1978},  # The crisis extended over a few years
    {"name": "Latin American Debt Crisis", "start_year": 1980, "end_year": 1989},
    {"name": "Asian Financial Crisis", "start_year": 1997, "end_year": 1998},
    {"name": "Dot-com Bubble Burst", "start_year": 2000, "end_year": 2002},
    {"name": "Global Financial Crisis", "start_year": 2007, "end_year": 2008},
    {"name": "Eurozone Crisis", "start_year": 2010, "end_year": 2012},
    {"name": "COVID-19 Pandemic", "start_year": 2020, "end_year": 2022},  
]

# region Functions
def read_csv(file_path):
    """
    Read a CSV file and return a list of dictionaries.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - list of dict: A list of dictionaries representing each row in the CSV.
    """
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter='\t')
        data_list = list(csv_reader)
    
    return data_list
# endregion

# region Data Processing
# Open and read the csv file
crude_oil_data = sorted(read_csv('data\crude_oil.csv'), key=lambda x: x['Year']) 
snp500_data = sorted(read_csv('data\snp500.csv'), key=lambda x: x['Year'])  
gold_data = sorted(read_csv('data\gold.csv'), key=lambda x: x['Year'])

# Process the crises list to be plot as scatter
crises_x_values = [int(item['start_year']) for item in global_economy_crises_years]

# Plot scatter at secondary axis mean height
mean_value = statistics.mean([float(item['Average Closing Price'].strip('$').replace(',', '')) for item in crude_oil_data])
crises_y_values = [mean_value for item in global_economy_crises_years]

crises_colors = [random.randint(0,50) for item in global_economy_crises_years]
crises_sizes = [300*(item['end_year']-item['start_year']) for item in global_economy_crises_years]

# end region

# region Plot Chart
# Plotting the data
fig, main_axis = pyplot.subplots(figsize=(10, 6))
main_axis.plot([int(item['Year']) for item in snp500_data], [float(item['Average Closing Price'].strip('$').replace(',', '')) for item in snp500_data], label='SNP500 Price', marker='o')
main_axis.plot([int(item['Year']) for item in gold_data], [float(item['Average Closing Price'].strip('$').replace(',', '')) for item in gold_data], label='Gold Price', marker='o')

secondary_axis = main_axis.twinx()
secondary_axis.plot([int(item['Year']) for item in crude_oil_data], [float(item['Average Closing Price'].strip('$').replace(',', '')) for item in crude_oil_data], label='Crude Oil Price', color='tab:red', marker='o')

# Create scatter plot for economy crises
secondary_axis.scatter(crises_x_values, crises_y_values, c=crises_colors, s=crises_sizes, alpha=0.5, label='Economy Crisis')

# Adding labels and title
main_axis.set_xlabel('Year')
main_axis.set_ylabel('Price in USD')
secondary_axis.set_ylabel('Price in USD')

pyplot.title('SNP500, Crude Oil, and Gold Prices in USD Over Years')

# Sub axis will overwrite the main axis legend, combine legends and display via sub axis
ma_lines, ma_labels = main_axis.get_legend_handles_labels()
sa_lines2, sa_labels2 = secondary_axis.get_legend_handles_labels()
legend = secondary_axis.legend(ma_lines + sa_lines2, ma_labels + sa_labels2, loc='upper right')

# Resize the 4th legend marker/circle for scatter into smaller size
legend.legendHandles[3]._sizes = [50]
pyplot.grid(True)
pyplot.show()
# endregion
