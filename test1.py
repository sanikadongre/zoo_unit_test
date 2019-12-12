import sys
import unittest
import random


# https://raw.githubusercontent.com/sanikadongre/OOAD_F19_Homeworks_Projects/master/Project2/Q1a/zoo.py
from zoo import Animal
from zoo import Canine
from zoo import Feline
from zoo import Pachyderm
from zoo import Cat
from zoo import Elephant
from zoo import Hippo
from zoo import Lion
from zoo import Rhino
from zoo import Tiger
from zoo import Wolf
from zoo import Dog
from zoo import ZooKeeper

@classmethod
def getAnimal():
	animal = Animal("name")
	return animal

def test_animal_wakeUp(getAnimal, unittest.TestCase):
	ani = getAnimal.wakeUp()
	self.assertEqual(ani, "name The animal wakes up.\n")

def test_animal_sleep(getAnimal, unittest.TestCase):
	ani = getAnimal.sleep()
	 self.assertEqual(ani,"name The animal sleeps.\n")

def test_animal_eat(getAnimal, unittest.TestCase):
	ani = getAnimal.eat()
	self.assertEqual(ani,"name The animal eats.\n")

def test_animal_roam(getAnimal, unittest.TestCase):
	ani = getAnimal.roam()
	self.assertEqual("")
def test_animal_makeNoise(getAnimal, unittest.TestCase):
	ani = getAnimal.makeNoise()
	self.assertEqual("")

@classmethod
def getCanine():
	canine = Canine("name")
	return canine

def test_canine_eat(getCanine, unittest.TestCase):
	ani = getCanine.eat()
	self.assertEqual(ani,"name The Canine animal eats meat.\n")

def test_canine_roam(getCanine, unittest.TestCase):
	ani = getCanine.roam()
	self.assertEqual(ani,"name The Canine animal roams in pack.\n")

@classmethod
def getFeline():
	feline = Feline("name")
	return feline

def test_feline_eat(getFeline, unittest.TestCase):
	ani = getFeline.eat()
	self.asserEqual(ani,"name The Feline animal eats raw meat.\n")

def test_feline_roam(getFeline, unittest.TestCase):
	ani = getFeline.roam()
	 self.assertEqual(ani,"name The Feline animal roams individually/alone.\n")

@classmethod
def getPachyderm():
	pachyderm = Pachyderm("name")
	return pachyderm

def test_pachyderm_eat(getPachyderm, unittest.TestCase):
	ani = getPachyderm.eat()
	self.assertEqual(ani,"name The Pachyderm animal eats grass and/or some meat.\n")

def test_pachyderm_roam(getPachyderm, unittest.TestCase):
	ani = getPachyderm.roam()
	self.assertEqual(ani,"name The Pachyderm animal roams in herds or by itself.\n")

@classmethod
def getCat():
	cat = Cat("name")
	return cat

def test_cat_makeNoise(getCat, unittest.TestCase):
	ani = getCat.makeNoise()
	self.assertEqual(ani,"name Cat makes noise Meow.\n" or out == "name Cat makes noise Meowwww and Meowwww.\n")
def test_cat_roam(getCat, unittest.TestCase):
	ani = getCat.roam()
	self.assertEqual(ani,"name Cat exercises by stretching and licking itself.\n") or self.assertEqual(ani,"name Cat exercises by playing with itself and purring.\n")

@classmethod
def getElephant():
	elephant = Elephant("name")
	return elephant
def test_elephant_makeNoise(getElephant, unittest.TestCase):
	ani = getElephant.makeNoise()
	self.assertEqual(ani,"name Elephant makes noise Mooooo.\n")
def test_elephant_roam(getElephant, capsys):
	ani = getElephant.roam()
	self.assertEqual(ani,"name Elephant exercises by moving and bathing in the muddy water.\n")

@classmethod
def getHippo():
	hippo = Hippo("name")
	return hippo
def test_hippo_makeNoise(getHippo, unittest.TestCase):
	ani = getHippo.makeNoise()
	self.assertEqual(ani,"name Hippo makes noise Hipooo.\n")

def test_hippo_roam(getHippo, unittest.TestCase):
	ani = getHippo.roam()
	self.assertEqual(ani,"name Hippo exercises by jumping up and down in the water.\n")

@classmethod
def getLion():
	lion = Lion("name")
	return lion
def test_lion_makeNoise(getLion, unittest.TestCase):
	getLion.makeNoise()
	self.assertEqual(ani,"name Lion makes noise LionGrrr.\n")
def test_lion_roam(getLion, unittest.TestCase):
	ani = getLion.roam()
	self.assertEqual(ani,"name Lion exercises by running quick and putting claws in trees.\n")

@classmethod
def getRhino():
	rhino = Rhino("name")
	return rhino

def test_rhino_makeNoise(getRhino, unittest.TestCase):
	ani = getRhino.makeNoise()
	self.assertEqual(ani,"name Rhino makes noise Rhinooo.\n")
def test_rhino_roam(getRhino, unittest.TestCase):
	ani = getRhino.roam()
	self.assertEqual(ani,"name Rhino exercises by jumping up and down in the grass.\n")

@classmethod
def getTiger():
	tiger = Tiger("name")
	return tiger

def test_tiger_makeNoise(getTiger, unittest.TestCase):
	ani = getTiger.makeNoise()
	self.assertEqual(ani,"name Tiger makes noise Tigrrrrr.\n")
def test_tiger_roam(getTiger, capsys):
	getTiger.roam()
	self.assertEqual(ani,"name Tiger exercises by running quick and putting claws in trees.\n")
	

@classmethod
def getWolf():
	wolf = Wolf("name")
	return wolf

def test_wolf_makeNoise(getWolf, unittest.TestCase):
	ani = getWolf.makeNoise()
	self.assertEqual(ani,"name Wolf makes noise Grrrrr.\n")
def test_wolf_roam(getWolf, unittest.TestCase):
	getWolf.roam()
	self.assertEqual(ani,"name Wolf exercises by stretching and licking itself.\n")

@classmethod
def getDog():
	dog = Dog("name")
	return dog
def test_dog_makeNoise(getDog, unittest.TestCase):
	ani = getDog.makeNoise()
	self.assertEqual(ani,"name Dog makes noise Woof.\n")
def test_dog_roam(getDog, unittest.TestCase):
	ani = getDog.roam()
	self.assertEqual(ani,"name Dog exercises by stretching and sprinting.\n")


def test_zookeeper_init(capsys):
	ani = ZooKeeper()
	self.assertEqual(ani,"""----- Day At the Zoo: Output -----
Zoo Opened.)
