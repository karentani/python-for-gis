"""
Move, Convert, Rename data from STL.gdb to the newly created folder structure
"""
import os
import arcpy

delivery_folder = r"C:\Users\nick.wilgruber\Desktop\Final_Delivery"
input_gdb = r"C:\Wilgruber\Teaching\Python_for_GIS_series\Class6\C6_Data\STL.gdb"

arcpy.Copy_management(input_gdb, os.path.join(delivery_folder, "Unzipped", "STL.gdb"))

arcpy.env.workspace = os.path.join(delivery_folder, "Unzipped", "STL.gdb")
fc_list = arcpy.ListFeatureClasses()

for fc in fc_list:
    arcpy.CopyFeatures_management(fc, os.path.join(delivery_folder, "Unzipped", "Shapefiles", fc + ".shp"))
