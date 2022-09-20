#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current, *prev;
    current = *head;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
    {
        return (NULL);
    }
    new->n = number;

    if (*head == NULL)
    {
        new->next = NULL;
        *head = new;
        return (*head);
    }
    else
    {
        if (current->n > new->n)
        {
            new->next = current;
            *head = new;
            return (*head);
        }
        else
        {
            prev = current;
            current = current->next;
            while (current != NULL)
            {
                if (current->n >= new->n)
                {
                    prev->next = new;
                    new->next = current;
                    return (*head);
                }
                prev = current;
                current = current->next;
            }
            prev->next = new;
            new->next = NULL;
            return (*head);
        }
    }
    return (NULL);
}
