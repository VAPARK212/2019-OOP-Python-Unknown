from requests import get

loc = 'https://ipapi.co/'

class get_local():
    def get_city(self):
        return get(loc+'city/').text

    def get_region(self):
        return get(loc+'region/').text

    def get_postal_code(self):
        return get(loc+'postal/').text

    def get_x(self):
        return get(loc+'longitude/').text

    def get_y(self):
        return get(loc+'latitude/').text


if __name__ == '__main__':
    local = get_local()
    print(local.get_postal_code())
    print(local.get_x(), local.get_y())
