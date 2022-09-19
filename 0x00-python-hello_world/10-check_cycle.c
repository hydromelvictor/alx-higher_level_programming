#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
    listint_t *current, *head;

    if (list == NULL)
    {
        return 0;
    }
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
