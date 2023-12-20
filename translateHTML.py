from googletrans import Translator
from bs4 import BeautifulSoup

# Google Translate API의 번역기 초기화
translator = Translator()

def translate_html(html_doc, dest_language='en'):
    soup = BeautifulSoup(html_doc, 'html.parser')

    # 모든 텍스트 노드를 찾아 번역
    for element in soup.find_all(text=True):
        if element.strip():  # 공백이 아닌 텍스트에 대해서만 번역
            translated_text = translator.translate(element, dest=dest_language).text
            element.replace_with(translated_text)

    # 번역된 HTML 반환
    return str(soup)

# 예제 HTML 문서
html_doc = """
<html>
<head><title>예제</title></head>
<body>
    <h1>안녕하세요</h1>
    <p>이 문장은 번역될 것입니다.</p>
</body>
</html>
"""

# HTML 문서 번역
translated_html = translate_html(html_doc)

print(translated_html)
