"""
Create the folder structure
"""
import os

delivery_folder = r"C:\Users\nick.wilgruber\Desktop\Final_Delivery"

# Building out the delivery folder structure
# Create primary directory
if not os.path.exists(os.path.join(delivery_folder)):
    os.makedirs(delivery_folder)

# Create Zipped and Unzipped sub folders
if not os.path.exists(os.path.join(delivery_folder, "Unzipped")):
    os.makedirs(os.path.join(delivery_folder, "Unzipped"))

if not os.path.exists(os.path.join(delivery_folder, "Zipped")):
    os.makedirs(os.path.join(delivery_folder, "Zipped"))

# Create Shapefile folder
if not os.path.exists(os.path.join(delivery_folder, "Unzipped", "Shapefiles")):
    os.makedirs(os.path.join(delivery_folder, "Unzipped", "Shapefiles"))









