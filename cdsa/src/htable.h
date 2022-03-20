#ifndef __HTABLE_H
#define __HTABLE_H

enum {BUCKET_COUNT = 1024};


typedef struct HNode {
    const char *key;
    int value;
    struct HNode *next;
} HNode;

typedef struct HTable{
    HNode *array[BUCKET_COUNT];
} HTable;


//
HTable* htable_create(void);
void htable_add(HTable *table, const char *key, int value);
int htable_search(HTable *table, const char *key, int *value);
void htable_free(HTable *table);


#endif
