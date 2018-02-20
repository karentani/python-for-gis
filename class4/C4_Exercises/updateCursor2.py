"""
In Central_Phila.gdb
Use an UpdateCursor to update Parks address... If ends in PKY change to PKWY or ends in BLV change to BLVD
"""

# Import modules
import arcpy

# Set variables
parks_fc = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class4\C4_Data\Central_Phila.gdb\Parks'
fields = ['ADDRESS']

# Execute operation
with arcpy.da.UpdateCursor(parks_fc, fields) as cursor:
    for row in cursor:

        address = row[0]

        if address.endswith('PKY'):
            row[0] = address.replace('PKY', 'PKWY')
            cursor.updateRow(row)

        elif address.endswith('BLV'):
            row[0] = address.replace('BLV', 'BLVD')
            cursor.updateRow(row)
