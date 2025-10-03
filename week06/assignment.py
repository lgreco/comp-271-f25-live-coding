def simple_frequency_counter(message: str) -> dict[str, int]:
    frequency = {}
    if message is not None and len(message) > 0:
        for char in message:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

pangram = "sphinx of black quartz judge my vow"
f = simple_frequency_counter(pangram)
print(f)

test = "now is the winter of our discontent made glorious summer by this on of york"
print(simple_frequency_counter(test))