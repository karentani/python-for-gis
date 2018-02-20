"""
In Central_Phila.gdb
Use an UpdateCursor to update the misspelled records to 'Land'
"""

# Import modules
import arcpy

# Set variables
parks_fc = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class4\C4_Data\Central_Phila.gdb\Parks'
fields = ['TYPE']

# Execute operation
with arcpy.da.UpdateCursor(parks_fc, fields) as cursor:
    for row in cursor:
        if row[0] == 'Lad' or row[0] == 'Lan':
            row[0] = 'Land'
            cursor.updateRow(row)
