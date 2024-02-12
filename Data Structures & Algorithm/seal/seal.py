# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
#​‌​‌‌​​​‌​‌​​​‌ A class to describe a seal object
#​‌​‌‌​​​‌​‌​​​‌ Implement the missing functions here below

class Seal:

    def __init__(self, name):
        self.name = name
        self.energy = 3
        self.friends = []
        self.location = "water"

    def get_name(self):
        return self.name

    def eat(self):
        self.location = "water"
        self.energy = 5
        return "{} ate a fish!".format(self.name)

    def climb_on_rock(self):
        self.location = "rock"
        return "{}: Such a nice rock! :3".format(self.name)

    def do_banana_pose(self):
        if self.location == "water":
            return "{} is not on a rock.".format(self.name)
        elif self.energy > 1:
            self.energy -= 1
            return "{}: -__;3".format(self.name)
        elif self.energy == 1:
            return "{}: I won't. ___:3".format(self.name)

    def add_friend(self, x):
        if x not in self.friends:
            self.friends.append(x)
            x.add_friend(self)

    def tell_friends(self):
        f_num = len(self.friends)
        if f_num == 0:
            return ""
        elif f_num == 1:
            return "{}".format(self.friends[0].get_name())
        sentence = "{}".format(self.friends[0].get_name())
        for i in range(1, f_num):
            sentence += ", {}".format(self.friends[i].get_name())
        return sentence

    def request_banana_pose(self):
        response = []
        if len(self.friends) == 0:
            return response
        for x in self.friends:
            response.append(x.do_banana_pose())
        return response

    def __repr__(self):
        #​‌​‌‌​​​‌​‌​​​‌ Returns the representation of the object as a string:
        #​‌​‌‌​​​‌​‌​​​‌ the name of the seal and the unique identifier of this particular
        #​‌​‌‌​​​‌​‌​​​‌ Seal object. Reference for id():
        #​‌​‌‌​​​‌​‌​​​‌ https://docs.python.org/3/library/functions.html#id

        #​‌​‌‌​​​‌​‌​​​‌ You don't need to modify this method. It is used implicitly in the
        #​‌​‌‌​​​‌​‌​​​‌ unit tests to identify Seal objects that have been created in the
        #​‌​‌‌​​​‌​‌​​​‌ case some unit test does not pass.
        return "<Seal {}, id {}>".format(self.name, id(self))

if __name__ == "__main__":
    pass
    #​‌​‌‌​​​‌​‌​​​‌ You can experiment with the Seal class here

