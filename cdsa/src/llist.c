#include<stdlib.h>
#include<stdio.h>

#include "llist.h"

//
ListTable* table_create(void){
    ListTable *table;
    table = (ListTable *)malloc(sizeof(*table));
    if(table == NULL){
        perror("table_create(): allocation error");
        return NULL;
    }
    table->first = NULL;
    return table;
}
