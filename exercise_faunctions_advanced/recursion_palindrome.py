def palindrome(string, index):
    length = len(string) // 2
    if index == length:
        return f"{string} is a palindrome"

    if string[index] == string[-1-index]:
        return palindrome(string, index + 1)

    return f"{string} is not a palindrome"


print(palindrome("peter", 0))