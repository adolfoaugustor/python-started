#ramdom
import random

def random_number():
    print(random.randint(1, 100))

random_number()

print("Random: ", random.random())
print("Random: ", random.uniform(4,10))
print("Random: ", random.randint(21, 55))

cores = ["red", "green", "blue", "yellow"]
print("Random: ", random.choice(cores))

cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cartas)
print("Cartas: ", cartas)

moeda = ["cara", "coroa"]
print("Moeda: ", random.choice(moeda))