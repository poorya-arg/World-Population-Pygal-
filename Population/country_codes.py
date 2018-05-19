from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """return pygal 2-digit country code"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
