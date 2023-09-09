#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: The linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start, *end;

	start = *head;
	end = *head;

	while (end->next != NULL)
		end++;

	while (start <= end)
	{
		if (start->n != end->n)
			return (0);
		start++;
		end--;
	}

	return (1);
}
