def check(s1, s2):
    for i in range(len(s1)):
        print(s1, s2)
        if s1[i] != s2[i]:
            return False
    return True
def find(string, pattern):
    psum = sum([ord(char) for char in pattern])
    ssum = sum([ord(char) for char in string[:len(pattern)]])
    for i in range(0, len(string)-len(pattern)+1):
        if i != 0:
            ssum += ord(string[i+len(pattern)-1]) 
        current = string[i : i + len(pattern)]
        if ssum == psum:
            if check(current, pattern):
                return f'match found at index {i}'
        ssum -= ord(string[i])
    return False


string = "ccaccaaedba"
pattern = "dba"
print(find(string, pattern))
