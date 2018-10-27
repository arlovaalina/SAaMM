from random import *

from tkinter import *
from variables import *
from stateMatrix import *

def getNewState(graph, currState, probability):
    prevTransition = 0
    for i in range(STATE_AMOUNT):
        transition = prevTransition + graph[currState][i]
        if probability < transition:
            return i
        else:
            prevTransition = transition
    

def start_algorithm(p, pi1, pi2, tactsAmount):
    graph = getStateMatrix(p, pi1, pi2)
    print(graph)
    
    currState = 0
    for tact in range(tactsAmount):
        print(currState)
        probability = random()
        currState = getNewState(graph, currState, probability)
        print(probability)

    # aperiodic_interval_label = Label(root, text = "Длина отрезка апериодичности: " + str(round(aperiodic_interval, 3)), height = 1, width = 50, anchor = 'w').place(x = 200, y = 500)
    # indirect_indications_label = Label(root, text = "2К / N: " + str(round(indirect_indications, 3)) + "; pi / 4: " + str(round(math.pi / 4, 3)), height = 1, width = 50, anchor = 'w').place(x = 200, y = 520)
    

def initialize_window():
    root = Tk()
    root.geometry("{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT))

    p_label = Label(root, text = "Вероятность не выдачи заявки, ρ").place(x = 10, y = 10)
    p_input = Entry(root, width = 27)
    p_input.place(x = 10, y = 30)
    
    pi1_label = Label(root, text = "Вероятность просеивания, π1").place(x = 10, y = 60)
    pi1_input = Entry(root, width = 27)
    pi1_input.place(x = 10, y = 80)
    
    pi2_label = Label(root, text = "Вероятность просеивания, π2").place(x = 10, y = 110)
    pi2_input = Entry(root, width = 27)
    pi2_input.place(x = 10, y = 130)
    
    tacts_label = Label(root, text = "Количество тактов").place(x = 10, y = 160)
    tacts_input = Entry(root, width = 27)
    tacts_input.place(x = 10, y = 180)
    
    start_button = Button(root, text = "Моделировать", width = 15,
        command = lambda: start_algorithm(float(p_input.get()), float(pi1_input.get()), float(pi2_input.get()), int(tacts_input.get())))
    start_button.place(x = 10, y = 210)

    root.mainloop()


def main():
    initialize_window();

if __name__ == "__main__":
    main()
