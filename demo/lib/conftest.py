import pytest

@pytest.fixture
def house_test_data():
    return { 
        "name": "Test House",
        "region": "Test Region",
        "coatOfArms": "Test Insignia"
    }


@pytest.fixture()
def house_test_list():
    return [
        { 
            "name": "Test House",
            "region": "Test Region",
            "coatOfArms": "Test Insignia"
        },
        { 
            "name": "Test House 2",
            "region": "Test Region 2",
            "coatOfArms": "Test Insignia 2"
        }
    ]