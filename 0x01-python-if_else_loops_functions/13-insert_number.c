#include "lists.h"
/**
 * insert_node - inserts a new node into a linked list
 * @head: pointer to the head of the linked list
 * @number: value to be inserted in the linked list
 * Return: pointer to the newly inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
