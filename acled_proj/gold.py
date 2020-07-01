# import libraries
import shapefile, csv

# funtion to generate a .prj file
def getWKT_PRJ (epsg_code):
    import urllib.request
    wkt = urllib.request.urlopen("http://spatialreference.org/ref/epsg/{0}/prettywkt/".format(epsg_code))
    text = wkt.read().decode("utf-8")
    remove_spaces = text.replace(" ","")
    output = remove_spaces.replace("\n", "")
    return output

# create a point shapefile
acled_shp = shapefile.Writer('shapefiles/output', shapefile.POINT)

# for every record there must be a corresponding geometry.
acled_shp.autoBalance = 1

# create the field names and data type for each.
acled_shp.field("data_id", "C")
acled_shp.field("event_id_cnty", "C")
acled_shp.field("latitude", "C")
acled_shp.field("longitude", "C")
acled_shp.field("geo_precision", "C")

# count the features
counter = 1

# access the CSV file
with open('2020-04-Iraq.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # skip the header
    next(reader, None)

#loop through each of the rows and assign the attributes to variables
    for row in reader:
        data_id = row[0]
        event_id_cnty = row[1]
        latitude = row[2]
        longitude = row[3]
        geo_precision = row[4]

  # create the point geometry
        acled_shp.point(float(longitude),float(latitude))
        #coord = (float(longitude), float(latitude))
  # add attribute data
        #row_list = [data_id, event_id_cnty, geo_precision]
        #acled_shp.record(*row_list)
        acled_shp.record(data_id='data_id', event_id_cnty='event_id_cnty', geo_precision='geo_precision')

        print("Feature " + str(counter) + " added to Shapefile.")
        counter = counter + 1

# save the Shapefile
acled_shp.close()

# create a projection file
prj = open("shapefiles/output.prj", "w")
epsg = getWKT_PRJ("4326")
prj.write(epsg)
prj.close()