#include "lists.h"
listint_t *reverse(listint_t **head)
{
    listint_t *start, *current, *pos;
    start = *head;
    current = NULL;
    while (start != NULL)
    {
        pos = start;
        start = start->next;
        pos->next = current;
        current = pos;
    }
    return (current);
}

int is_palindrome(listint_t **head)
{
    listint_t *left, *rigth, *current;
    if (*head == NULL)
    {
        return (1);
    }
    else
    {
        left = *head;
        rigth = reverse(head);
        while (left->next != NULL)
        {
            if (left->n != rigth->n)
                return 0;
            left = left->next;
            rigth = rigth->next;
        }
        return (1);
    }
}
