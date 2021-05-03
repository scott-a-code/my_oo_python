from .house import House

class TestHouseCase():
    def test_name(self, house_test_data):
        house = House(house_test_data)
        assert house.name == 'Test House'

    def test_region(self, house_test_data):
        house = House(house_test_data)
        assert house.region == 'Test Region'

    def test_insignia(self, house_test_data):
        house = House(house_test_data)
        assert house.insignia == 'Test Insignia'

    def test_save(self, house_test_data):
        start_len = len(House.all)
        house = House(house_test_data)
        assert len(House.all) == start_len + 1

    def test_find_by_input(self, house_test_list):
        House.all = []
        for data in house_test_list:
            House(data)
        house = House.find_by_input("2")
        assert house.name == house_test_list[1]['name']
