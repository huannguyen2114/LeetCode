/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if(head == nullptr || head-> next == nullptr) return nullptr;
        ListNode* fastPointer = head;
        ListNode *dummyHead = new ListNode(-1, head);
        ListNode* p = head;
        ListNode* prev = dummyHead;
        while(fastPointer != nullptr && fastPointer->next != nullptr){
            prev = p;
            p = p->next;
            fastPointer = fastPointer->next->next;
        }
        prev->next = prev->next->next;
        return head;
    }
};