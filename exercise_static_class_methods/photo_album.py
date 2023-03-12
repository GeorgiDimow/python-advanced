from math import ceil


class PhotoAlbum:
    PHOTOS_ON_A_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list[list] = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_ON_A_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < self.PHOTOS_ON_A_PAGE:
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"

        return "No more free slots"

    def display(self):
        result = ["-" * 11]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append("-" * 11)

        return "\n".join(result)