# word count in string
n='rajeshnahak'
def word_counter(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count
print(word_counter(n))


# word count in tuplle
y=('a','b','c','d','a')
def word_counter(s):
    r=list(s)
    count={}
    for char in r:
        count[char]=r.count(char)
    return count
print(word_counter(y))