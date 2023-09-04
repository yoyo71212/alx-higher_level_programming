#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 *
 * @list: The singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	turtle = list;
	hare = list;

	while (hare && hare -> next)
	{
		turtle = turtle -> next;
		hare = hare -> next -> next;
		if (turtle == hare)
		{
			return(1);
		}
	}

	return (0);
}
