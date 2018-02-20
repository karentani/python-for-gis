"""
Use an InsertCursor to add a row to the parks feature class
"""
# Import modules
import arcpy

# Set variables
parks_fc = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class4\C4_Data\Central_Phila.gdb\Parks'


# Execute operation
with arcpy.da.InsertCursor(parks_fc, ['ASSET_NAME', 'ADDRESS', 'ZIPCODE']) as cursor:
    cursor.insertRow(('Made-up Park', '122 NOTREAL AVE', 19122))
