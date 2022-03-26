from .land import Land


class ListLandTransport:
    def __init__(self):
        self.land_list = []

    def add_land(self, land: Land):
        self.land_list.append(land)

    def display(self):
        for land in self.land_list:
            print(land.display_data())
