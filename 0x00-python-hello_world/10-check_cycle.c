#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
    listint_t *current;

    if (list == NULL)
    {
        return 0;
    }
    current = list;
    current = current->next;
    while (current != NULL)
    {
        if (current == list)
        {
            return (1);
        }
        current = current->next;
    }
    return (0);
}
