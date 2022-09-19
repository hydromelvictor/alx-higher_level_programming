#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int check_cycle(listint_t *list)
{
    listint_t *current = malloc(sizeof(listint_t));
    listint_t *head = malloc(sizeof(listint_t));
    current = list;
    head = current;
    current = current->next;
    while (current != NULL)
    {
        if (current == head)
        {
            free(current);
            free(head);
            return (1);
        }
        current = current->next;
    }
    free(current);
    free(head);
    return (0);
}
