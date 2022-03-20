#include<stdlib.h>
#include<stdio.h>
#include<string.h>

#include "llist.h"

typedef enum DTYPE{
    LINKED_LIST = 1,
    HASH_TABLE
}DTYPE;

void print_table(void *table, DTYPE type);
void testListTable();

//
static void print_listnode(ListNode node){
    char buf[48];
    sprintf(buf, "(%24s, %7d)\n", node.key, node.value);
    puts(buf);
    return;
}

// -----------------------------------------------
//              M A I N     D R I V E R
// -----------------------------------------------
int main(int argc, char **argv){

    testListTable();
    return EXIT_SUCCESS;
}

//
void print_table(void *table, DTYPE type){
    if(type == LINKED_LIST){
        ListTable* _table = (ListTable*)table;
        ListNode *node=_table->first;
        for(; node != NULL; node = node->next){
            print_listnode(*node);
        }
        return;
    }else if(type == HASH_TABLE){
        return;
    }
}

//
void testListTable(){
    // Create a table
    ListTable *table = table_create();
    // Add elements
    table_add(table, "Ruth", 3);
    table_add(table, "Gehrig", 4);
    table_add(table, "Mantle", 7);
    // Search element 
    const char *key = "Gehrig";
    int value;
    int found;
    found = table_search(table, key, &value);
    if(found){
        printf("Key=%s found in table with value=%d\n", key, value);
    }
    // Print table
    puts("Table contents:");
    print_table(table, LINKED_LIST);
    // Release allocate memory
    table_free(table);

    return;
}
