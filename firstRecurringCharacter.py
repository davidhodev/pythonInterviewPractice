# Returns the first returning character in a string
# We want to use a hash for the best efficiency
# O(nlogn)
def firstReucrringCharacter(phrase):
    hashSet = {}
    for char in phrase:
        if char in hashSet:
            return char
        hashSet[char] = 1
    return False

print(firstReucrringCharacter('asdfghjklasdfgh'))