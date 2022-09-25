#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
listint_t *reverse_copy(listint_t **head, int n)
{
    listint_t *new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;
    return (new);
}


listint_t *copy(listint_t **head)
{
    listint_t *current, *copy = NULL;
    current =*head;

    while (current != NULL)
    {
        reverse_copy(&copy, current->n);
        current = current->next;
    }
    return (copy);
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
