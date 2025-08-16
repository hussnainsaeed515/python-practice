# practice.py
# Hussnain's Python Practice 🚀

# --- Lists ---
nums = [10, 20, 30, 40, 50]
print(nums[2])
nums[2] = 35
print(nums)
nums.append(60)
print(nums)
nums.pop()
print(nums)

# --- Tuples ---
colours = ("red", "blue", "green")
print(colours[1])
print(len(colours))

# --- Dictionary ---
car = {"brand": "honda", "model": "civic", "year": 2020}
print(car["model"])
car["year"] = 2022
car["colour"] = "black"
print(car)
print(car.pop("brand"))

# --- Sets ---
a = {10, 20, 30}
b = {10, 20, 30}
print(a.union(b))
print(a.intersection(b))

# --- Loops ---
for i in range(1, 11):
    print(i, end=" ")
print()

for i in range(2, 21, 2):
    print(i)

i = 5
while i >= 1:
    print(i)
    i -= 1

nums = [2, 5, 7, 10, 15]
for i in nums:
    print(i * i)

for i in range(1, 10):
    if i == 5:
        break
    print(i)

for i in range(1, 10):
    if i == 5:
        continue
    print(i)
