def select_frontyard_polygon(split_plots, buildings, ouput_path_file):
    import pandas as pd
    import geopandas as gpd
    import matplotlib.pyplot as plt
    import numpy as np

    #afther splitting the polygons in arcgis pro, the front yards need to be selected

    #open split plots file
    split_plots = gpd.read_file(split_plots)

    #open building file
    buildings = gpd.read_file(buildings)

    #Spatial join to identify overlapping polygons
    joined = gpd.sjoin(split_plots, buildings, how="left", op="intersects")


    #Initialize an empty DataFrame to store the selected polygons
    selected_polygons = []

    # Iterate over unique CAPAKEY values
    for capakey in joined["CAPAKEY"].unique():
        # Filter joined DataFrame for the current CAPAKEY
        subset = joined[joined["CAPAKEY"] == capakey]

        # Check if there's more than one polygon in the original plots layer with the same CAPAKEY
        if len(split_plots[split_plots["CAPAKEY"] == capakey]) > 1:
            # Check if there's only one polygon in the subset
            if len(subset) > 1:
                # Calculate the overlap area for each polygon in the subset
                overlap_areas = subset.geometry.intersection(subset.geometry).area

                # Find the minimum overlap area
                min_overlap_area = overlap_areas.min()

                # If the minimum overlap area is 0, assign a large value (np.inf) to ensure it's selected
                if min_overlap_area == 0:
                    min_overlap_area = np.inf

                # Find the index of the polygon with the minimum overlap area
                min_overlap_index = overlap_areas.idxmin()

                # Append the polygon with the minimum overlap area to the selected_polygons list
                selected_polygons.append(split_plots.loc[min_overlap_index])

    # Create a GeoDataFrame from the selected polygons
    selected_plots_gdf = gpd.GeoDataFrame(selected_polygons, crs=split_plots.crs)

    # Export to a shapefile
    selected_plots_gdf.to_file(ouput_path_file, driver='ESRI Shapefile')

    """
    # Plot the selected plots
    fig, ax = plt.subplots(figsize=(10, 10))
    selected_plots_gdf.plot(ax=ax, edgecolor='black', facecolor='none')

    # Add title and labels
    ax.set_title('Selected Plots')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    # Show the plot
    plt.show()
    """

    return print("Finished")

split_plots_path = r'C:\Users\U0167935\Documents\ArcGIS\Projects\Residential_plots_spatialjoin.shp'
buildings_path = r'C:\Users\U0167935\Documents\ArcGIS\Projects\residential_buildings_study_area.shp'
output_path = 'C:/Users/U0167935/Documents/trial_frontpoints/frontyards.shp'
select_frontyard_polygon(split_plots_path, buildings_path, output_path)