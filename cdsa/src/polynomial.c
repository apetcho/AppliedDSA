#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<curses.h>
#include<math.h>
#include<assert.h>
#include<errno.h>

#define MYNORMAL    "\x1b[m"
#define MYRED       "\x1b[31m"
#define MYGREEN     "\x1b[32m"
#define MYBLUE      "\x1b[34m"
#define MYWHITE     "\x1b[37m"

#define MYPROMPT    printf("%s ", "poly>>")


// -------------------------------------------------------------------------
// Write a program to store a polynomial using linked list. Also, perform
// addition and substraction on two polynomials.
// -------------------------------------------------------------------------

typedef struct Node Node;
struct Node{
    int num;
    int coef;
    Node *next;
};

Node *start1 = NULL;
Node *start2 = NULL;
Node *start3 = NULL;
Node *start4 = NULL;
Node *last3 = NULL;

void menu();
Node *create_polynomial(Node *);
Node *display_polynomial(Node *);
Node *add_polynomial(Node *, Node*, Node*);
Node *sub_polynomial(Node *, Node*, Node*);
Node *add_node(Node *, int, int);



// ----------------------------
//     M A I N   D R I V E R
// ----------------------------
int main(int argc, char **argv){
    int option;
    clear();
    do{
        menu();
        puts("\nEnter your option:");
        MYPROMPT;
        scanf("%d", &option);
        switch(option){
        case 1:
            start1 = create_polynomial(start1);
            break;
        case 2:
            start1 = display_polynomial(start1);
            break;
        case 3:
            start2 = create_polynomial(start2);
            break;
        case 4:
            start2 = create_polynomial(start2);
            break;
        case 5:
            start3 = add_polynomial(start1, start2, start3);
            break;
        case 6:
            start3 = display_polynomial(start3);
            break;
        case 7:
            start4 = sub_polynomial(start1, start2, start4);
            break;
        case 8:
            start4 = display_polynomial(start4);
            break;
        }
    }while(option != 9);
    (void)getch();

    return EXIT_SUCCESS;
}

// -----
void menu(){
    char buf[60];
    memset(buf, '*', 80);
    buf[79] = '\0';
    printf("%s%s%s\n", MYWHITE, buf, MYNORMAL);
    printf("%s% 80s%s\n", MYGREEN, "  M A I N   M E N U  ", MYNORMAL);
    printf("%s%s%s\n", MYWHITE, buf, MYNORMAL);
    puts("1. Enter the first polynomial");
    puts("2. Display the first polynomial");
    puts("3. Enter the second polynomial");
    puts("4. Display the second polynomial");
    puts("5. Add the polynomials");
    puts("6. Display the result");
    puts("7. Substract the polynomials");
    puts("8. Display the result");
    puts("9. EXIT");
}

// ---
Node *create_polynomial(Node *start){
    Node *newnode;
    Node *ptr;
    int num, coef;
    puts("Enter the number:");
    MYPROMPT;
    scanf("%d", &num);
    puts("Enter its coefficient:");
    MYPROMPT;
    scanf("%d", &coef);
    while(num != -1){
        if(start == NULL){
            newnode = (Node*)malloc(sizeof(Node));
            assert(newnode != NULL);
            newnode->num = num;
            newnode->coef = coef;
            newnode->next = NULL;
            start = newnode;
        }else{
            ptr = start;
            while(ptr->next != NULL){ ptr = ptr->next; }
            newnode = (Node*)malloc(sizeof(Node));
            assert(newnode != NULL);
            newnode->num = num;
            newnode->coef = coef;
            newnode->next = NULL;
            ptr->next = newnode;
        }
        puts("Enter the number:");
        scanf("%d", &num);
        if(num == -1){ break; }
        printf("Enter its coefficient:");
        MYPROMPT;
        scanf("%d", &coef);
    }

    return start;
}


Node *display_polynomial(Node *x){}
Node *add_polynomial(Node *x, Node *y, Node *z){}
Node *sub_polynomial(Node *x, Node *y, Node *z){}
Node *add_node(Node *x, int a, int b){}
