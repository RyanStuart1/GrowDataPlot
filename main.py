import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def load_and_clean_data(file_path):
    """Reads in the data from the csv and cleans the grow locations data."""

    df = pd.read_csv(file_path) # Loads the data from csv

    df = df.dropna() # Removes rows with missing vlaues

    df.rename(columns={'Longitude': 'Latitude', 'Latitude': 'Longitude'}, inplace=True) # Renames columns for correct longitude and latitude mapping

    df[['Latitude', 'Longitude']] = df[['Latitude', 'Longitude']].apply(pd.to_numeric) # Converts columns from strings to numeric

    bounding_box_df = df.query('50.681 <= Latitude <= 57.985 and -10.592 <= Longitude <= 1.6848') # Filter rows within the bounding box
    
    return bounding_box_df

def plot_locations(data, map_image_path, output_path):
    """Plots the grow location dataset onto a map of the UK."""
    
    plt.rcParams["figure.figsize"] = [4.0, 4.0] # Set up the plot appearance
    plt.rcParams["figure.autolayout"] = True
    uk_map = plt.imread(map_image_path) # Loads the image of the map

    _, ax = plt.subplots() # Creates the figure and axis
    ax.imshow(uk_map, extent=[-10.592, 1.6848, 50.681, 57.985])

    
    plt.yticks(np.arange(51, 58, 1)) # Configure axis ticks

    longitudes = data['Longitude'].to_numpy() # Extract longitude as arrays
    latitudes = data['Latitude'].to_numpy() # Extract latitude as arrays

    for lon, lat in zip(longitudes, latitudes): # Plots each grow datapoint as a red circle
        circle = Circle((lon, lat), radius=0.05, color='red')
        ax.add_patch(circle)

    plt.title("Grow Dataset Plot") # Title of plot
    plt.savefig(output_path) # Saves the figure
    plt.show() # Shows the figure

def main():
    data_file = "C:/Users/PC/Desktop/PythonAssignment2/GrowLocations.csv"
    map_image = "C:/Users/PC/Desktop/PythonAssignment2/map7.png"
    output_image = "C:/Users/PC/Desktop/PythonAssignment2/GrowDataVisualisation.png"

    cleaned_data = load_and_clean_data(data_file) # Load and manipulates data from the csv

    plot_locations(cleaned_data, map_image, output_image) # Plots the data from the manipulated csv to the map returning the final figure

if __name__ == "__main__":
    main()
