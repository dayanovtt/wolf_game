import random
import time
from enum import Enum
from functools import partial


class Location(Enum):
    left_up = 'Слева сверху'
    left_down = 'Слева внизу'
    right_up = 'Справа сверху'
    right_down = 'Справа внизу'


class Wolf:
    def __init__(self):
        self.location = Location.left_up

    def move(self, new_location: Location):
        print(f'Wolf moved to {new_location}')
        self.location = new_location


class Egg:
    def __init__(self, location: Location):
        self.location = location
        self.position = 0

    def move(self):
        self.position += 1
        print(f'Egg {self.location} moved to {self.position}')


class Game:
    EGG_PATH_LENGTH = 5

    def __init__(self):
        self.score = 0
        self.sound = True
        self.speed = 2
        self.is_active = False
        self.health = 3
        self.wolf = Wolf()
        self.eggs = [Egg(x) for x in Location]

    def toggle_sound(self):
        self.sound = not self.sound

    def end_game(self):
        self.is_active = False
        print(f'Game Over. Your score {self.score}!')

    def check_wolf_position(self, egg: Egg):
        if egg.location == self.wolf.location:
            self.score += 1
        else:
            self.health -= 1
            if self.health == 0:
                self.end_game()

    def move_random_egg(self):
        egg = random.choice(self.eggs)
        egg.move()
        if egg.position > self.EGG_PATH_LENGTH:
            self.check_wolf_position(egg)
            egg.position = 0

    def play(self):
        self.is_active = True
        while self.is_active:
            print(f'Current score {self.score}')
            self.move_random_egg()
            time.sleep(2 / self.speed)


class Button:
    def __init__(self, name: str, action: callable):
        self.name = name
        self.action = action

    def press(self):
        print(f'Button {self.name} pressed')
        self.action()


class GameController:
    def __init__(self):
        self.game = Game()
        self.buttons = [
            Button('Game', self.game.play),
            Button('Sound', self.game.toggle_sound),

            Button('И', partial(self.game.wolf.move, Location.left_up)),
            Button('Ы', partial(self.game.wolf.move, Location.left_down)),
            Button('З', partial(self.game.wolf.move, Location.right_up)),
            Button('Д', partial(self.game.wolf.move, Location.right_down))

        ]


if __name__ == '__main__':
    gc = GameController()
    gc.buttons[0].press()
