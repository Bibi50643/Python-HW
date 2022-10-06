class Wordplay:
    def __init__(self):
        self.list = []


    def words_with_length(self,length):
        words = []
        for word in self.list:
            if len(word) == length:
                words.append(word)
        return "length : {}  Words: {}".format(length,words)

    def starts_with(self, s):
        words = []  
        for word in self.list:
            if (word[0] == s):
                words.append(word)
        return "The first letter: {} words: {}".format(s,words)

    def ends_with(self,s):
        words =[]
        for word in self.list:
            if word[-1] == s:
                words.append(word)
        return "Last letter:{} Word:{}".format(s,words)

    def palindromes(self):
        words =[]
        for word in self.list:
            if word[::1] == word[::-1]:
                words.append(word)
        return "Palindrome:{}".format(words)

    def only_L(self):
        words =[]
        for word in self.list:
            if "l" in word:
                words.append(word)
        return "Words with L:{}".format(words)


    def avoids_L(self):
        words = []
        for word in self.list:
            if "l" not in word:
                words.append(word)
        return "Words without L:{}".format(words)


x = Wordplay()
x.list=["create","method","stringwes","lerewef","bibi","character","called","assa","Alma"]
print(x.words_with_length(4))
print(x.starts_with("s"))
print(x.ends_with("s"))
print(x.palindromes())
print(x.only_L())
print(x.avoids_L())