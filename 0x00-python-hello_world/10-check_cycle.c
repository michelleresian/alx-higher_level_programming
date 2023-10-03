#include "lists.h"
/**
 * check_cycle - checks if a linked list has a recurring cyc
le
 * list: a pointer to the linked list in question
 * Return: 1 if a cycle is foun and 0 if a failure is not fo
und
 */
int check_cycle(listint_t *list)
{
    listint_t *current;
    listint_t *power;

    current = list;
    power = list;

    while (current != NULL && power != NULL && power->next)
    {
        current = current->next;
        power = power->next->next;

        if (current == power)
            return (1);
    }
    return (0);
}