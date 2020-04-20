# DataStructuresPython
- Solving Data Structure problems all revolve around finding the solution in the least amount of time using the least computing resources. <br>
- Calculating time can be denoted in complexity classes based on which operations you use. <br>
- You'll find problems in this repo from Leetcode.

## Linear Data Structures
## 1. Arrays
- Suppose you had a bunch of DVDs at home that you wanted to arrange neatly. What would be the ideal choice for storing such a thing? <br>
- You could find a cardboard box (or some other box) big enough to arrange all of the DVDs neatly, right? It's as simple as that. <br>
- However, you might want to add a new DVD to the box, or you might want to get rid of the old ones that you've watched a million times over in the past. <br>


> The two most primitive Array operations are writing elements into them, and reading elements from them. All other Array operations are built on top of these two primitive operations. <br>


* We usually use _for loop_ to write and read data from the Array. <br>
*  Operations:
    - Traverse − print all the array elements one by one.
    - Insertion − Adds an element at the given index.
    - Deletion − Deletes an element at the given index
    - Search − Searches an element using the given index or by the value.
    - Update − Updates an element at the given index.
## 2. Linked List
#### - Singly LinkedList <br>
   - Singly linkedlist have a data node and a pointer to the next node. <br>
      * Main Linked Lists Operations <br>
           - Insert: inserts an clement into the list <br>
           - Delete: removes and returns the specified position element from the list <br>
      * Auxiliary Linked Lists Operations <br>
           - Delete List: removes all elements of the list (dispose of the lisl) <br>
           - Count: returns the number of elements in the list <br>
           - Find nth node from the end of the list <br>
#### - Doubly LinkedList <br>
   - The doubly linked list works in a similar way but has one more reference field which is known as the "prev" field. With this extra field, you are able to know the previous node of the current node. <br>
   - If we want to delete an existing node cur from the doubly linked list, we can simply link its previous node prev with its next node next.<br>
   - Unlike the singly linked list, it is easy to get the previous node in constant time with the "prev" field.

   - Since we no longer need to traverse the linked list to get the previous node, both the time and space complexity are O(1).
        * Operations performed: <br>
             - Add Operation <br>
             - Remove Operation <br>
      
## 3. Stack <br>
   - Stack follows only a specific flow of operation. Either FIFO(First in First Out) or LIFO (Last In First Out).  <br>
## 4. Queue <br>
   - Similar to Stack but the order of operation is only FIFO(First In First Out) <br>
   
 # Non-Linear Data Structures <br>
 ## 1. Binary Tree <br>
   - It is a Data Structure where each data element can be connected to maximum two other data elements and it starts with a root node. <br>
 ## 2. Heap <br>
   - It is a special case of Tree data structure where the data in the parent node is either strictly greater than/ equal to the child nodes or strictly less than it’s child nodes. <br>
 ## 3. Hash Table <br>
   - It is a data structure which is made of arrays associated with each other using a hash function. It retrieves values using keys rather than index from a data element. <br>
 ## 4. Graph <br>
   - It is an arrangement of vertices and nodes where some of the nodes are connected to each other through links.
