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

typedef struct ListNode{
    const char *key;
    int value;
    struct ListNode *next;
} ListNode;

typedef struct Table {
    struct ListNode *first;
}ListTable ;

/** Create a new Table */

ListTable* table_create(void);
void table_add(ListTable *table, const char *key, int value);
int table_search(ListTable *table, const char *key, int *value);
void table_free(ListTable *table);
#endif
