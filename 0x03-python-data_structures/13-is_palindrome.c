#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
listint_t *copy(listint_t **head)
{
    listint_t *current, *copy = NULL;
    current =*head;

    while (current != NULL)
    {
        add_nodeint_end(&copy, current->n);
        current = current->next;
    }
    return (copy);
}

listint_t *revevrse(listint_t **head)
{
    listint_t *start, *current = NULL, *pos;
    start =*head;
    while (start != NULL)
    {
        pos = start;
        start = start->next;
        pos->next = current;
        current = pos;
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

        current = copy(head);
        current = revevrse(&current);
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
