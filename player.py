from enum import Enum
from typing import DefaultDict

from fish_animation import FishAnimation


class Direction(Enum):
    LEFT = 0
    RIGHT = 1

class Player:
    MOVEMENT_SPEED = 5.0
    PLAYER_LIVES = 3
    
    def __init__(self, spritesheet_path):
        self.left_animation = FishAnimation(spritesheet_path, scale=0.15)
        self.right_animation = FishAnimation(spritesheet_path, flip=True, scale=0.15)
        self.current_animation = None

        self.direction = Direction.LEFT
        if self.direction == Direction.LEFT:
            self.current_animation = self.left_animation
        else:
            self.current_animation = self.right_animation

        self.lives = Player.PLAYER_LIVES

    def draw(self):
        self.current_animation.draw()

    def update(self, delta_time):      
        self.current_animation.center_x += self.current_animation.change_x
        self.current_animation.center_y += self.current_animation.change_y

        self.current_animation.on_update(delta_time)

    def change_direction(self, new_direction):
        old_direction = self.direction
        if old_direction == new_direction:
            return
        self.direction = new_direction
        if self.direction == Direction.LEFT:
            self.left_animation.center_x = self.current_animation.center_x
            self.left_animation.center_y = self.current_animation.center_y
            self.current_animation = self.left_animation
        else:
            self.right_animation.center_x = self.current_animation.center_x
            self.right_animation.center_y = self.current_animation.center_y            
            self.current_animation = self.right_animation      
        

    