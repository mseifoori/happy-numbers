def is_happy(n: int) -> bool:
    """
    A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.
    :param n: The number to check if it is happy or not.
    :type n: int
    :return: True if the number is happy, False otherwise.
    :rtype: bool
    
    :example:
    
    >>> is_happy(21)
    False
    
    >>> is_happy(19)
    True
    """
    seen_numbers: set = set()
    while (n != 1) and (n not in seen_numbers):
        seen_numbers.add(n)
        n: int = sum([int(i) ** 2 for i in str(n)])
        
    return n == 1


if __name__ == '__main__':
    assert not is_happy(2), 'Test Case 1 Failed'
    assert is_happy(19), 'Test Case 2 Failed'
    assert not is_happy(21), 'Test Case 3 Failed'
    assert is_happy(44), 'Test Case 4 Failed'
    assert is_happy(139), 'Test Case 5 Failed'
    
    print('All test cases passed.')
