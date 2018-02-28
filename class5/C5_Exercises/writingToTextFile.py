"""
Using a search cursor to print all the feature classes in our PGH.gdb
Writing the name of the gdb and all its feature classes to a text file
"""

# Import modules
import arcpy
import os

# Set variables
pgh_gdb = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5\C5_Data\PGH.gdb'
text_file_location = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5'
text_file = open(os.path.join(text_file_location, "FeatureClasses.txt"), "w")

# Execute operation(s)
arcpy.env.workspace = pgh_gdb
feature_class_list = arcpy.ListFeatureClasses()

gdb_name = os.path.basename(pgh_gdb)
print "\nGetting feature class names for " + gdb_name + ". . ."
text_file.writelines("Getting feature class names for " + gdb_name + ". . .")

for feature_class in feature_class_list:
    print "  " + feature_class
    text_file.writelines("\n  " + feature_class)

text_file.close()
