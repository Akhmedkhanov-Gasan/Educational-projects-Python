def first_non_repeating_word(text):
    words = text.split()
    count = {}
    for i in words:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    for i in words:
        if count[i] == 1:
            return i
    return None

def has_duplicates(nums):

    seen = {}
    for i in nums:
        if i in seen:
            return True
        else:
            seen[i] = 1
    return False

def group_anagram(words):
    sorted_words = {}

    for i in words:
        if tuple(sorted(i)) not in sorted_words:
            sorted_words[tuple(sorted(i))] = []
            sorted_words[tuple(sorted(i))].append(i)
        else:
            sorted_words[tuple(sorted(i))].append(i)
    return list(sorted_words.values())

print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
