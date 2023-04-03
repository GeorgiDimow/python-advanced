class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}
        self.guild: str = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost

            return f"Skill {skill_name} added to the collection of the player {self.name}"

        return "Skill already added"

    def player_info(self):
        stats = f"Name: {self.name}\n" \
                f"Guild: {self.guild}\n" \
                f"HP: {self.hp}\n" \
                f"MP: {self.mp}\n"

        str_skills = '\n'.join([f"==={skill[0]} - {skill[1]}" for skill in self.skills.items()])

        return stats + str_skills
