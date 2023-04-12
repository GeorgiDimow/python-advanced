from project.services.base_service import BaseService


class SecondaryService(BaseService):

    @property
    def get_capacity(self):
        return 15

    def __init__(self, name: str):
        super().__init__(name, self.get_capacity)

    def details(self):
        if self.robots:
            return f"{self.name} Secondary Service:\n" \
                   f"Robots: {' '.join(r.name for r in self.robots)}"

        return f"{self.name} Secondary Service:\n" \
               "Robots: none"
