#include "lists.h"

listint_t* reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - reverses a singly-linked listint_t list.
 * @head: points to the starting node of the list to reverse.
 *
 * Return: points to the head of the reversed list.
 */
listint_t* reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: points to the head of the linked list.
 *
 * Return: 0 if !palindrome otherwise 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, n;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (n = 0; n < (size / 2) - 1; n++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}

	reverse_listint(&mid);

	return (1);
}
