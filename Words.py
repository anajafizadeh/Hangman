"""A function that selects a word randomly."""

import random

def car_selector() -> str:
    """Returns a randomly selected word from the file."""
    s = open("/Users/amirali/PycharmProjects/Hangman/Cars.txt", 'r')
    m = s.readlines()
    l = []
    for i in range(0, len(m) - 1):
        x = m[i]
        z = len(x)
        a = x[:z - 1]
        l.append(a)
    l.append(m[i + 1])
    o = random.choice(l)
    return o


def country_selector():
    s = open("/Users/amirali/PycharmProjects/Hangman/Countries.txt", 'r')
    m = s.readlines()
    l = []
    for i in range(0, len(m) - 1):
        x = m[i]
        z = len(x)
        a = x[:z - 1]
        l.append(a)
    l.append(m[i + 1])
    o = random.choice(l)
    return o


def name_selector():
    s = open("/Users/amirali/PycharmProjects/Hangman/Names.txt", 'r')
    m = s.readlines()
    l = []
    for i in range(0, len(m) - 1):
        x = m[i]
        z = len(x)
        a = x[:z - 1]
        l.append(a)
    l.append(m[i + 1])
    o = random.choice(l)
    return o


def club_selector():
    s = open("/Users/amirali/PycharmProjects/Hangman/Clubs.txt", 'r')
    m = s.readlines()
    l = []
    for i in range(0, len(m) - 1):
        x = m[i]
        z = len(x)
        a = x[:z - 1]
        l.append(a)
    l.append(m[i + 1])
    o = random.choice(l)
    return o


def random_selector():
    s = open("/Users/amirali/PycharmProjects/Hangman/random.txt", 'r')
    m = s.readlines()
    l = []
    for i in range(0, len(m) - 1):
        x = m[i]
        z = len(x)
        a = x[:z - 1]
        l.append(a)
    l.append(m[i + 1])
    o = random.choice(l)
    return o
