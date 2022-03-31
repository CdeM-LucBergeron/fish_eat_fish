import arcade

from fish_animation import FishAnimation

class EnemyFish(FishAnimation):
    def __init__(self, spritesheet_path, flip=False):
        super().__init__(spritesheet_path, flip)

    def update(self):
        return super().on_update()