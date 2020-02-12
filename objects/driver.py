class Driver:
    def __init__(self, name, address, city, state, zip_code, phone, email):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __eq__(self, other):
        if not isinstance(other, Driver):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == other.name and self.address == other.address and \
               self.city == other.city and self.state == other.state and self.zip_code == other.zip_code \
               and self.phone == other.phone and self.email == other.email
