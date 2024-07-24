from typing import List


class Codec:
    def __init__(self):
        self.delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        if not strs:
            return ""

        return ''.join(f"{len(s)}{self.delimiter}{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        result = []
        i = 0
        while i < len(s):
            j = s.index(self.delimiter, i)
            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i + length])
            i += length
        return result


# Example usage:
codec = Codec()

# Example 1
input1 = ["neet", "code", "love", "you"]
encoded1 = codec.encode(input1)
print(encoded1)
decoded1 = codec.decode(encoded1)
print(f"Example 1: {decoded1 == input1}")  # Should print True

# Example 2
input2 = ["we", "say", ":", "yes"]
encoded2 = codec.encode(input2)
decoded2 = codec.decode(encoded2)
print(f"Example 2: {decoded2 == input2}")  # Should print True