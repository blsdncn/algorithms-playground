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
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // Create a dummy node to simplify edge cases
    struct ListNode dummy;
    struct ListNode *tail = &dummy;
    dummy.next = NULL;

    // Traverse both lists and attach the smaller node to the tail
    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    // If either list is not empty, attach it to the end of the merged list
    if (list1 != NULL) {
        tail->next = list1;
    } else {
        tail->next = list2;
    }

    // Return the merged list, which starts from dummy.next
    return dummy.next;
}