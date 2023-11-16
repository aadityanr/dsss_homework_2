import random


#Generates a random integer between the given numbers
def random_generator(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

#Generates a random operator from the given choice
def generate_random_operator():
    return random.choice(['+', '-', '*'])


#Perform a simple arithmetic operation
#example: operation(5,6,'+')
def arithmetic_operation(num_1, num_2, operator):
    expression = f"{num_1} {operator} {num_2}"
    try:
        if operator == '+':
            solution = num_1 + num_2
        elif operator == '-':
            solution = num_1 - num_2
        elif operator == '*':
            solution = num_1 * num_2
        else:
            raise ValueError("Invalid operator. Please use '+', '-', or '*'.")
        return expression, solution
    except (TypeError, ValueError) as e:
        print(f'Error: {e}')
        print('Wrong input! Please try again.')


# Math Quiz connected with previous functions
def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")

    for _ in range(total_questions):
            num_1 = random_generator(1, 10)
            num_2 = random_generator(1, 5)
            operator = generate_random_operator()
            expression, correct_answer = operation(num_1, num_2, operator)

            print(f"\nQuestion: {expression}")
            try:
                user_answer = int(input("Your answer: "))
            except ValueError:
                print("Invalid answer")
                next

            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
