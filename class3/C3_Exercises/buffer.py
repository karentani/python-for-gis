"""
Buffer the StreetTrees feature class by 20 meters
"""
# Import modules
import arcpy

# Set variables
in_features = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class3\C3_Data\Central_Phila.gdb\StreetTrees'
out_feature_class = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class3\C3_Data\Central_Phila.gdb\BuffStreetTrees'
buffer_distance = '20 Meters'

# Execute operation
arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance)

# Go look in the out location. Did the buffer happen?
