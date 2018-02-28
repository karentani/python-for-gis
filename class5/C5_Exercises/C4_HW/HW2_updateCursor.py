"""
In the Parks feature class,
use an Update Cursor and string manipulation to update the 'DESCRIPTIO' field to Park
when the 'USE_' field is any type of Park
(Park- Mini, Park- Linear/Parkway, Park- Square/Plaza, Park- Neighborhood, etc.)
"""
# Import modules
import arcpy

# Set variables
parks_feature_class = r'C:\Wilgruber\Teaching\Python_for_GIS_series\Class4\C4_Data\Central_Phila.gdb\Parks'

# Execute operation
with arcpy.da.UpdateCursor(parks_feature_class, ['USE_', 'DESCRIPTIO']) as cursor:
    for row in cursor:
        if row[0] is not None and row[0].startswith("Park"):
            row[1] = "Park"
            cursor.updateRow(row)
