def similar(target: list[str], reference: list[str]) -> str:
    if not target or not reference:
        return "0.00%"
    
    matches = 0
    for word in target:
        if word in reference:
            matches += 1
    
    percent = (matches / len(target)) * 100
    return str(round(percent, 2)) + "%"
print(similar(["a", "b", "c", "d"], ["c", "d", "e", "f"]))

#-------------------------------------------------------

def reverse(data: list[str], spaces: int) -> str | None:
    if not data:
        return None

    result = ""
    count = 0
    for word in data:
        result = " " * (spaces * count) + word + "\n" + result
        count += 1
    return result
names = ["Howard", "Jarvis", "Morse", "Loyola"]
print(reverse(names, 2))
#--------------------------------------------------------

def frequency(message: str) -> list[int]:
    numbers = [0] * 27
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in message:
        if char == ' ':
            numbers[26] += 1
        else:
            found = False
            for i in range(len(alphabet)):
                if not found and alphabet[i] == char:
                    numbers[i] += 1
                    found = True

    return numbers
pangram = "sphinx of black quartz judge my vow"
counts = frequency(pangram)

print("Letter frequencies in the pangram:")
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alphabet)):
    print(alphabet[i] + ": " + str(float(counts[i])))
print("space: " + str(float(counts[26])))
#---------------------------------------------------




