from typing import List

from project.band import Band
from project.band_members.musician import Musician
from project.concert import Concert
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer


class ConcertTrackerApp:

    @property
    def get_valid_musicians(self):
        return {
            "Guitarist": Guitarist,
            "Drummer": Drummer,
            "Singer": Singer
        }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.get_valid_musicians:
            raise ValueError("Invalid musician type!")

        musician = [m for m in self.musicians if m.name == name]

        if musician:
            raise Exception(f"{name} is already a musician!")

        musician = self.get_valid_musicians[musician_type](name, age)
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = [b for b in self.bands if b.name == name]

        if band:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = [c for c in self.concerts if c.place == place]

        if concert:
            raise Exception(f"{place} is already registered for {concert[0].genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = next(filter(lambda m: musician_name == m.name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: band_name == b.name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = next(filter(lambda b: band_name == b.name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: musician_name == m.name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        if musician not in band.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda b: band_name == b.name, self.bands))
        concert = next(filter(lambda c: concert_place == c.place, self.concerts))

        try:
            singer = next(filter(lambda m: m.__class__.__name__ == "Singer", band.members))
            drummer = next(filter(lambda m: m.__class__.__name__ == "Drummer", band.members))
            guitarist = next(filter(lambda m: m.__class__.__name__ == "Guitarist", band.members))
        except StopIteration:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if "play the drums with drumsticks" in drummer.skills and "sing high pitch notes" in singer.skills \
                and "play rock" in guitarist.skills and concert.genre == "Rock":
            pass
        elif "play the drums with drumsticks" in drummer.skills and "sing low pitch notes" in singer.skills \
                and "play metal" in guitarist.skills and concert.genre == "Metal":
            pass
        elif "play the drums with drum brushes" in drummer.skills and "sing high pitch notes" in singer.skills \
                and "sing low pitch notes" in singer.skills and "play jazz" in guitarist.skills \
                and concert.genre == "Jazz":
            pass
        else:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
