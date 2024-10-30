import math
from queue import PriorityQueue
import copy
import numpy as np





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~READING INPUTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Read the total number of nodes, start, end, and edge information from the inputfil
def read_inputfile():

    #open input file for reading and place all lines in a list
    with open('input.txt', 'r') as file:
        txt = file.readlines()

    # 
    total_nodes = int(txt[0].strip())
    start = int(txt[1].strip())
    goal = int(txt[2].strip())

    edges_matrix = np.full((total_nodes,total_nodes),float('inf'))
    for line in txt[3:]:
        split = [float(component) for component in line.split()]
        edges_matrix[int(split[0])-1][int(split[1])-1] = float(split[2])


    return [edges_matrix, total_nodes, start, goal]



#~~~~~~~~~~~~~~~DYNAMIC PROGRAMMING~~~~~~~~~~~~~~~~
# Find the shortest path using Dynamic Programming
def cost_to_come():
    value_table = np.full((total_nodes),float('inf'))
    value_table[start-1] = 0
    best_neighbour = np.full(total_nodes,None)

    for step in range(2,total_nodes+1):                         # Dynamic step number
        for node_id in range(1,total_nodes+1):                  # Node we are calculating value of in the step
            temp_value = []
            temp_neighbour = []
            
            for neighbour_node_id in range(1,total_nodes):
                cost = edges_matrix[node_id-1][neighbour_node_id-1]
                if cost != float('inf'):                        # Nodes related to that node
                    start_value = value_table[neighbour_node_id-1] 
                    temp_value.append(cost + start_value)       # Bellman
                    temp_neighbour.append(neighbour_node_id)    # Keep track of nearst neighbour id in parallel array

            index = np.argmin(temp_value)                       # get min id
            selected_min_value = temp_value[index]              # get min value
            current_value = value_table[node_id-1]              # get id of min value

            if selected_min_value < float('inf') and selected_min_value < current_value: # if less than inf and less than current value
                value_table[node_id-1] = selected_min_value     # Assign min value
                best_neighbour[node_id-1] = temp_neighbour[index] # assign best neighrbour
            else:
                value_table[node_id-1] = current_value

    print(value_table)
    return value_table, best_neighbour



#~~~~~~~~~MAIN~~~~~~~~~~~~~

#readinputs
nodes_list = []
[edges_matrix, total_nodes, start, goal] = read_inputfile()


# If you wish to test other start/end points on the graph, enter those values here
goal = goal
start = start

value_table, best_neighbour = cost_to_come()

backtrack_id = goal
shortestpath_ids = []

while backtrack_id != start:
    shortestpath_ids.insert(0, backtrack_id)
    backtrack_id = best_neighbour[backtrack_id-1]

shortestpath_ids.insert(0, backtrack_id)


#Print Output File
with open('012155624.txt', 'w') as file:
    for id in shortestpath_ids:
        file.write(str(id) + ' ')
    file.write('\n')
    for values in value_table:
        file.write(str(round(values,2)) + ' ')
    file.write('\n')