import time

def test_concatenation():
    print("Exercise 1: String Concatenation Performance")
    print("-" * 40)

    # Method 1: Regular concatenation
    start = time.perf_counter()
    result = ""
    for i in range(100000):
        result = result + str(i)
    end_time = time.perf_counter()
    print("String concatenation:", round(end_time - start, 5), "seconds")