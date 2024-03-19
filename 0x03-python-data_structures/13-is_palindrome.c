#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *h = *head;
	int i = 0;
	int arr[11] = [];
	
	printf("before");
	while (h != NULL && (h->next != NULL))
	{
		i++;
		h = h->next;
	}
	i++;
	printf("here");
	printf("%d\n",i);
	printf("out");
	while (current)
	{
		arr[i] = current->n;
		i--;
		current = current->next;
	}

	return 1;

}
