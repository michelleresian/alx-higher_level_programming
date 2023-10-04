#include "lists.h"

/**
 * insert_node - inserts a new node into a linked list
 * @head: pointer to the head of the linked list
 * @number: value to be inserted in the linked list
 * Return: Address of the new node else NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new_node = NULL;
	    listint_t *current = *head;
	    listint_t *prev = NULL;

	    new_node = malloc(sizeof(listint_t));

	    if (new_node == NULL)
		    return (NULL);

	    new_node->n = number;
	    new_node->next = NULL;

	    if (*head == NULL)
	    {
		    *head = new_node;
		    return (new_node);
	    }

	    while (current != NULL && current->n <= number)
	    {
		    prev = current;
		    current = current->next;
	    }

	    if (prev == NULL)
	    {
		    new_node->next = *head;
		    *head = new_node;
	    }
	    else
	    {
		    new_node->next = current;
		    prev->next = new_node;
	    }
	    return (new_node);
}