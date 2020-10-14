#ifndef __LINKED_LIST__
#define __LINKED_LIST__

#include <stdlib.h>

typedef struct 
{
  int val;
  ListNode *next;
  ListNode *prev;
} ListNode;

typedef struct 
{
  /* data */
  ListNode *head;
  ListNode *tail;
  int size;
} LinkedList;

LinkedList linkedList_create() {
  LinkedList list;
  ListNode *head = (ListNode *) malloc(sizeof(ListNode));
  ListNode *tail = (ListNode *) malloc(sizeof(ListNode));
  head -> next = tail;
  tail -> prev = head;
  list.head = head;
  list.tail = tail;

}

#endif