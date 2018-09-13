def find_prime():
    """
        Write a program that finds all the prime numbers from 2 to 100 using nested loops.
        (Hint: use counters; define prime numbers)
        prime number: any number that cannot be divided besides 1 and itself
    """
    for prime_num in range(2, 101):
        num_of_factor = 0
        # A prime number only has 2 factors, 1 and itself.
        # If the number of factor is 2, then it mean the number is a factor
        for factors in range(1, prime_num + 1):
            # This gives the program all the possible factors to test for
            if prime_num % factors == 0:
                num_of_factor += 1
                # This counts and records how many full number factors the given number has
        if num_of_factor == 2:
            print(prime_num, " is a prime number.")
            # This tests for if the number has 2 factors
            # Aka. check for number of factors to determine if it is a prime number
        else:
            pass
            # This skips the loop and goes onto the next possible number if the number has more than two factors
