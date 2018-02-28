"""
Making a feature layer in memory, then selecting by attributes where Parks acreage > 10.0
Saving as a shapefile to visually show that the selection worked.
"""
# Import modules
import arcpy
import os

# Set variables
gdb = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5\C5_Data\PGH.gdb'
parks_feature_class = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5\C5_Data\PGH.gdb\Parks'
where_clause = "acreage > 10.0"

# Execute operation(s)
arcpy.MakeFeatureLayer_management(parks_feature_class, "parks_layer")
arcpy.SelectLayerByAttribute_management("parks_layer", where_clause=where_clause)

# Saving the output to a shapefile to show that the selection worked successfully
arcpy.CopyFeatures_management("parks_layer", os.path.join(gdb, "Parks_selection"))
