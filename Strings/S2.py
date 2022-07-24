from cmath import e


odd = "MALAYALAM"
even = "mbaabm"
text = "lksdfnlsknfls"


def checkPalindrome(s):
    mid = (0 + len(s)) // 2
    for i in range(mid + 1):
        if s[i] != s[-i - 1]:
            return False
    return True


print(checkPalindrome(odd))
print(checkPalindrome(even))
print(checkPalindrome(text))
