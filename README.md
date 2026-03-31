# Nutri-Switch: My AI Ingredient Finder 
**By: Nikhil** **Reg No: 25BCE11299** **VIT Bhopal University**

### Why I made this (The "Humble" Idea)
For my BYOP project, I wanted to do something different from the usual campus maps or maze solvers that everyone else is doing. I decided to solve a real problem I face in the hostel: running out of specific ingredients while trying to make a quick snack or drink.

Nutri-Switch is a simple AI that helps you find a "chain" of substitutes. If you are out of Honey, it suggests Sugar. If you are out of Sugar, it might suggest Jaggery. It uses the search strategies we learned in class to find these logical connections.

---

### How the AI "Thinks"
I used two different search types to see how they compare in a real-world kitchen scenario:

* **BFS (Breadth-First Search):** I used this as the "Smart Search." It looks for the most direct replacement first (the shortest path). So if you need Milk, it won't take you through five different steps if there is a direct substitute available right away.
* **DFS (Depth-First Search):** I used this more for "Exploration." It dives deep into the substitution tree to see all the possible alternatives, even if the path is a bit longer or less common.

---

### What's in the Folder?
I split the code into three files to keep it organized and because it makes it much easier to debug:
1.  **data_map.py**: This is my "Knowledge Base." It is a dictionary showing which ingredients can replace others.
2.  **logic.py**: This is where the actual AI "brain" is located. It contains the BFS and DFS functions.
3.  **app.py**: This is the main file you actually run to use the program.

---

### How to Run It
1. Download all three files into one single folder on your PC.
2. Open your terminal or VS Code.
3. Run the command: `python app.py`
4. Simply type in what you are missing and what you are looking for when prompted.

---

### Final Thoughts
Building this helped me actually see the difference between a Queue (used in BFS) and a Stack (used in DFS). It is much more interesting to see these algorithms work on food ingredients than just on a random graph from a textbook.

---

