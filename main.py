import requests


class GetMaps:
    def __init__(self):
        self.base_url = 'https://api.maptiler.com/'
        self.api_key = 'GpMC1KBXPvnBEnQteMcN'
        self.api_key_1 = "FmUCbxZZXCT1hXKQwg5i"
        self.railway_maps = "1dafa1a7-f820-418b-a7b1-d321bdf8d876"
        self.airfield_maps = "bfd13fb2-070d-4090-8d72-1f44a4472352"
        self.lep = "a47f06f8-bafa-4478-9b5b-b7e219b96bad"

    def get_lep_ways(self):
        response = requests.get(url=f"{self.base_url}maps/{self.lep}/?key={self.api_key_1}")
        return response.text

    def get_maps_railway_stations(self):
        response = requests.get(url=f'{self.base_url}maps/{self.railway_maps}/?key={self.api_key_1}')
        print(response)
        return response

    def get_maps_airfields(self):
        response = requests.get(url=f"{self.base_url}maps/{self.airfield_maps}/?key={self.api_key_1}")
        return response.text

    def get_maps_json(self):
        response = requests.get(url=f'{self.base_url}maps/openstreetmap/style.json?key={self.api_key}')
        print(response)
        return response

    def get_tiles(self):
        response = requests.get(url=f'{self.base_url}tiles/satellite/?key={self.api_key}')
        print(response)
        return response
    def get_rails_json(self):
        response = requests.get(url=f'{self.base_url}maps/openstreetmap/style.json?key={self.api_key}').json()
        rails = [each for each in response.get("layers") if "rail" in each.get("id")]
        return rails

    def get_data_by_id(self):
        endpoint = f"{self.base_url}data/6e9fa66c-b559-4cd4-9f1c-991ccf551d87/features.json?key=FmUCbxZZXCT1hXKQwg5i"
        response = requests.get(url=endpoint)
        return response.json()

    # def compile_map_with_dataset(self):
    #     dataset = GetMaps.get_data_by_id(self)
    #     map = GetMaps.get_maps(self)


if __name__ == '__main__':
    get_maps = GetMaps()
    get_maps.get_lep_ways()