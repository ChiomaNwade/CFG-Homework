def is_isogram(word):
    """
The function checks whether a word is an isogram,
meaning that no letter is repeated within the word.
It returns True if the word is an isogram,
indicating that each letter appears only once.
 Otherwise, it returns False,
 indicating that there are repeated letters within the word.
    """
    try:
        if not isinstance(word, str):
            raise TypeError("Input should be a string.")
        word_lower = word.lower()
        unique_letters = set(word_lower)
        return len(unique_letters) == len(word_lower)
    except Exception as e:
        print("An error occurred:", str(e))
        return False
