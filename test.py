import sys
from abc import ABC, abstractmethod
import random
import unittest
from mock import patch
from unittest.mock import MagicMock


class Animal():
    def _init_(self, name=" "):

        self.name = name

    def wakeUp(self):
        if self.name != " ":
            print(self.name," The animal wakes up.")

    def sleep(self):
        if self.name != " ":
            print(self.name + " The animal sleeps.")

    def eat(self):
        if self.name != " ":
            print(self.name + " The animal eats.")

    @abstractmethod
    def roam(self):
        pass
    @abstractmethod
    def makeNoise(self):
        pass


class Canine(Animal):


    def eat(self):
        print(self.name + " The Canine animal eats meat.")

    def roam(self):
        super().roam()
        print(self.name + " The Canine animal roams in pack.")


class Feline(Animal):


    def eat(self):
        print(self.name + " The Feline animal eats raw meat.")


    def roam(self):
        super().roam()
        print(self.name + " The Feline animal roams individually/alone.")


class Pachyderm(Animal):

    def eat(self):
        print(self.name + " The Pachyderm animal eats grass and/or some meat.")


    def roam(self):
        super().roam()
        print(self.name + " The Pachyderm animal roams in herds or by itself.")

class Cat(Feline):

    def _init_(self,name):
        self.name = name;

    def makeNoise(self):
        super().makeNoise()
      #use random number generation to select from alternative responses to animal actions
        if(random.randint(1,101) < 50):
            #Math.random() generates number between 0 & 1
            print(self.name + " Cat makes noise Meow.")
        else:
            print(self.name + " Cat makes noise Meowwww and Meowwww.")

    def roam(self):
        #use random number generation to select from alternative responses to animal actions
        if(random.randint(1,101) < 50):
      #Math.random() generates number between 0 & 1
            print(self.name + " Cat exercises by stretching and licking itself.")
        else:
            print(self.name + " Cat exercises by playing with itself and purring.")

class TestCat(unittest.TestCase):
    def test_makeNoise(self):
        cat = Cat("Cheshire")
        #self.assertTrue(mock_makeNoise.expr=)
        cat.makeNoise = MagicMock()
        cat.makeNoise.assert_called_with(1,2,3)
        #self.assertTrue(mock_makeNoise.call_args[0][0] == "Cheshire Cat makes noise Meow." or mock_makeNoise.call_args[0][0] == "Cheshire Cat makes noise Meowwww and Meowwww.")

    def test_roam(self):
        cat = Cat("Cheshire")
        cat.roam = MagicMock()
        cat.roam.assert_called_with(1,2,3)

class Elephant(Pachyderm):
    def _init_(self,name):
        self.name = name;

    def makeNoise(self):
        super().makeNoise()
        print(self.name + " Elephant makes noise Mooooo.")


    def roam(self):
        print(self.name + " Elephant exercises by moving and bathing in the muddy water.")

class TestElephant(unittest.TestCase):
    elephant = Elephant("Elle")



class Hippo(Pachyderm):

    def _init_(self,name):
        self.name = name

    def makeNoise(self):
        super().makeNoise()
        print(self.name + " Hippo makes noise Hipooo.")
    def roam(self):
        print(self.name + " Hippo exercises by jumping up and down in the water.")

class Lion(Feline):

    def _init_(self,name):
        self.name = name

    def makeNoise(self):
        super().makeNoise()
        print(self.name + " Lion makes noise LionGrrr.")

    def roam(self):
        print(self.name + " Lion exercises by running quick and putting claws in trees.")

class Rhino(Pachyderm):

    def _init_(self,name):
        self.name = name

    def makeNoise(self):
        super().makeNoise()
        print(self.name + "Rhino makes noise Rhinooo.")

    def roam(self):
        print(self.name + " Rhino exercises by jumping up and down in the grass.")


class Tiger(Feline):

    def _init_(self,name):
        self.name = name

    def makeNoise(self):
        super().makeNoise()
        print(self.name + "Tiger makes noise Tigrrrrr.")

    def roam(self):
        print(self.name + "Tiger exercises by running quick and putting claws in trees.")


class Wolf(Canine):

    def _init_(self,name):
        self.name = name

    def makeNoise(self):
        super().makeNoise()
        print(self.name + "Wolf makes noise Grrrrr.")

    def roam(self):
        print(self.name + "Wolf exercises by stretching and licking itself.")


class Dog(Canine):

    def _init_(self,name):
        self.name = name

    def makeNoise(self):
        super().makeNoise()
        print(self.name + "Dog makes noise Woof.")

    def roam(self):
        print(self.name + "Dog exercises by stretching and sprinting.")


class ZooKeeper:



    def _init_(self):
        sys.stdout = open('dayatthezoo.txt','wt')
        print("----- Day At the Zoo: Output -----")
        print("Zoo Opened.")
        print("")

        animals=[Animal()]
        animals.append(Cat("Cheshire"))
        animals.append(Cat("Cuddles"))
        animals.append(Lion("Leo"))
        animals.append(Lion("Lewis"))
        animals.append(Tiger("Tigran"))
        animals.append(Tiger("Tigru"))
        animals.append(Elephant("Ellen"))
        animals.append(Elephant("Elson"))
        animals.append(Dog("Deo"))
        animals.append(Dog("Dawn"))
        animals.append(Hippo("Hank"))
        animals.append(Hippo("Hustler"))
        animals.append(Rhino("Rincon"))
        animals.append(Rhino("Ruben"))
        animals.append(Tiger("Ruben"))
        animals.append(Wolf("Will"))
        animals.append(Wolf("Wiz"))
        self.performTasksSequentially(animals)
        print("")
        print("Zoo Closed")


    #def createZooAnimals(self):


    def performTasksSequentially(self,animals):
        print("----------- wakeUpAnimals --------------")
        self.performFunction("wakeUpAnimals",animals)
        print("----------- rollCallAnimals --------------")
        self.performFunction("rollCallAnimals",animals)
        print("----------- feedAnimals --------------")
        self.performFunction("feedAnimals",animals)
        print("------------ exerciseAnimals -------------")
        self.performFunction("exerciseAnimals",animals)
        print("------------ shutDownZoo -------------")
        self.performFunction("shutDownZoo",animals)

    def one(self,a):
        return  a.wakeUp()

    def two(self,a):
        return  a.makeNoise();

    def three(self,a):
        return a.eat();

    def four(self,a):
        return  a.roam();

    def five(self,a):
        return a.sleep();


    def performFunction(self,Task,animals):
        for a in animals:
            if Task == "wakeUpAnimals":
                self.one(a)
            elif Task == "rollCallAnimals":
                self.two(a)
            elif Task == "feedAnimals":
                self.three(a)
            elif Task == "exerciseAnimals":
                self.four(a)
            elif Task == "shutDownZoo":
                self.five(a)



if _name_ == '_main_':
    zk=ZooKeeper()
    unittest.main()
