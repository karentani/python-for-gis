"""
Print the name of every feature class in Central_Phila.gdb
"""
# Import modules
import arcpy

# Set variables
# Change this to wherever you saved the class data...
geodatabase = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class3\C3_Data\Central_Phila.gdb'

# Execute operation
# Set the workspace. This tells arcpy to use this path for any subsequent operation.
arcpy.env.workspace = geodatabase
feature_class_list = arcpy.ListFeatureClasses()

for feature_class in feature_class_list:
    print feature_class
