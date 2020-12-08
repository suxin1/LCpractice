#include <stdlib.h>
#include <stdio.h>

typedef struct _Node Node;

typedef struct _Node {
  int value;
  Node * left;
  Node * right;
} Node;

typedef struct {
  Node root;
  Node *memo;
} Tree;


/**
 * 输入一个二维数组，返回一个二叉树的根节点。
 * 二维数组型如： {{1, 2, 4}, {2, 5, 6}, {4, 0, 0}, {5, 0, 0}, {6, 0, 0}} 0表示无子节点。
 * */
Tree bt_from_array(int a[][3], int size) {
  Node root;

  Node *memo = (Node *) malloc(size * sizeof(Node));

  for(int i=0;i<size;i++) {
    memo[i].value = a[i][0];
  }

  for(int i=0;i<size;i++) {
    int leftValue = a[i][1];
    int rightValue = a[i][2];
    
    int done = 0;
    for(int j=0;j<size;j++) {

      if(a[j][0] == leftValue && leftValue != 0) {
        memo[i].left = &memo[j];
        done ++;
      }

      if(a[j][0] == rightValue && rightValue != 0) {
        memo[i].right = &memo[j];
        done ++;
      }

      if(done == 2) break;
    }

  }

  Tree tree;
  tree.memo = memo;
  tree.root = memo[0];
  return tree;
}

/**
 * 释放树占用内存。
 * */
void destroy_tree(Tree tree) {
  free(tree.memo);
}


int main() {
  int a[7][3] = { {5, 4, 6}, {4, 1, 2}, {6, 7, 8}, {1, 0, 0}, {2, 0, 0}, {7, 0, 0}, {8, 0, 0} };
  Tree n = bt_from_array(a, 7);
  printf("node.value %d, node.right.value %d\n", n.root.value, n.root.right->value);
  destroy_tree(n);
}