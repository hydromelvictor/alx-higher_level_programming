#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *nil = NULL;
listint_t *reverse_copy(listint_t **head, listint_t *nil)
{
    listint_t *old, *pos = nil, *new;
    old = *head;
/*
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    
    new->n = old->n;*/
    new = old;
    new->next = pos;
    pos = new;
    if (old->next != NULL)
    {
        return (reverse_copy(&old->next, new));
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
        current = reverse_copy(head, NULL);
        while (start != NULL)
        {
            if (start->n != current->n)
                return (0);
            
            start = start->next;
            current = current->next;
        }
        return (1);
    }
}
