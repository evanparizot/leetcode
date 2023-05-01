
def merge(word1: str, word2: str) -> str:
    result = ""
    if len(word1) > len(word2):
        for i, l in enumerate(word2):
            result += word1[i]
            result += l
        result += word1[len(word2):]
    else:
        for i, l in enumerate(word1):
            result += l
            result += word2[i]
        result += word2[len(word1):]

    return result