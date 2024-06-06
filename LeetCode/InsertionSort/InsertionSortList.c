#include <stdlib.h>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

  
struct ListNode {
    int val;
    struct ListNode *next;
};
 
struct ListNode* insertionSortList(struct ListNode* head) {
    // Dummy node to act as the new head of the sorted list
    struct ListNode dummy;
    dummy.next = NULL;

    // Iterate through each node in the original list
    struct ListNode* current = head;
    while (current != NULL) {
        // Keep the next node
        struct ListNode* nextNode = current->next;

        // Find the correct position to insert the current node in the sorted part
        struct ListNode* prev = &dummy;
        while (prev->next != NULL && prev->next->val < current->val) {
            prev = prev->next;
        }

        // Insert the current node into the sorted part
        current->next = prev->next;
        prev->next = current;

        // Move to the next node
        current = nextNode;
    }

    return dummy.next;
}

