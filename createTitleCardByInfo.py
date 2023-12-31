from PIL import Image, ImageDraw, ImageFont, WebPImagePlugin
import os
import config
from remove_emoji import remove_emoji
from config import BORDER_COLOR, BORDER_WIDTH, DEST_LANG,  IMAGE_SIZE, FONT_PATH, TEXT_COLOR, BACKGROUND_COLOR, TITLE_BLOG_NAME_FONT_SIZE
from sanitize_filename import sanitize_filename
import unicodedata
from PIL import ImageFont
from PIL import ImageFont

def calculate_font_size(font_path, text, max_size, min_size, image_size):
    font_size = max_size
    font = ImageFont.truetype(font_path, font_size)
    text_width, _ = font.getsize(text)

    # Adjust font size to fit the width of the image
    while font_size > min_size and text_width > 0.9 * image_size[0]:
        font_size -= 1
        font = ImageFont.truetype(font_path, font_size)
        text_width, _ = font.getsize(text)

        # if DEST_LANG == "ja":
        #       # Special handling for Japanese text
        #     lines = []
        #     for char in text:
        #         if lines and font.getsize(lines[-1] + char)[0] <= 0.9 * image_size[0]:
        #             lines[-1] += char
        #         else:
        #             lines.append(char)

        #     # Adjust font size to fit the height of the image
        #     text_height = font.getsize(lines[0])[1]
        #     while font_size > min_size and text_height * len(lines) > 0.9 * image_size[1]:
        #         font_size -= 1
        #         font = ImageFont.truetype(font_path, font_size)
        #         text_height = font.getsize(lines[0])[1]

    return font, font_size

def is_japanese(text):
    for char in text:
        if 'CJK' in unicodedata.name(char, ''):
            return True
    return False

def split_text(post_title, max_line_length,font,is_japanese=True):
    text_lines = []
    current_line = ""
    print(f"is_japanese = {is_japanese}")

    if is_japanese:


      for char in post_title:
        test_line = current_line + char
        test_width, _ = font.getsize(test_line)

        if test_width > max_line_length:
            text_lines.append(current_line)
            
            current_line = char
        else:
            current_line = test_line

        

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

def createTitleCardByInfo(BlogMetaInfo):
    post_title = remove_emoji(str(BlogMetaInfo['title']))
    blog_name = BlogMetaInfo['site_name']
    
    # 이미지 설정
    size = IMAGE_SIZE
    background_color = BACKGROUND_COLOR
    font_path = FONT_PATH

    min_font_size = 60
    max_font_size = 120
    text_color = TEXT_COLOR

    # 블로그 이름과 글의 제목
    blogname_font_size = TITLE_BLOG_NAME_FONT_SIZE

    # 새로운 값 추가: 테두리 색상 및 너비
    border_color = BORDER_COLOR
    border_width = BORDER_WIDTH  # Change this value to adjust the border width

    # 이미지 생성
    image = Image.new("RGB", size, background_color)

    # 제목 글자 크기 계산
    font, font_size = calculate_font_size(font_path, post_title, max_font_size, min_font_size,IMAGE_SIZE)
    text_width, text_height = font.getsize(post_title)
    
    max_line_length = 0.8 * IMAGE_SIZE[0]

    # 텍스트를 여러 줄로 분할
    text_lines = split_text(post_title, max_line_length,font, is_japanese(post_title))

    
    # current_line = ""
    # words = post_title.split()
    # for word in words:
    #     test_line = current_line + " " + word if current_line else word
    #     test_width, _ = font.getsize(test_line)
    #     if test_width <= max_line_length:
    #         current_line = test_line
    #     else:
    #         text_lines.append(current_line)
    #         current_line = word
    # if current_line:
    #     text_lines.append(current_line)
    # 기능 분할 필요

    # 왼쪽 상단의 블로그 이름의 폰트 크기 적용
    blog_font = ImageFont.truetype(font_path, blogname_font_size)

    # 이미지에 글자 쓰기
    draw = ImageDraw.Draw(image)
    text_y = (size[1] - len(text_lines) * text_height) // 2 + 40
    for line in text_lines:
        text_x = (size[0] - font.getsize(line)[0]) // 2
        draw.text((text_x, text_y), line, font=font, fill=text_color, align='center')
        text_y += text_height

    blog_text_x = 10
    blog_text_y = 10
    draw.text((blog_text_x, blog_text_y), f"@{blog_name}", font=blog_font, fill=text_color)

    # 테두리 그리기
    border_rect = [(0, 0), (size[0] - 1, size[1] - 1)]
    draw.rectangle(border_rect, outline=border_color, width=border_width)

    # 이미지 저장
    post_title_sanitized = sanitize_filename(post_title)
    
    directory_path = os.path.join(config.save_dir_path, post_title_sanitized)

    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

            


        # 이미지 저장 부분 수정
        filename = os.path.join(directory_path, f"{post_title_sanitized}_0.webp")
        image.save(filename, format="WEBP")
        print(f"Title Image : {post_title_sanitized}_0.webp 저장 완료\n\n")
    except OSError as e:
        print(f"파일 저장 오류: {e} ,cwd : {os.getcwd()}")
        

if __name__ == "__main__":
    # Test with different blog names and post titles
    createTitleCardByInfo({'site_name': 'giftedmbti', 'title': '[MBTI] INTJとINTPの友情の互換性：お互いをよりよく理解する方法を見つけてください！'})
