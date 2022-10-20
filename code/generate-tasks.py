import random
import string
from dag.graph import Graph
from dag.vertex import Vertex
from library import earnings
from library import numbers
from library import dependencys
import PySimpleGUI as sg


def setup_graph():
    g = Graph()
    g.add_vertex("start", "")

    for key_comb, value_comb in dependencys.COMBINATIONS.items():
        print(g.add_vertex(key_comb, value_comb))
        g.add_edge("start", key_comb)

        for key_earn, value_earn in earnings.ALL.items():
            print(g.add_vertex(key_earn, value_earn))
            g.add_edge(key_comb, key_earn)

            for key_num, value_num in numbers.ALL.items():
                print(g.add_vertex(key_num, value_num))
                g.add_edge(key_earn, key_num)

    print("\n")
    
    sg.theme('LightBlue')
    layout = [
            [sg.Graph(canvas_size=(700,700), graph_bottom_left=(0, 0), graph_top_right=(700, 700), key='graph')]
            ]
    window = sg.Window('Created Graph', layout, finalize=True)
    graph = window['graph']
    pos_x = 40
    pos_y = 660
    
    for vert in g:
        print(vert)
        graph.DrawCircle((pos_x, pos_y), 25)
        pos_x += 35
        pos_y -= 35
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break 
    return window


if __name__ == '__main__':
    char = random.choice(string.ascii_letters).upper()
    w = setup_graph()
    w.close()
