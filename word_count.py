value = """Abebe loves Ethiopia and loves kenya too.
Abebech loves Ethiopia but hates kenya because she is racist.
We all love Abebe but hate Abebech because she hates Ethiopia"""
wordlist = value.split()
words = dict()
for i in wordlist:
        words[i] = words.get(i, 0) + 1

print("Ethiopia was mentioned", words["Ethiopia"], "times")
print(words)
