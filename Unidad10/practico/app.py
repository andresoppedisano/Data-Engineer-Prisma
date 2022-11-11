def test_sum(list_number):

    total_sum = sum(list_number)
    assert(total_sum) == 10

if  __name__ == "__main__":
    numbers = [3, 5, 1]
    test_sum(numbers)
    print('esta todo bien')