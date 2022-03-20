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
