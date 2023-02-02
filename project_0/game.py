import numpy as np

def random_predict(number:int=1) -> int:
    
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1,101) #guess number
        if predict_number == number:
            break
    
    return (count)

print(f'Quantity of guesses: {random_predict()}')
    
def score_game(random_predict) -> int:
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size =(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Your algorythm mean number is: {score}')
    
    return (score)


if __name__ == '__main__':
    score_game(random_predict)