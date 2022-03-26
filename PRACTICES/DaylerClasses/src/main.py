from PRACTICES.DaylerClasses.src.classes.bicycle import Bicycle
from PRACTICES.DaylerClasses.src.classes.car import Car
from PRACTICES.DaylerClasses.src.classes.list_land_transport import ListLandTransport


def main():
    list_land = ListLandTransport()
    land1 = Bicycle("my bicycle", 100, True, False)
    land2 = Car("my car", 2000, False, True)

    list_land.add_land(land1)
    list_land.add_land(land2)

    list_land.display()


if __name__ == "__main__":
    main()
