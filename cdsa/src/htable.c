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

// --
void htable_add(HTable *table, const char *key, int value){
    HNode *node = (HNode*)malloc(sizeof(HNode));
    if(check_hnode(node) == -1){
        perror("htable_add(): allocation failed.");
        exit(EXIT_FAILURE);
    }
    node->key = (const char*)malloc(strlen(key)+1);
    if(node->key == NULL){
        perror("htable_add(): allocation failed.");
        exit(EXIT_FAILURE);
    }
    strcpy(node->key, key);
    node->value = value;
    int h = hash(key);
    node->next = table->array[h];
    table->array[h] = node;
}

//
int htable_search(HTable *table, const char *key, int *value){
    HNode *node;
    int h = hash(key);
    for(node=table->array[h]; node != NULL; node = node->next){
        if(strcmp(node->key, key) == 0){
            *value = node->value;
            return 1;
        }
    }

    return 0;
}

// --
void htable_free(HTable *table){
    HNode *node;
    HNode *next;
    int b;
    for(b=0; b < BUCKET_COUNT; b++){
        for(node=table->array[b]; node != NULL; node = next){
            next = node->next;
            if(node->key){ free(node->key); }
            free(node);
        }
    }
    free(table);
}
