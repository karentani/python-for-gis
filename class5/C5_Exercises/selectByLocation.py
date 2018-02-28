"""
Get a count of the number parks in the Bloomfield neighborhood of Pittsburgh

First create a Neighborhood layer and select for Bloomfield
Then create a Parks layer and select by location for parks within Bloomfield
Finally, print a count of the, now selected, Parks layer
"""
# Import modules
import arcpy

# Set variables
parks_feature_class = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5\C5_Data\PGH.gdb\Parks'
neighborhoods_feature_class = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5\C5_Data\PGH.gdb\Neighborhoods'

# Execute operation(s)
# Select only the Bloomfield neighborhood
arcpy.MakeFeatureLayer_management(neighborhoods_feature_class, "bloomfield_layer")
arcpy.SelectLayerByAttribute_management("bloomfield_layer", where_clause="neighborho = 'Bloomfield'")

# Select Parks within Bloomfield
arcpy.MakeFeatureLayer_management(parks_feature_class, "parks_layer")
arcpy.SelectLayerByLocation_management("parks_layer", "INTERSECT", "bloomfield_layer")
count = arcpy.GetCount_management("parks_layer")
print "There are " + str(count) + " parks in Bloomfield"
