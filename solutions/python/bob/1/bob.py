def response(hey_bob):
    """
    Determines Bob's response based on the tone and content of an input string.

    The function analyses the input string and determines an appropriate response based on
    whether it is a question, a shouted statement (all uppercase), both, neither, or an empty
    string. Responses are returned as predefined phrases specific to each case.

    Arguments:
        hey_bob: Input string directed towards Bob. It is analyzed to determine if it is a
            question, shouting, both, or empty.

    Returns:
        str: A response from Bob, which varies depending on the content and tone of the input.
    """
    hey_bob = hey_bob.strip()
    is_shouting = hey_bob.isupper()
    is_question = hey_bob.endswith("?")

    if hey_bob == "":
        return "Fine. Be that way!"
    elif is_question and is_shouting:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_shouting:
        return "Whoa, chill out!"
    else:
        return "Whatever."
