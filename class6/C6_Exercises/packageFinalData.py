"""
Create a script to package the Class 6 STL.gdb for delivery
"""
import arcpy
import os
import shutil

delivery_folder = r"C:\Users\nick.wilgruber\Desktop\Final_Delivery"
input_gdb = r"C:\Wilgruber\Teaching\Python_for_GIS_series\Class6\C6_Data\STL.gdb"

# Building out the delivery folder structure
if not os.path.exists(os.path.join(delivery_folder)):
    os.makedirs(delivery_folder)

if not os.path.exists(os.path.join(delivery_folder, "Unzipped")):
    os.makedirs(os.path.join(delivery_folder, "Unzipped"))

if not os.path.exists(os.path.join(delivery_folder, "Zipped")):
    os.makedirs(os.path.join(delivery_folder, "Zipped"))

if not os.path.exists(os.path.join(delivery_folder, "Unzipped", "Shapefiles")):
    os.makedirs(os.path.join(delivery_folder, "Unzipped", "Shapefiles"))

# Moving, converting, and renaming data
arcpy.Copy_management(input_gdb, os.path.join(delivery_folder, "Unzipped", "STL.gdb"))

arcpy.env.workspace = os.path.join(delivery_folder, "Unzipped", "STL.gdb")
fc_list = arcpy.ListFeatureClasses()

for fc in fc_list:
    arcpy.CopyFeatures_management(fc, os.path.join(delivery_folder, "Unzipped", "Shapefiles", fc + ".shp"))

# Zipping
unzipped_gdb = os.path.join(delivery_folder, "Unzipped", "STL.gdb")
unzipped_shapefile_folder = os.path.join(delivery_folder, "Unzipped", "Shapefiles")
zipped_folder = r"C:\Users\nick.wilgruber\Desktop\Final_Delivery\Zipped"

shutil.make_archive(unzipped_gdb, "zip")
shutil.move(unzipped_gdb + ".zip", zipped_folder)
shutil.make_archive(unzipped_shapefile_folder, "zip")
shutil.move(unzipped_shapefile_folder + ".zip", zipped_folder)
