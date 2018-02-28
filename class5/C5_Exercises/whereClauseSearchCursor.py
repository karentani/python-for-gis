"""
Using a where clause to limit to attribute table rows that the search cursor has to loop through
"""
# Import modules
import arcpy

# Set variables
parks_feature_class = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class5\C5_Data\PGH.gdb\Parks'
fields = ['updatepknm']
clause = "final_cat = 'Neighborhood Park'"

# Execute operation
with arcpy.da.SearchCursor(parks_feature_class, fields, where_clause=clause) as cursor:
    for row in cursor:
        print row[0]
