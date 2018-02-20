"""
String methods for manipulating strings
Walkthrough each quick
"""

road_list = ["10th Street", "Siegfried Avenue", "Main Street", "6th Avenue", "Broad Street", "Frankford Avenue"]

# startswith / endswith
for road in road_list:
    if road.endswith("Street"):
        print road

# upper / lower
# for road in road_list:
#     print road.upper()

# replace
# for road in road_list:
#     if road.endswith("Street"):
#         print road.replace("Street", "Circle")

# split
# for road in road_list:
#     print road.split(" ")[0]


# slice
# for road in road_list:
#     if road.endswith("Street"):
#         print road[:-4]
#     elif road.endswith("Avenue"):
#         print road[:-3]
