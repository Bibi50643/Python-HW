import random,string
print("random String of length 5:",''.join(random.choice(string.ascii_letters) for i in range(5)))

