#include "../lists.h"
#include <stdio.h>
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

int main()
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);
    head = reverse(&head);
    printf("\n\n");
    print_listint(head);
    return 0;
}