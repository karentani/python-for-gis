"""
Zip up all the data in the unzipped folder and move it to the zipped folder
"""
import shutil

unzipped_gdb = r"C:\Users\nick.wilgruber\Desktop\Final_Delivery\Unzipped\STL.gdb"
unzipped_shapefile_folder = r"C:\Users\nick.wilgruber\Desktop\Final_Delivery\Unzipped\Shapefiles"
zipped_folder = r"C:\Users\nick.wilgruber\Desktop\Final_Delivery\Zipped"

shutil.make_archive(unzipped_gdb, "zip")
shutil.move(unzipped_gdb + ".zip", zipped_folder)
shutil.make_archive(unzipped_shapefile_folder, "zip")
shutil.move(unzipped_shapefile_folder + ".zip", zipped_folder)
