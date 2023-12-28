import unicodedata

def is_japanese(text):
    for char in text:
        if 'CJK' in unicodedata.name(char, ''):
            return True
    return False

def split_text(post_title, max_line_length, is_japanese=True):
    text_lines = []
    current_line = ""

    if is_japanese:
        for char in post_title:
            if unicodedata.category(char) in ('Zs', 'Zl', 'Zp'):
                test_line = current_line + char if current_line else char
                test_width, _ = font.getsize(test_line)
                if test_width <= max_line_length:
                    current_line = test_line
                else:
                    text_lines.append(current_line)
                    current_line = char
            else:
                current_line += char
    else:
        words = post_title.split()
        for word in words:
            test_line = current_line + " " + word if current_line else word
            test_width, _ = font.getsize(test_line)
            if test_width <= max_line_length:
                current_line = test_line
            else:
                text_lines.append(current_line)
                current_line = word
        if current_line:
            text_lines.append(current_line)

    return text_lines

# Example usage
post_title = "日本語のテキストを分割する例です。これは非常に長い見出しの場合を想定しています。"
max_line_length = 0.8 * IMAGE_SIZE[0]

# Check if the text is Japanese
japanese_text = is_japanese(post_title)

# Split the text based on language
result_lines = split_text(post_title, max_line_length, is_japanese=japanese_text)

for line in result_lines:
    print(line)
