"""
Buatkan 3 contoh operator logika
"""
# Contoh AND
P = True  # "I love you"
Q = True  # "You make me happy"

hasil_and = P and Q
print(hasil_and)  # Output: True, karena keduanya P and Q adalah True

# Contoh of OR
P = True  # "I love you"
Q = False  # "I'm not happy right now" (Tapi Boong!)

hasil_or = P or Q
print(hasil_or)  # Output: True, karena P itu True, walaupun si Q itu False

# Contoh NOT
P = True  # "I love you"

hasil_not = not P
print(hasil_not)  # Output: False, karena P itu True, dan 'not' ngebalikin artinya jadi False

# DONE