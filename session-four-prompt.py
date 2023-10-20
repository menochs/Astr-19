# Declares a class describing my favorite animal
class BlackCat:

    # length of arms (float)
    # length of legs (float)
    # number of eyes (int)
    # tail (bool)
    # furry (bool)
    def __init__(self, arm, leg, eyes, tail, furry):
        self.arm_length = arm
        self.leg_length = leg
        self.num_eyes = eyes
        self.tail = tail
        self.furry = furry

    def describe(self):
        print("Black Cat Qualities")
        print(f"Arm: {self.arm_length} inches")
        print(f"Leg: {self.leg_length} inches")
        print(f"Eyes: {self.num_eyes}")

        if self.tail:
            print("Has Tail: Yes")
        else:
            print("Has Tail: No")

        if self.furry:
            print("Is Furry: Yes")
        else:
            print("Is Furry: No")

# My Cat Mr. Maximus:
my_cat = BlackCat(6.1, 6.3, 2, True, True)
my_cat.describe() 