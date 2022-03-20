#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include "htable.h"

//
static unsigned int hash(const char *x){
    unsigned int h = 0U;
    for(int i=0; x[i] != '\0'; i++){
        h = h * 65599 + (unsigned char)x[i];
    }
    return h & 1023;
}

static int check_htable(HTable *table){
    if(table == NULL){
        return -1;
    }
    return 0;
}

static int check_hnode(HNode *node){
    if(node == NULL){ return -1; }
    return 0;
}

//
HTable* htable_create(void){
    HTable *table;

    table = (HTable*)calloc(1, sizeof(*table));
    if(check_htable(table) == -1){
        perror("htable_create(): allocation failed.");
        return  NULL;
    }

    return table;
}
