def cut_before_first_a_tag(text):
    # Find the index of the first occurrence of <a tag
    a_tag_index = text.find('<a')

    # If <a tag is found, slice the text up to that index
    if a_tag_index != -1:
        return text[:a_tag_index]
    else:
        # If <a tag is not found, return the whole text
        return text

