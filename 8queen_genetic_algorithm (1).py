# 1-init popu  2-crossover 3-mutation 4-fitness
import numpy as np
import time


def init_popu(p):
    popu_list = np.random.randint(8, size=(p, 8+1))
    return popu_list


def crossover(p):
    half = 4
    for i in range(0, len(p), 2):
        rnd1 = np.random.randint(100)
        rnd2 = np.random.randint(100)
        first_child = np.concatenate((p[rnd1][0:half], p[rnd2][half:]))
        second_child = np.concatenate((p[rnd2][0:half], p[rnd1][half:]))
        p.append(first_child)
        p.append(second_child)        
    return p


def mutation(p):
    # mutation is just for children
    for i in range(len(p)//2, len(p)):
        for j in range(8):
            x = np.random.rand()
            if x < 0.01:
                x = np.random.randint(8)
                while x == j:
                    x = np.random.randint(8)
                p[i][j] = x
    return p


def fitness(p):
    # at last if fitness==0 then it is the answer.
    for i in range(len(p)):
        fitness = 0
        for j in range(8):
            for k in range(j+1, 8):
                if p[i][j] == p[i][k]:
                    fitness += 1
                if abs(j-k) == abs(p[i][j]-p[i][k]):
                    fitness += 1
        p[i][-1] = fitness
    p = sorted(p, key=lambda x: x[-1])
    p = p[0:100]
    return p


def main():
    EPOCH = 500
    population = 500
    popu = init_popu(population)
    popu = fitness(popu)
    if popu[0][-1] == 0:
        print('I found answer:\n', popu[0])
        return

    while EPOCH:
        popu = crossover(popu)
        popu = mutation(popu)
        popu = fitness(popu)
        if popu[0][-1] == 0:
            print('I found answer:\n', popu[0])
            return
        EPOCH -= 1
    print('Sorry. I could not find an answer')


main()
