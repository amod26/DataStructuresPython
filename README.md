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
   - Stack simply means aranging objects one over another. The same way memory is allocated in this data structure.<br>
   - In Stack elements inserted last in sequence will come out first as we can remove only from the top of the stack. <br>
   - LIFO (Last In First Out). <br>
   - The operations of adding and removing the elements is known as PUSH and POP. 
   - We declare an empty list and use the below methods to add and remove the data elements.
        * Operations performed: <br>
            - append()<br>
            - pop() <br>
## 4. Queue <br>
   - As we wait in Queue in stores, similarly, in this data structure the data is aligned in Queue.<br>
   - The uniquenes of queue lies the way data is inserted and removed. Items are allowed from one end but removed only from the other end.<br>
   - Similar to Stack but the order of operation is only FIFO(First In First Out),which means that element inserted first will also be removed first. <br>
   - An queue can be implemented using python list where we can use the below operations.
        * Operations performed: <br>
            - insert()<br>
            - pop() <br>
   - There is no insertion as data elements are always added at the end of the queue.
 # Abstract/Non-Linear Data Structures <br>
 ## 1. Tree <br>
   - A tree is an abstract data structure used to organize the data in a tree format so as to make the data insertion or deletion or search faster. <br>
 ## 2. Binary Tree <br>
   - One node is marked as Root node.<br>
   - Every node other than the root is associated with one parent node.<br>
   - Each node can have an arbitrary number of child node.<br>
   - It is a Data Structure where each data element can be connected to maximum two other data elements and it starts with a root node. <br>
 ## 3. Heap <br>
   - It is a special case of Tree data structure where the data in the parent node is either strictly greater than/ equal to the child nodes or strictly less than it’s child nodes. <br>
 ## 4. Hash Table <br>
   - It is a data structure which is made of arrays associated with each other using a hash function. It retrieves values using keys rather than index from a data element. <br>
 ## 5. Graph <br>
   - It is a collection of nodes called vertices, and the connections between them called edges. <br>
   - It is an arrangement of vertices and nodes where some of the nodes are connected to each other through links.<br>
   - Graphs can be used to model many types of relations and processes in physical, biological, social und information systems, and many practical problems can be represented by graphs.<br>
 ## 6. Priority Queue <br>
   - It is designed for systems that maintains a collection of prioritized elements, where elements are removed from the collection in order of their priority. <br>
   - Priority queues turn up in various applications, for example, processing jobs, where we process each job based on how urgent it is. <br>
   - For example, operating systems often use priority queue for the ready queue of processes to run on the CPU.<br>
