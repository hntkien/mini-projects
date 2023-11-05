"""
Example inputs & outputs for binary search algorithm. 

The test cases are organized into a list of dictionaries `tests` with the structure as follows:

tests = [{
    'input': {
        'nums': [list of numbers in an ascending order],
        'target': target number
    }
    'output': [first occurence, last occurence]
},
.
.
.
]

Some possible variations we might encounter: 
    - Target only appears once -> Return the same value for the first and the last occurence 
    - Target does not exist -> Return -1 for both the first and last occurences 
    - Empty list -> Return -1 for both the first and last occurence 
    - Multiple occurences -> Return the first and last occurences as normal

"""
test_cases = [] 

# Single occurence (at the beginning, middle, and end of the list)
test_cases.append({
    'input': {
        'nums': [0, 1, 3, 4, 7, 10, 11, 13],
        'target': 7
    },
    'output': [4, 4]
})
test_cases.append({
    'input': {
        'nums': [0, 1, 3, 4, 7, 10, 11, 13],
        'target': 0
    },
    'output': [0, 0]
})
test_cases.append({
    'input': {
        'nums': [0, 1, 3, 4, 7, 10, 11, 13],
        'target': 13
    },
    'output': [7, 7]
})

# No occurence 
test_cases.append({
    'input': {
        'nums': [-9, 2, 5, 7, 9],
        'target': 4
    },
    'output': [-1, -1]
})

# Empty list 
test_cases.append({
    'input': {
        'nums': [],
        'target': 7
    },
    'output': [-1, -1]
})

# Multiple occurences 
test_cases.append({
    'input': {
        'nums': [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 8, 8],
        'target': 8
    },
    'output': [12, 13]
})
test_cases.append({
    'input': {
        'nums': [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 8, 8],
        'target': 6
    },
    'output': [7, 11]
})
test_cases.append({
    'input': {
        'nums': [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 8, 8],
        'target': 0
    },
    'output': [0, 2]
})
