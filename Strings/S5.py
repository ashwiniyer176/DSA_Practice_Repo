s1 = "ABACD"
s2 = "CDAAB"
s3 = "CDAB"


def areRotations(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        mid = len(s1) // 2
        rotated = s1[mid:] + s1[:mid]
        print(rotated)
        if rotated == s2:
            return True
        return False


print(areRotations(s1, s2))
print(areRotations(s1, s3))
