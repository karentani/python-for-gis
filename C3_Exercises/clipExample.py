"""
Use Clip_analysis to... clip stuff...
http://pro.arcgis.com/en/pro-app/tool-reference/analysis/clip.htm
"""

# Import modules
import arcpy

# Set variables
in_features = r"C:\Wilgruber\MajorRoads.shp"
clip_features = r"C:\Wilgruber\AOI.shp"
out_feature_class = r"C:\Wilgruber\MajorRoadsClipped.shp"

# Execute Clip
arcpy.Clip_analysis(in_features, clip_features, out_feature_class)
