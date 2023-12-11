import gzip
import pickle

list = [int(input("Enter element: ")) for _ in range(10)]

with open("txt.pickle", "wb") as file:
    pickle.dump(list, file)

with open("txt.pickle", "rb") as file:
    new_list = pickle.load(file)

print(new_list)
