"""
[summary]
Simple module to declare our animation class for the different attack type.
https://gamedev.stackexchange.com/questions/44118/how-to-slow-down-a-sprite-that-updates-every-frame
Used this site to implement a slower animation.
"""
import arcade


class FishAnimation(arcade.Sprite):
    ANIMATION_SPEED = 15.0

    def __init__(self, spritesheet_path):
        super().__init__()

        textures = arcade.load_spritesheet(spritesheet_path, 498, 327, 3, 12)
        self.textures = textures

        self.scale = 0.5
        self.current_texture = 0
        self.set_texture(self.current_texture)

        # Animation speed related
        self.animation_update_time = 1.0 / FishAnimation.ANIMATION_SPEED
        self.time_since_last_swap = 0.0

    def on_update(self, delta_time: float = 1 / 60):
        # Update the animation.
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0
