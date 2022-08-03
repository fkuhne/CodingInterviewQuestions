#include "Stack.h"

using namespace std;

void stack::push(int value)
{ 
	lifo = insertAtTheBeggining(lifo, value); 
}

int stack::pop()
{
	if (isEmpty()) return -1;
	int value = lifo->value; 
	lifo = deleteNodeAtTheBeggining(lifo); 
	return value; 
}

bool stack::isEmpty() 
{ 
	return lifo == nullptr; 
}

bool isOperand(char c)
{
	return (c >= '0' && c <= '9');
}

bool isOperator(char c)
{
	return (c == '*' || c == '/' || c == '+' || c == '-');
}

int evalExp(char operation, int operand1, int operand2)
{
	switch (operation) {
		case '*': return operand1 * operand2;
		case '/': return operand1 / operand2;
		case '+': return operand1 + operand2;
		case '-': return operand1 - operand2;
	}
	return 0;
}

int evaluatePostfix(vector<char> exp)
{
	if (exp.empty()) return 0;

	stack s;

	for (char c : exp) {
		if (isOperand(c)) s.push(c - 48);
		else if (isOperator(c)) {
			int op2 = s.pop();
			int op1 = s.pop();
			s.push(evalExp(c, op1, op2));
		}
	}
	
	return s.pop();
}
