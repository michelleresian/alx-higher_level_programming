#include "lists.h"

/**
 *is_palindrome - Check value in the linked list if is palindrome.
 *@head: pointer to the head of the linked list.
 *
 *Return: 1 if palindrome else 0.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		listint_t *next;

		fast = fast->next->next;

		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast != NULL)
		slow = slow->next;
	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}