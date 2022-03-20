#include<stdlib.h>
#include<stdio.h>
#include<string.h>

#include "llist.h"

//
static int check_table(ListTable *table){
    if(table == NULL){
        return -1;
    }
    return 0;
}

//
ListTable* table_create(void){
    ListTable *table;
    table = (ListTable *)malloc(sizeof(*table));
    if(table == NULL){
        perror("table_create(): allocation error\n");
        return NULL;
    }
    table->first = NULL;
    return table;
}

//
void table_add(ListTable *table, const char *key, int value){
    if(check_table(table) == -1){
        fprintf(stderr, "Table is not yet allocated\n");
        exit(EXIT_FAILURE);
    }

    // Allocate a new node
    struct ListNode *node = (struct ListNode*)malloc(sizeof(struct ListNode));
    if(node == NULL){
        perror("table_add(): not enough memory slot\n");
        exit(EXIT_FAILURE);
    }
    // the node needs to own the value of key
    node->key = malloc(strlen(key)+1);
    if(node->key == NULL){
        perror("table_add(): not enough memory slot\n");
        exit(EXIT_FAILURE);
    }
    strcpy(node->key, key);
    node->value = value;
    node->next = table->first;
    table->first = node;
}


/**
 * @brief Search a given key in a table and retun its value
 * 
 * @param table Table to search
 * @param key search key
 * @param value value returned if key found
 * @return int 0 if key not found otherwise retunr 1
 */
int table_search(ListTable *table, const char *key, int *value){
    struct ListNode *node;

    if(check_table(table) == -1){
        fprintf(stderr, "Table is empty or non-existant");
        exit(EXIT_FAILURE);
    }

    for(node=table->first; node != NULL; node=node->next){
        if(strcmp(node->key, key) == 0){
            *value = node->value;
            return 1;
        }
    }
    return 0;
}
