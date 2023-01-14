import random, operator, time



def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,

    }
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print(f'What is {num_1} {operation} {num_2} ?')
    return answer


def timer(count):
    while count:
        min , secs = divmod(count , 60)
        timer_count = ('{:02d}:{:02d}'.format(min, secs))
        print(timer_count,end="\r")
        time.sleep(1)
        count -= 1
    return True

def user():
    result = random_problem()
    user_ans = float(input())
    return user_ans == result

def game2():
    print("How well do you know math?\U0001F914\n")
    score = 0
    for i in range(5):
        if user() == True:
            score += 1
            print("CORRECT!!!")
        else:
            print("INCORRECT!!!")
    print(f'Your score is {score}\nThank you for playing \U0001F64F')

