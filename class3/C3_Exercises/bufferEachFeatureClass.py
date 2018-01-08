"""
Buffer every feature class, except 'PlanningDistrict', in the 'Central_Phila' geodatabase by 50 meters
"""
# Import modules
import arcpy
import os

# Set variables
geodatabase = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class3\C3_Data\Central_Phila.gdb'
output_location = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class3\C3_Data\Central_Phila.gdb'
buffer_distance = '50 Meters'

# Execute operation
# Set the workspace and get feature class names
arcpy.env.workspace = geodatabase
feature_class_list = arcpy.ListFeatureClasses()

for feature_class in feature_class_list:

    if feature_class != 'PlanningDistrict':

        # Execute buffer on every feature class
        arcpy.Buffer_analysis(os.path.join(geodatabase, feature_class),
                              os.path.join(output_location, 'Buffered' + feature_class),
                              buffer_distance)
