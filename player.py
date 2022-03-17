from fish_animation import FishAnimation

class Player(FishAnimation):
    def __init__(self, spritesheet_path):
        super().__init__(spritesheet_path)

        self.scale = 0.5
    