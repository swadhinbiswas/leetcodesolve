#include <stdio.h>
#include <stdlib.h>

// Function to create a new node
int* createNode(int key) {
    int* newNode = (int*)malloc(3 * sizeof(int));
    newNode[0] = key;
    newNode[1] = 0;  // left child
    newNode[2] = 0;  // right child
    return newNode;
}

// Insertion
void insert(int** root, int key) {
    int* newNode = createNode(key);
    if (*root == NULL) {
        *root = newNode;
        return;
    }

    int* queue = (int*)malloc(100 * 3 * sizeof(int));
    int front = 0, rear = 0;
    queue[rear++] = (*root)[0];
    queue[rear++] = (*root)[1];
    queue[rear++] = (*root)[2];

    while (front < rear) {
        int temp = queue[front++];
        int left = queue[front++];
        int right = queue[front++];

        if (!left) {
            queue[rear++] = temp;
            queue[rear++] = (int)newNode;
            queue[rear++] = 0;
            break;
        } else {
            queue[rear++] = left;
            queue[rear++] = right;
        }

        if (!right) {
            queue[rear++] = temp;
            queue[rear++] = 0;
            queue[rear++] = (int)newNode;
            break;
        } else {
            queue[rear++] = left;
            queue[rear++] = right;
        }
    }

    free(queue);
}

// Deletion
int* deleteDeepest(int** root, int* delNode) {
    int* queue = (int*)malloc(100 * 3 * sizeof(int));
    int front = 0, rear = 0;
    queue[rear++] = (*root)[0];
    queue[rear++] = (*root)[1];
    queue[rear++] = (*root)[2];

    while (front < rear) {
        int temp = queue[front++];
        int left = queue[front++];
        int right = queue[front++];

        if (left == (int)delNode) {
            left = 0;
            free(delNode);
            return *root;
        } else if (right == (int)delNode) {
            right = 0;
            free(delNode);
            return *root;
        } else {
            queue[rear++] = left;
            queue[rear++] = right;
        }
    }

    free(queue);
    return *root;
}

int* delete(int** root, int key) {
    if (*root == NULL)
        return NULL;

    if ((*root)[1] == 0 && (*root)[2] == 0) {
        if ((*root)[0] == key) {
            free(*root);
            *root = NULL;
            return NULL;
        } else {
            return *root;
        }
    }

    int* keyNode = NULL;
    int* queue = (int*)malloc(100 * 3 * sizeof(int));
    int front = 0, rear = 0;
    queue[rear++] = (*root)[0];
    queue[rear++] = (*root)[1];
    queue[rear++] = (*root)[2];
    int* temp;
    while (front < rear) {
        int node = queue[front++];
        int left = queue[front++];
        int right = queue[front++];

        if (node == key)
            keyNode = (int*)node;

        if (left)
            queue[rear++] = left;
        if (right)
            queue[rear++] = right;
    }

    if (keyNode != NULL) {
        int x = temp[0];
        *root = deleteDeepest(root, (int*)temp);
        *keyNode = x;
    }

    free(queue);
    return *root;
}

void printLevelOrder(int* root) {
    if (root == NULL)
        return;

    int* queue = (int*)malloc(100 * 3 * sizeof(int));
    int front = 0, rear = 0;
    queue[rear++] = root[0];
    queue[rear++] = root[1];
    queue[rear++] = root[2];

    while (front < rear) {
        int temp = queue[front++];
        int left = queue[front++];
        int right = queue[front++];
        printf("%d ", temp);

        if (left)
            queue[rear++] = left;
        if (right)
            queue[rear++] = right;
    }

    free(queue);
}

int main() {
    int* root = NULL;
    insert(&root, 1);
    insert(&root, 2);
    insert(&root, 3);
    insert(&root, 4);
    insert(&root, 5);

    printf("Level order traversal before deletion: ");
    printLevelOrder(root);

    // Delete a node
    root = delete(&root, 3);

    printf("\nLevel order traversal after deletion: ");
    printLevelOrder(root);

    return 0;
}