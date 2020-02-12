class Vehicle:
    def __init__(self, make_model, year, color, engine, name, sponsors, club):
        self.make_model = make_model
        self.year = year
        self.color = color
        self.engine = engine
        self.name = name
        self.sponsors = sponsors
        self.club = club

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.make_model == other.make_model and self.year == other.year and self.color == other.color and \
               self.engine == other.engine and self.name == other.name and self.sponsors == other.sponsors and \
               self.club == other.club
