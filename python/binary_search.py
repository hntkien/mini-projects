""" 
========== Binary Search Algorithm ========== 

Problem: Find first and Last Position of Element in Sorted Array. The array is sorted in ascending order. (From LeetCode)

Binary Search Implementation:
    1. Find the middle element of the list 
    2. If it matches the target, return the middle position as the answer 
    3. If it is less than the target, then search the first (left) half of the list 
    4. If it is greater than the target, then search the second (right) half of the list
    5. If no more elements remain, return -1 
"""

#===== Import the test cases =====# 
from binary_search_data import test_cases 

#===== Feature Functions =====#

### Binary Search Implementation
def binary_search(low, high, check_location):
    """
    Implementation of the Binary Search Algorith with a given location. Return the middle position if the target is found, otherwise, return -1. 

    Parameters:
        - low : The left-most index of the list 
        - high: The right-most index of the list 
        - check_location: A function to determine whether to search the left half, right half, or the target is found. Return values: ['left', 'right', 'found']
    """
    while low <= high:

        mid = (low + high) // 2
        location = check_location(mid) 

        if location == 'found':
            return mid 
        elif location == 'right':
            low = mid + 1 
        else:
            high = mid - 1
    
    return -1 

### Searching 
def search_range(nums, target):
    """
    Searching Process. Return the first and last positions of the target. 

    Parameters: 
        - nums  : The list of numbers in an ascending order 
        - target: The target number 
    """

    def first_occurence(mid):
        """
        A function indicating that we want to find the first occurence of the target. Return values: ['left', 'right', 'found']
        """
        if nums[mid] == target:
            # if the value at the middle position equals the target 
            if (mid > 0) and (nums[mid-1] == target):
                # if mid is not the first index, and if the target also appears before the middle position, search the left half of the list  
                return 'left' 
            else: 
                # the target is found
                return 'found' 
        elif nums[mid] < target:
            # search the right half of the list
            return 'right'
        else:
            return 'left' 
    
    def last_occurence(mid):
        """
        A function indicating that we want to find the last occurence of the target. Return values: ['left', 'right', 'found']
        """
        if nums[mid] == target:
            if (mid+1 < len(nums)) and (nums[mid+1] == target):
                # if mid is not the last index, and if the target also appears after the middle position, search the right half of the list
                return 'right'
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right' 
        else:
            return 'left' 
        
    first_position = binary_search(
        low=0, high=len(nums)-1, check_location=first_occurence)
    last_position = binary_search(
        low=0, high=len(nums)-1, check_location=last_occurence)
    return [first_position, last_position] 


#===== Main Function =====#
def main():
    # # Test cases from LeetCode:
    # print(search_range(nums= [5,7,7,8,8,8,10], target=8))
    # print(search_range(nums= [5,7,7,8,8,10], target=7))
    # print(search_range(nums= [5,7,7,8,8,10], target=6))
    # print(search_range(nums= [], target=8))

    # Validating all the customized test cases
    for test in test_cases:
        results = search_range(
            nums=sorted(test['input']['nums']),
            target=test['input']['target']
        )

        if (results[0]==test['output'][0]) and (results[1]==test['output'][1]):
            print(f"Expected: {test['output']}, Result: {results}. Test Passed.")
        else:
            print(f"Expected: {test['output']}, Result: {results}. Test Failed.")


#===== Execution =====#
if __name__ == '__main__':
    main() 