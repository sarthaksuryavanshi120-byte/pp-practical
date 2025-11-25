# ============================
# 1️⃣ STRINGS
# ============================
s1 = "Hello"
s2 = "Python"

print("\n--- Strings ---")
print("String 1:", s1)
print("Indexing:", s1[1])       # 'e'
print("Slicing:", s1[1:4])      # 'ell'
print("Concatenation:", s1 + " " + s2)
print("Repetition:", s1 * 3)    # "HelloHelloHello"


# ============================
# 2️⃣ LISTS
# ============================
lst1 = [10, 20, 30, 40]
lst2 = [50, 60]

print("\n--- Lists ---")
print("List:", lst1)
print("Indexing:", lst1[2])      # 30
print("Slicing:", lst1[:3])      # [10,20,30]
print("Concatenation:", lst1 + lst2)
print("Repetition:", lst1 * 2)


# ============================
# 3️⃣ TUPLES (IMMUTABLE)
# ============================
t1 = (1, 2, 3)
t2 = (4, 5)

print("\n--- Tuples ---")
print("Tuple:", t1)
print("Indexing:", t1[0])        # 1
print("Slicing:", t1[1:])        # (2,3)
print("Concatenation:", t1 + t2)
print("Repetition:", t1 * 3)


# ============================
# 4️⃣ DICTIONARY (KEY:VALUE)
# ============================
d = {"name": "Alex", "age": 21, "city": "Mumbai"}

print("\n--- Dictionary ---")
print("Dictionary:", d)
print("Access by key:", d["name"])   # Indexing using key
# No concatenation or repetition for dict
d["age"] = 22                        # Update existing value
print("Updated age:", d)

# Slicing not allowed in dictionary


# ============================
# 5️⃣ SET (Unique & Unordered)
# ============================
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("\n--- Sets ---")
print("Set:", set1)
# No indexing or slicing allowed in sets because they are unordered
print("Union:", set1 | set2)         # Concatenation equivalent
print("Intersection:", set1 & set2)
print("Repetition not allowed in sets")

