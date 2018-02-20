"""
In Central_Phila.gdb
Use arcpy.Clip_analysis() to find all the StreetTrees located in Parks
"""
# Import modules
import arcpy

# Set variables
input_feature = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class3\C3_Data\Central_Phila.gdb\StreetTrees'
clip_feature = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class3\C3_Data\Central_Phila.gdb\Parks'
output_fc = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class3\C3_Data\Central_Phila.gdb\StreetTreesClipped'

# Execute operation
arcpy.Clip_analysis(input_feature, clip_feature, output_fc)
