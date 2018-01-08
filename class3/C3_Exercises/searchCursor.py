"""
Use a SearchCursor to print the 'ASSET_NAME' of each record in the Parks feature class
"""
# Import modules
import arcpy

# Set variables
parks_fc = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class3\C3_Data\Central_Phila.gdb\Parks'
fields = ['ASSET_NAME', 'ADDRESS']

# Execute operation
with arcpy.da.SearchCursor(parks_fc, fields) as cursor:
    for row in cursor:
        print row[0] + ' is located at ' + row[1]
