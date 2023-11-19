"""
CP1404 prac_09
band.py
"""


class Band:
    """Band class."""

    def __init__(self, band_name):
        """Initialise a band."""
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.band_name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add a musician to musicians."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument for each musician."""
        play_string = [musician.play() for musician in self.musicians]
        return "\n".join(play_string)
