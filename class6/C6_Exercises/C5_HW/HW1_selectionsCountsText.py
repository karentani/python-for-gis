"""
Write the name of each Pittsburgh neighborhood and
the count of all Parks and Greenways in that neighborhood to a text file
"""
# Import modules
import arcpy
import os

arcpy.env.overwriteOutput = True

# Set variables
parks_feature_class = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5\C5_Data\PGH.gdb\Parks'
greenways_feature_class = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5\C5_Data\PGH.gdb\Greenways'
neighborhoods_feature_class = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5\C5_Data\PGH.gdb\Neighborhoods'

text_file_location = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5'
text_file = open(os.path.join(text_file_location, "ParkAndGreenwayCount.txt"), "w")

# Execute operation(s)
with arcpy.da.SearchCursor(neighborhoods_feature_class, ["neighborho", "hood_no"]) as cursor:
    for row in cursor:
        neighborhood_name = row[0]

        print "\nGetting park and greenway counts for " + neighborhood_name + ". . ."
        text_file.writelines("\nGetting park and greenway counts for " + neighborhood_name + ". . .")

        neighborhood_number = row[1]

        # Make a feature layer and select only a specific neighborhood
        arcpy.MakeFeatureLayer_management(neighborhoods_feature_class, "hood_layer")
        arcpy.SelectLayerByAttribute_management("hood_layer", where_clause="hood_no = " + str(neighborhood_number))

        # Select parks that intersect that neighborhood and get a count of those parks
        arcpy.MakeFeatureLayer_management(parks_feature_class, "parks_layer")
        arcpy.SelectLayerByLocation_management("parks_layer", "INTERSECT", "hood_layer")
        park_count = arcpy.GetCount_management("parks_layer")
        print "  Park count is: " + str(park_count)
        text_file.writelines("\n  Park count is: " + str(park_count))

        # Select greenways that intersect that neighborhood and get a count of them
        arcpy.MakeFeatureLayer_management(greenways_feature_class, "greenways_layer")
        arcpy.SelectLayerByLocation_management("greenways_layer", "INTERSECT", "hood_layer")
        greenway_count = arcpy.GetCount_management("greenways_layer")
        print "  Greenway count is: " + str(greenway_count)
        text_file.writelines("\n  Greenway count is: " + str(greenway_count))
        text_file.writelines("\n")

text_file.close()
