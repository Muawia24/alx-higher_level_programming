#include "lists.h"

/**
 * insert_node - inserts a number into a
 * sorted singly linked list.
 * @head: pointer to head of list
 * @number: number to be stored in the list
 * Return:  the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *temp = *head;
	listint_t *new;
	unsigned int i = 0;

	for (i = 0; current->n < number; i++)
		current = current->next;
	while (i - 1 > 0)
	{
		temp = temp->next;
		i--;
	}
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = temp->next;
	temp->next = new;

	return (new);

}
