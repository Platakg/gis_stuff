import shapefile
import csv
import urllib
'''
# generate projection file
def getWKT_PRJ (epsg_code):
    wkt = urllib.urlopen("http://spatialreference.org/ref/epsg/{0}/prettywkt/".format(epsg_code))
    remove_spaces = wkt.read().replace(" ","")
    output = remove_spaces.replace("\n", "")
    return output
'''
acled_shp = shapefile.Writer(shapefile.POINT)
acled_shp.autoBalance = 1

acled_shp.field("data_id", "C")
acled_shp.field("event_id_cnty", "C")
acled_shp.field("latitude", "C")
acled_shp.field("longitude", "C")
acled_shp.field("geo_precision", "C")

counter = 1

with open('/Users/kat/Desktop/python/postgis_data/test.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)

    for row in reader:
        data_id = row[0]
        event_id_cnty = row[1]
        latitude = row[2]
        longitude = row[3]
        geo_precision = row[4]

        acled_shp.point(float(longitude), float(latitude))
        # add attribute data
        acled_shp.record(data_id, event_id_cnty, geo_precision)

        print("Feature " + str(counter) + " added to shapefile.")
        counter += 1

    acled_shp.save("geo_project")
    