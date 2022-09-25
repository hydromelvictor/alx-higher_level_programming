#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
listint_t *reverse_copy(listint_t **head)
{
    listint_t *old, *pos, *new;
    old = *head;
    pos = NULL;
    while (old != NULL)
    {
        new = malloc(sizeof(listint_t));
        if (new == NULL)
            return (NULL);

        new->n = old->n;
        new->next = pos;
        pos = new;
        old = old->next;
    }
    return (pos);
}

int is_palindrome(listint_t **head)
{
    listint_t *start, *current;
    if (*head == NULL)
        return (1);
    else
    {
        start = *head;
        if (start->next == NULL)
            return (0);

        current = reverse_copy(head);
        while (start->next != NULL)
        {
            if (start->n != current->n)
                return (0);
            
            start = start->next;
            current = current->next;
        }
        return (1);
    }
}
