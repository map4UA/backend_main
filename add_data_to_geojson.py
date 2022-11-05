import requests
from datasets.data import object
from datasets.main_data import main_geojson

class AddDataToGeoJSON:
    def __init__(self):
        self.base_url = "url"
        self.object = object

    def add_data(self):
        geojson = main_geojson
        response = geojson.append(self.object)
        print(geojson)
        return geojson

if __name__ == '__main__':
    add = AddDataToGeoJSON()
    add.add_data()
