# DataStructuresPython
- Solving Data Structure problems all revolve around finding the solution in the least amount of time using the least computing resources. <br>
- Calculating time can be denoted in complexity classes based on which operations you use. <br>
- You'll find problems in this repo from Leetcode.

## 1. Arrays
- Suppose you had a bunch of DVDs at home that you wanted to arrange neatly. What would be the ideal choice for storing such a thing? <br>
- You could find a cardboard box (or some other box) big enough to arrange all of the DVDs neatly, right? It's as simple as that. <br>
- However, you might want to add a new DVD to the box, or you might want to get rid of the old ones that you've watched a million times over in the past. <br>


> The two most primitive Array operations are writing elements into them, and reading elements from them. All other Array operations are built on top of these two primitive operations. <br>


* We usually use _for loop_ to write and read data from the Array. <br>

## 2. Linked List
#### - Singly LinkedList <br>
   - Singly linkedlist have a data node and a pointer to the next node. <br>
        * Operations performed: <br>
 	        - find(data) <br>
            - get_size() <br>
            - add(data) <br>
            - remove(data) <br>
            
#### - Doubly LinkedList <br>
   - The doubly linked list works in a similar way but has one more reference field which is known as the "prev" field. With this extra field, you are able to know the previous node of the current node. <br>
   -If we want to delete an existing node cur from the doubly linked list, we can simply link its previous node prev with its next node next.<br>
   - Unlike the singly linked list, it is easy to get the previous node in constant time with the "prev" field.

   - Since we no longer need to traverse the linked list to get the previous node, both the time and space complexity are O(1).
        * Operations performed: <br>
             - Add Operation <br>
             - Remove Operation <br>
