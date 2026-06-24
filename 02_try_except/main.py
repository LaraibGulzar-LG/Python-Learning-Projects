# 1. ZeroDivisionError handle karo
print("--------------------------------ZeroDivisionError--------------------------------")
try:
    result = 10 / 0
except ZeroDivisionError as MineError:
    print("Error: Zero se divide nahi kar sakte!")
    print("Python ne ye error diya hai:", MineError)


# 2. File not found
print("--------------------------------FileNotFoundError--------------------------------")
try:
    with open('ghost_file.txt', 'r') as f:
        data = f.read()
except FileNotFoundError as MineError:
    print("Error: File nahi mili!")
    print("Python ne ye error diya hai:", MineError)


# 3. ValueError handle karo
print("--------------------------------ValueError--------------------------------")
try:
    num = int("abc")
except ValueError as MineError:
    print("Error: String ko integer mein convert nahi kar sakte!")
    print("Python ne ye erro diya hai:", MineError)


# 4. Multiple exceptions
print("--------------------------------MultipleExceptions--------------------------------")
try:
    num = int(input("Enter number: "))
    result = 100 / num
except ValueError:
    print("Error: Sirf number daalo!")
except ZeroDivisionError:
    print("Error: 0 nahi daal sakte!")
except Exception as e:
    print(f"Koi aur error: {e}")


# 5. Try-Except-Else-Finally
print("--------------------------------TryExceptElseFinally--------------------------------")
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Zero nahi!")
except ValueError:
    print("Yaha Number dalo!")
else:
    print("Result:", result)  # Agar error nahi aayi
finally:
    print("Ye line hamesha print hogi!")  # Hamesha run hoga


# 6. Custom exception raise karo
print("--------------------------------RaisingCustomException--------------------------------")
def age_checking(age):
    if age < 0:
        raise ValueError("Common Sense Hai Age Negative nhi ho skti!")
    return age

try:
    Age_batao = int(input("Enter number: "))
    age_checking(Age_batao)
except ValueError as e:
    print("Custom Error:", e)
else:
    print("Tumhari Age is :" , Age_batao)


