from cellular_automaton import *
import random

ALIVE = '#'
DEAD = '.'

data = None

class Nilu(Rule):
    def __init__(self, data):
        self.data = data

    def init_state(self, cell_coordinate):
        init = self.data[cell_coordinate[0]][cell_coordinate[1]]
        return [init]


    def evolve_cell(self, last_cell_state, neighbors_last_states):
        new_cell_state = last_cell_state
        alive_neighbours = self.__count_alive_neighbours(neighbors_last_states)
        if last_cell_state == DEAD and alive_neighbours == 3:
            new_cell_state = ALIVE
        if last_cell_state == ALIVE and alive_neighbours < 2:
            new_cell_state = DEAD
        if last_cell_state == ALIVE and 1 < alive_neighbours < 4:
            new_cell_state = ALIVE
        if last_cell_state == ALIVE and alive_neighbours > 3:
            new_cell_state = DEAD
        return new_cell_state

    @staticmethod
    def __count_alive_neighbours(neighbours):
        an = []
        for n in neighbours:
            if n == ALIVE:
                an.append(1)
        return len(an)

    def get_state_draw_color(self, current_state):
        return [255 if current_state[0] else 0, 0, 0]



if __name__=="__main__":
    #data = [ [y for y in x.strip()[:]] for x in open("d24.in").readlines()]
    neighborhood = MooreNeighborhood(EdgeRule.IGNORE_MISSING_NEIGHBORS_OF_EDGE_CELLS)

    ca = CAFactory.make_single_process_cellular_automaton(dimension=[100, 100],neighborhood=neighborhood,rule=ConwaysRule)
    ca_window = CAWindow(cellular_automaton=ca, evolution_steps_per_draw=1)