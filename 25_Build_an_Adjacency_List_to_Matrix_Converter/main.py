def adjacency_list_to_matrix(adj_list):
    # Get the number of nodes by counting the number of keys
    n = len(adj_list.keys())
    # The final adjacency matrix using list comprehension
    adj_matrix = [[1 if neighbour in adj_list[node_no] else 0 for neighbour in range(n)] for node_no in range(n)]
    # Print the rows of the adjacency matrix and then return it
    print(adj_matrix)
    return adj_matrix

# Test code
#adj_list = {
#    0: [1, 2],
#    1: [2],
#    2: [0, 3],
#    3: [2]
#}
#adjacency_list_to_matrix(adj_list) 
