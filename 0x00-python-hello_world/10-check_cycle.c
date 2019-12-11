#include "lists.h"

/**
 *check_cycle - function to check if a linked list has a cycle
 *@list: list
 *Return: zero or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *i, *j;

	i = list;
	j = list;

	if (list == NULL)
		return (0);
	while (i != NULL && j != NULL && j->next != NULL)
	{
		i = i->next;
		j = j->next->next;
		if (i == j)
			return (1);
	}

	return (0);
}
