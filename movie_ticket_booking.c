#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure for each customer node
struct Node {
    char name[50];
    struct Node* next;
};

// Front and Rear pointers
struct Node *front = NULL, *rear = NULL;

// Function to add a booking (Enqueue)
void bookTicket(char name[]) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    if (!newNode) {
        printf("❌ Memory allocation failed!\n");
        return;
    }
    strcpy(newNode->name, name);
    newNode->next = NULL;

    if (rear == NULL) { // if queue is empty
        front = rear = newNode;
    } else {
        rear->next = newNode;
        rear = newNode;
    }
    printf("🎫 Ticket booked for %s\n", name);
}

// Function to serve a customer (Dequeue)
void serveCustomer() {
    if (front == NULL) {
        printf("⚠ No customers in queue!\n");
        return;
    }
    struct Node* temp = front;
    printf("✅ %s has received the ticket.\n", front->name);
    front = front->next;
    if (front == NULL)
        rear = NULL; // queue became empty
    free(temp);
}

// Function to display all customers in queue
void displayQueue() {
    if (front == NULL) {
        printf("📭 No pending customers.\n");
        return;
    }
    struct Node* temp = front;
    int i = 1;
    printf("\n🎟 Current Booking Queue:\n");
    while (temp != NULL) {
        printf("%d. %s\n", i++, temp->name);
        temp = temp->next;
    }
}

int main() {
    int choice;
    char name[50];

    printf("=== Movie Ticket Booking System (Linked List) ===\n");
    while (1) {
        printf("\n1. Book Ticket\n2. Serve Customer\n3. Display Queue\n4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter customer name: ");
                scanf("%s", name);  // For multi-word names, replace with fgets
                bookTicket(name);
                break;
            case 2:
                serveCustomer();
                break;
            case 3:
                displayQueue();
                break;
            case 4:
                printf("Exiting... Thank you!\n");
                // Free any remaining nodes before exiting
                while (front != NULL) {
                    serveCustomer();
                }
                exit(0);
            default:
                printf("❌ Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
