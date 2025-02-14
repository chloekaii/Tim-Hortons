# Tim-Hortons
Implementing a greedy algorithm to find the solution to the Tim-Hortons problem.

## Algorithm Design:
- Read K (highway length), L (maximum distance from Tim Hortons), n (number of off-ramps), and H (sorted list of off-ramp locations) from input.txt.
- selected _positions: A list where the Tim Hortons locations selected for covering the range will be stored.
- current_position: Set to 0, representing the initial position.
- i: set to 0, used to traverse H.
- While current_position is less than K (the target coverage):
  - Inner loop: It checks each location in H and increments i as long as the location H[i] is less than current_position + L.
  -  Once the inner loop completes, current_position is updated to the last valid location H[i - 1]
  -  The location H[i - 1] is added to selected_locations.
- After selecting all the necessary locations to cover the range, the algorithm writes selected_locations to a file.
## Data Structures/Variables Used:
- H (List of Integers): A list containing the positions of the available locations. It is indexed sequentially to find the valid locations within the coverage range.
- selected_locations (List of Integers): A list used to store the locations that are selected.
- current_position (Integer): A variable that keeps track of the current position. It is updated during each iteration to the position of the last selected location.
- i (Integer): An index used to iterate over H.
## Time Complexity Analysis:
- Outer while loop (while current_position < K): This loop iterates until current_position reaches or exceeds K. The number of iterations depends on the number of selected locations, m (the number of steps taken to cover the distance).
- Inner while loop (while i < n and H[i] <= current_position + L): For every iteration of the outer loop, this inner loop checks which locations are within the current step's range (current_position + L).

The outer loop runs m times, where m is the number of locations selected to cover the distance K. In the worst case, all n locations could be selected, but m can be smaller than n.
The inner loop increments i across all elements in Hn. Each element in H is checked once, making this loop's time complexity O(n).
Total Time Complexity:
The outer loop contributes O(m). The inner loop contributes O(n). Since m is less than or equal to n, the total time complexity of the program is O(n).
