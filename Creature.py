from Object import Object


class Creature(Object):
    def __init__(self):
        super().__init__(15, 100)

    def play(self, cells):
        action, place = "Move", "f"
        return action, place
