from enum import Enum

from fish_animation import FishAnimation


class Direction(Enum):
    LEFT = 0
    RIGHT = 1

class Player:
    MOVEMENT_SPEED = 2.0
    
    def __init__(self, spritesheet_path):
        #super().__init__(spritesheet_path)
        self.left_animation = FishAnimation(spritesheet_path)
        self.right_animation = FishAnimation(spritesheet_path, flip=True)
        self.current_animation = None

        self.face_left = True
        if self.face_left:
            self.current_animation = self.left_animation
        else:
            self.current_animation = self.right_animation

    def draw(self):
        self.current_animation.draw()

    def update(self, delta_time):
        self.current_animation.on_update(delta_time)

    def change_direction(self):
        self.face_left = not self.face_left
        if self.face_left:
            self.current_animation = self.left_animation
        else:
            self.current_animation = self.right_animation        
        

    