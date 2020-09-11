import pickle
import json


def saveWithPickle(fileName, obj):
    file = open(fileName, "w")
    pickle.dump(obj, file)
    file.close()


def saveWithJSON(fileName, obj):
    file = open(fileName, "w")
    json.dump(obj, file)
    file.close()


def loadWithPickle(fileName):
    file = open(fileName, "r")
    obj = pickle.load(file)
    file.close()
    return obj


def loadWithJSON(fileName):
    file = open(fileName, "r")
    obj = json.load(file)
    file.close()
    return obj
