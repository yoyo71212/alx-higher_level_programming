#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - Inserts a number into a sorted singly linked list
 *
 * @head: The sorted singly linked list
 * @number: The number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	current = *head;
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->n < number && current->next->n > number)
			{
				temp = current->next;
				current->next = new;
				new->next = temp;
				return (new);
			}
			current = current->next;
		}
		current->next = new;
	}

	return (new);
}
