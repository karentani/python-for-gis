"""
In Central_Phila.gdb
Use a SearchCursor to count the number of avenues in
Central Philadelphia based on the StreetCenterlines 'ST_TYPE' field
"""
# Import modules
import arcpy

# Set variables
streets_fc = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class3\C3_Data\Central_Phila.gdb\StreetCenterlines'
fields = ['ST_TYPE']

# Execute operation
count = 0

with arcpy.da.SearchCursor(streets_fc, fields) as cursor:
    for row in cursor:
        if row[0] == 'AVE':
            count += 1

print count
