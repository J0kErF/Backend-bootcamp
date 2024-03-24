from collections import Counter
import time

def fibonacci(n):
    ##O(2^n) time complexity
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memoized(n, memo={}):
    ##O(n) time complexity
    if n not in memo:
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

def linear_search(lst, target):
    ##O(n) time complexity
    for i, num in enumerate(lst):
        if num == target:
            return i
    return -1

def dict_search(lst, target):
    ##O(n) time complexity
    dct = dict(Counter(lst))
    return dct.get(target, -1)


def count_words_naive(text, word):
  ##O(n) time complexity
  count = 0
  for w in text.split():
    if w == word:
      count += 1
  return count


def count_words_hash(text, word):
    ##O(n) time complexity
    dct={}
    for w in text.split():
        if w in dct:
            dct[w]+=1
        else:
            dct[w]=1
    return dct[word]

def calculate_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

input_sizes = [10]
fibonacci_data = []
linear_search_data = []
dict_search_data = []
count_words_naive_data = []
count_words_hash_data = []

for size in input_sizes:
    #1st
    fibonacci_time = calculate_time(fibonacci, size)
    fibonacci_memoized_time = calculate_time(fibonacci_memoized, size)
    fibonacci_data.append([f"Fibonacci (Naive)", size, fibonacci_time])
    fibonacci_data.append([f"Fibonacci (Memoized)", size, fibonacci_memoized_time])
    #2nd
    test_list = list(range(size))
    target = size // 2 
    linear_search_time = calculate_time(linear_search, test_list, target)
    dict_search_time = calculate_time(dict_search, test_list, target)
    linear_search_data.append([f"Linear Search", size, linear_search_time])
    dict_search_data.append([f"Dictionary Search", size, dict_search_time])
    #3rd
    sample_text = "Back End Boot Camp Course is designed very well & the course is very helpful"
    word = "Course"
    count_words_naive_time = calculate_time(count_words_naive, sample_text, word)
    count_words_hash_time = calculate_time(count_words_hash, sample_text, word)
    count_words_naive_data.append([f"Count Words (Naive)", size, count_words_naive_time])
    count_words_hash_data.append([f"Count Words (Hash)", size, count_words_hash_time])

data=fibonacci_data+linear_search_data+dict_search_data+count_words_naive_data+count_words_hash_data

with open("data.txt", 'w') as f:
    f.write("Function, Input Size, Time (seconds)\n\n")
    for row in data:
      string_row = map(str, row)
      formatted_row = ', '.join(string_row)
      f.write(formatted_row + '\n')