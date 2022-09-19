#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
    listint_t *current, *head;
    current = list;
    head = current;
    current = current->next;
    while (current != NULL)
    {
        if (current == head)
        {
            return (1);
        }
        current = current->next;
    }
    return (0);
}
