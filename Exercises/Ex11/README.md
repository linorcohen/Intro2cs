# Ex11 - A program of illness diagnose with binary search tree.
A simple program of illness diagnosed with binary search tree.   
This code is for building and utilizing a decision tree for medical diagnosis based on symptoms.  

Node class: Represents a node in the decision tree. Non-leaf nodes contain a question, and leaf nodes contain a decision (diagnosis). Each node can have positive (yes) and negative (no) children.
Record class: Represents a medical record, consisting of an illness and its associated symptoms.  

parse_data function: Reads a file containing illnesses and their symptoms, creating a list of Record objects.  

Diagnoser class: Manages a decision tree for diagnosing illnesses based on symptoms.  
Key methods include:
- diagnose: Determines the illness for a given list of symptoms using the decision tree.
- calculate_success_rate: Computes the success rate of the diagnoser based on a list of records (illness and symptoms).
- all_illnesses: Returns a list of all illnesses in the decision tree.
- paths_to_illness: Finds all paths within the tree that lead to a specified illness.
- minimize: Simplifies the decision tree by removing redundant nodes.
- build_tree function: Constructs a decision tree for diagnosing illnesses based on a given list of symptoms and records. It returns a Diagnoser object for the constructed tree.
- optimal_tree function: Determines the most accurate decision tree with the highest success rate, given a specific depth (number of symptoms to consider) and a list of symptoms and records.  

The tree is built and utilized as follows:
Each non-leaf node in the tree represents a symptom.
The path taken through the tree (positive or negative child nodes) depends on whether the patient has the symptom represented by the current node.
Leaf nodes represent the most likely illness diagnosis based on the path of symptoms.
The tree can be optimized or minimized to improve efficiency or accuracy.  

Overall, this program is a sophisticated tool for medical diagnosis, leveraging decision trees to match symptom patterns with likely illnesses.

## Example
![image](https://github.com/linorcohen/Intro2cs/assets/76969581/2f27c068-6a13-455e-924d-775ec4d44d2c)

