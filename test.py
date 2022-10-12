from utils import *

def main():

    with open("jsons/players.json", "r") as f:
        data = json.load(f)
    f.close()

    for i in data:
        i["streak"] = 0

    with open("jsons/players.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()