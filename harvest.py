############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.extend(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

        # Fill in the rest


def make_melon_types():
    """Returns a listmy of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green',
                     True, True, 'Muskmelon')
    musk.add_pairing(['mint'])
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange',
                     True, False,  'Casaba')
    casaba.add_pairing(['mint', 'strawberries'])
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', True, False, 'Crenshaw')
    crenshaw.add_pairing(['proscuitto'])
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', True, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing(['ice cream'])
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon_type in melon_types:
        print "{} pairs well with".format(melon_type.name)
        pairings = melon_type.pairings
        for pairing in pairings:
            print "- {}".format(pairing)
        print ""

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    codes = {}
    for melon_type in melon_types:
        codes[melon_type.code] = melon_type
    # Fill in the rest
    return codes
############
# Part 2   #
############

# all_melon_types = make_melon_types()
# make_melon

class Melon(object):
    """A melon in a melon harvest."""
    self.all_melon_types = make_melon_type_lookup(make_melon_types())

    def __init__ (self, melon_code, shape_rating, color_rating, from_field, harvested_by):
        self.melon_type = self.all_melon_types[melon_code]
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.from_field = from_field
        self.harvested_by = harvested_by 

    def is_sellable():
        if (self.from_field != 3) and (self.shape_rating >= 5) and (self.color_rating >= 5):
            return True
        return False


    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melon_objects = []

    melon1 = Melon('yw', 8, 7, 2, 'Sheila')
    melon_objects.append(melon1)

    melon2 = Melon('yw', 3, 4, 2, 'Shei1a')
    melon_objects.append(melon2)

    melon3 = Melon('yw', 9, 8, 3, 'Sheila')
    melon_objects.append(melon3)

    melon4 = Melon('cas', 10, 6, 35, 'Sheila')
    melon_objects.append(melon4)

    melon5 = Melon('cren',8,9,35,'Michael')
    melon_objects.append(melon5)

    melon6 = Melon('cren', 8, 2, 35, 'Michael')
    melon_objects.append(melon6)

    melon7 = Melon('cren', 6,7,4, 'Michael')
    melon_objects.append(melon7)

    melon8 = Melon('musk', 6,7,4, 'Michael')
    melon_objects.append(melon8)

    melon9 = Melon('yw',7,10,3,'Sheila')
    melon_objects.append(melon9)

    return melon_objects


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


