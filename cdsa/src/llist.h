#ifndef __LLIST_H_
#define __LLIST_H_
/**
 * @brief Maintain a table of key/value pairs using singly linked list.
 * 
 * - Each key is a string
 * - Each value is an int
 * - Unknown number of key/value pairs
 * 
 * Examples
 * --------
 * - (student name, grade)
 * - (baseball player, number)
 * - (variable name, value)
 */

// Linked List
// ALGORITHM
// - Create
// - Add
// - Search
// - Free

struct ListNode{
    const char *key;
    int value;
    struct ListNode *next;
};

struct Table {
    struct ListNode *first;
};

#endif
