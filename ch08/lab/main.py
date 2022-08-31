from StringUtility import StringUtility


# Provided main() calls your class methods with interesting inputs,
# using test() to check if each result is correct or not.
def main():

    # Each line calls donuts, compares its result to the expected for that call.
    test_strings = ["interesting", "aardvark", "aaa", "aeiouAEIOU", "a b c d e f g h i j k l m n o p q r s t u v w x y z", '']
    su = []
    for i in test_strings:
        su.append(StringUtility(i))

    print("=========== Testing __str__ method ===========")
    expected_results = ["interesting", "aardvark", "aaa", "aeiouAEIOU", "a b c d e f g h i j k l m n o p q r s t u v w x y z", '']
    i = 0
    for s in su:
        result = str(s)
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert(result == expected_results[i])
        i += 1

    print("=========== Testing vowels method ===========")
    expected_results = ["4", "3", "3", "many", "many", "0"]
    i = 0
    for s in su:
        result = s.vowels()
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert(result == expected_results[i])
        i += 1

    print("=========== Testing bothEnds method ===========")
    expected_results = ["inng", "aark", "aaaa", "aeOU", "a  z", '']
    i = 0
    for s in su:
        result = s.bothEnds()
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert(result == expected_results[i])
        i += 1

    print("=========== Testing fixStart method ===========")
    expected_results = ["interest*ng", "a*rdv*rk", "a**", "aeiouAEIOU", "a b c d e f g h i j k l m n o p q r s t u v w x y z", '']
    i = 0
    for s in su:
        result = s.fixStart()
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert(result == expected_results[i])
        i += 1

    print("=========== Testing asciiSum method ===========")
    expected_results = [1196,844,291,902,3647,0]
    i = 0
    for s in su:
        result = s.asciiSum()
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert(result == expected_results[i])
        i += 1

    print("=========== Testing cipher method ===========")
    expected_results = ["tyepcpdetyr", "iizldizs", "ddd", "kosyeKOSYE", "z a b c d e f g h i j k l m n o p q r s t u v w x y", ""]
    i = 0
    for s in su:
        result = s.cipher()
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert(result == expected_results[i])
        i += 1

    print("=========== Testing __str__ method (again) ===========")
    expected_results = ["interesting", "aardvark", "aaa", "aeiouAEIOU", "a b c d e f g h i j k l m n o p q r s t u v w x y z", '']
    i = 0
    for s in su:
        result = str(s)
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert(result == expected_results[i])
        i += 1

    print("=========== Tests Complete! ===========")

main()
