from random import choices, randint

import arcade

from fish_animation import FishAnimation
from player import Direction
import game_constants as gc

FISH_COLOR_TO_PATH = {
    1: "assets/2dfish/spritesheets/__cartoon_fish_06_black_idle.png",
    2: "assets/2dfish/spritesheets/__cartoon_fish_06_blue_idle.png",
    3: "assets/2dfish/spritesheets/__cartoon_fish_06_green_idle.png",
    4: "assets/2dfish/spritesheets/__cartoon_fish_06_purple_idle.png",
    5: "assets/2dfish/spritesheets/__cartoon_fish_06_red_idle.png",
}

FISH_SIZE_TO_SCALE = {
    'XXXS': 0.10,
    'XXS': 0.15,
    'XS': 0.20,
    'S': 0.25,
    'M': 0.30,
    'ML': 0.35,
    'L': 0.40,
    'XL': 0.60,
}

FISH_SCALE = ['XXXS', 'XXS', 'XS', 'S', 'M', 'ML', 'L', 'XL']


class EnemyFish(FishAnimation):
    SMALL_ENEMY_SPEED = 5.0
    MEDIUM_ENEMY_SPEED = 4.0
    LARGE_ENEMY_SPEED = 2.0

    def __init__(self, direction, spawn_point):
        # Randomize the fish color and size
        fish_color = randint(1, 5)
        fish_scale = choices(FISH_SCALE, weights=(70, 55, 45, 35, 30, 25, 20, 15), k=1)
        flipped = False if direction == Direction.LEFT else True

        super().__init__(
            FISH_COLOR_TO_PATH[fish_color], 
            flipped, 
            FISH_SIZE_TO_SCALE[fish_scale[0]]
        )

        if fish_scale[0] in FISH_SCALE[0:2]:
            self.change_x = EnemyFish.SMALL_ENEMY_SPEED
        elif fish_scale[0] in FISH_SCALE[3:5]:
            self.change_x = EnemyFish.MEDIUM_ENEMY_SPEED
        else:
            self.change_x = EnemyFish.LARGE_ENEMY_SPEED

        self.direction = direction
        self.center_x = spawn_point[0]
        self.center_y = spawn_point[1]

    def update(self):
        if self.direction == Direction.LEFT:
            self.center_x += -self.change_x
        else:
            self.center_x += self.change_x

        # Are we going out of screen? If so, despawn
        if self.direction == Direction.LEFT:
            if self.center_x < 0:
                self.remove_from_sprite_lists()
                return
        else:
            if self.center_x > gc.SCREEN_WIDTH:
                self.remove_from_sprite_lists()
                return

        
        return super().on_update()