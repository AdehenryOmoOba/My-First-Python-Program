import random
import copy


class Hat:
    def __init__(self, **kwargs):
        print(kwargs)
        self.contents = []
        for ball in kwargs:
            for item in range(kwargs[ball]):
                self.contents.append(ball)
        print(self.contents)

    def draw(self, number):
        all_removed = []
        if (number > len(self.contents)):
            return self.contents
        for i in range(number):
            removed = self.contents.pop(
                int(random.random() * len(self.contents)))
            all_removed.append(removed)
        return all_removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors = hat_copy.draw(num_balls_drawn)

        for color in colors:
            if (color in expected_copy):
                expected_copy[color] -= 1

        if (all(item <= 0 for item in expected_copy.values())):
            count += 1
    return count / num_experiments


new_hat = Hat(yellow=2, blue=1, green=3)
