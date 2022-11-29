#Analysis of trackers
from utils import *

def load_data(file):
    with open("jsons/trackers/"+file+".json", "r") as f:
        return json.load(f)

def main():

    myFile = "0"
    gameJSON = load_data(myFile)
    print(gameJSON)

if __name__ == "__main__":
    main()