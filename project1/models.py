from datetime import datetime

"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.




The `designation` should resolve to a string, the `name` should resolve to either a nonempty string or the value `None`, the `diameter` should resolve to a float (you should use `float('nan')` to represent an undefined diameter), and the `hazardous` flag should resolve to a boolean.

The `approaches` attribute, for now, can be an empty collection. In Task 2, you'll use the real data set to populate this collection with the real `CloseApproach` data.

The `__str__` method that you write is up to you - it'll determine how this object is printed, and should be human-readable. For inspiration, we adopted the following format:

```
>>> neo = ...
>>> print(neo)
NEO {fullname} has a diameter of {diameter:.3f} km and [is/is not] potentially hazardous.
>>> halley = ...
>>> print(halley)
NEO 433 (Eros) has a diameter of 16.840 km and is not potentially hazardous.
```

In the above, `{fullname}` is either `{designation} ({name})` if the `name` exists or simply `{designation}` otherwise. As a hint, this is a great opportunity for a property named `fullname`!


"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation, name = None, diameter = float('nan'), hazardous = False):

        """Create a new `NearEarthObject`.

        :param designation: string [required]
        :param name: string or None
        :diameter designation: float
        :param hazardous: boolean

        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.

        if not designation:
            raise TypeError("Missing designation")

        else:
            self.designation = designation

        self.name = (name if name else None)

        try:
            self.diameter = float (diameter)
        except ValueError as error:
            self.diameter = None
            
        self.hazardous = bool(hazardous)

        # Create an empty initial collection of linked approaches.
        self.approaches = []
        
    def add_approach(self, approach):
        self.approaches.append(approach)

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        pretty_print_name = self.name if self.name else "unnamed"
        return f"{self.designation} ({pretty_print_name})"

    def __str__(self):
        """Return `str(self)`."""
        pretty_print_hazardous = "is potentially hazardous" if self.hazardous else "is not potentially hazardous"
        return f"A NearEarthObject: {self.fullname!r} which has diameter {self.diameter:.3f}au and {pretty_print_hazardous}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")
                
    @staticmethod
    def fromData(line):
        pha = line.get('pha', '').upper()
        designation = line.get('pdes', '')
        name = line.get('name', None)
        diameter = line.get('diameter', float('nan'))
        hazardous = (pha == "Y")
        return NearEarthObject(designation = designation, name = name, diameter = diameter, hazardous = hazardous)


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation, time, distance, velocity):
        """Create a new `CloseApproach`.

        :param designation: designation (string)
        :param time: time (float)
        :param distance: distance (float)
        :param velocity: velocity (float)

        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.

        if not designation:
            raise TypeError("Missing designation")

        else:
            self.designation = designation

        self.time = time if isinstance(time, datetime) else datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """

        return datetime_to_str(self.time)

        
    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        pretty_print_neo = self.neo.fullname if self.neo else "unknown"
        pretty_print_hazardous = "hazardous" if (self.neo and self.neo.hazardous) else "non-hazardous"
        return f"A {pretty_print_hazardous} CloseApproach of the object {pretty_print_neo} at time {self.time}, at a closest approach distance of {self.distance:.2f}au and a velocity of {self.velocity:.2f}km/s"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
                
                
    @staticmethod
    def fromData(data):
        return CloseApproach(designation = data[0], time = cd_to_datetime(data[3]), distance = float(data[4]), velocity = float(data[7]))
