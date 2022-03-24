"""
Simple jeu fait avec arcade.
Le jeu consiste a ce que notre poisson mange des poissons plus petits que lui pour grossir.
L'utilisateur doit aussi éviter les poissons plus gros afin de ne pas perdre de vie.
"""
import arcade

from player import Player

from fish_animation import FishAnimation

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 764
SCREEN_TITLE = "It's a fish eat fish world!"


class MyGame(arcade.Window):
    """
    La classe principale de l'application

    NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
    Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLUE_YONDER)

        self.back_ground = None

        # Player related attributes.
        self.player = None
        self.player_move_up = False
        self.player_move_down = False
        self.player_move_left = False
        self.player_move_right = True

        #self.left = FishAnimation("assets/2dfish/spritesheets/__cartoon_fish_06_yellow_idle.png")
        #self.right = FishAnimation("assets/2dfish/spritesheets/__cartoon_fish_06_yellow_idle.png", flip=True)

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous charger les sons de votre jeu.
        self.player = Player("assets/2dfish/spritesheets/__cartoon_fish_06_yellow_idle.png")

        self.back_ground = arcade.Sprite("assets/background.png")
        self.back_ground.center_x = SCREEN_WIDTH / 2
        self.back_ground.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
        # plan selon la couleur spécifié avec la méthode "set_background_color".
        arcade.start_render()
        self.back_ground.draw()

        self.player.current_animation.center_x = 200
        self.player.current_animation.center_y = 200
        self.player.draw()

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        self.player.update(delta_time)

    def update_player_speed(self):
        self.player.current_animation.change_x = 0
        self.player.current_animation.change_y = 0

        if self.player_move_left and not self.player_move_right:
            self.player.current_animation.change_x = -Player.MOVEMENT_SPEED
        elif self.player_move_right and not self.player_move_left:
            self.player.current_animation.change_x = Player.MOVEMENT_SPEED

        if self.player_move_up and not self.player_move_down:
            self.player.current_animation.change_y = Player.MOVEMENT_SPEED
        elif self.player_move_down and not self.player_move_up:
            self.player.current_animation.change_y = -Player.MOVEMENT_SPEED


    def on_key_press(self, key, key_modifiers):
        """
        Cette méthode est invoquée à chaque fois que l'usager tape une touche
        sur le clavier.
        Paramètres:
            - key: la touche enfoncée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

        Pour connaître la liste des touches possibles:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.A:
            self.player_move_left = True
            self.update_player_speed()
        elif key == arcade.key.D:
            self.player_move_right = True
            self.update_player_speed()
        elif key == arcade.key.W:
            self.player_move_up = True
            self.update_player_speed()
        elif key == arcade.key.S:
            self.player_move_down = True
            self.update_player_speed()

    def on_key_release(self, key, key_modifiers):
        """
        Méthode invoquée à chaque fois que l'usager enlève son doigt d'une touche.
        Paramètres:
            - key: la touche relâchée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        if key == arcade.key.A:
            self.player_move_left = False
            self.update_player_speed()
        elif key == arcade.key.D:
            self.player_move_right = False
            self.update_player_speed()
        elif key == arcade.key.W:
            self.player_move_up = False
            self.update_player_speed()
        elif key == arcade.key.S:
            self.player_move_down = False
            self.update_player_speed()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Méthode invoquée lorsque le curseur de la souris se déplace dans la fenêtre.
        Paramètres:
            - x, y: les coordonnées de l'emplacement actuel de la sourir
            - delta_X, delta_y: le changement (x et y) depuis la dernière fois que la méthode a été invoqué.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager clique un bouton de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été cliqué
            - button: le bouton de la souris appuyé
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager relâche le bouton cliqué de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été relâché
            - button: le bouton de la souris relâché
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
