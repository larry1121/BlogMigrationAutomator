import os
import logging
import requests
from urllib.parse import urlparse

# 기존에 정의된 외부 함수들의 임포트
from cut_before_first_a_tag import cut_before_first_a_tag
from generateCardnewsTitleImageByUrl import generateCardnewsTitleImageByUrl
from getBlogHTMLContent import getBlogHTMLContent

from translateHTML import translate_html
from uploadToWordpress import uploadToWordpress

# URL 유효성 검사 함수
def is_valid_url(url):
    parsed_url = urlparse(url)
    return all([parsed_url.scheme, parsed_url.netloc])

# URL 응답 코드 확인 함수
def check_url_response(url):
    if is_valid_url(url):
        try:
            response = requests.get(url)
            return response.status_code == 200, None
        except requests.RequestException as e:
            return False, str(e)
    else:
        return False, "Invalid URL format"

# 블로그 마이그레이션 자동화 함수
def blog_migration_automator(blog_url):
    is_valid, error = check_url_response(blog_url)
    if not is_valid:
        logging.error(f"Error with URL: {error}")
        return

    try:
        blog_content = getBlogHTMLContent(blog_url)
        translated_html = translate_html(cut_before_first_a_tag(blog_content))
        generateCardnewsTitleImageByUrl(blog_url)
        uploadToWordpress(blog_url, translated_html)
    except Exception as e:
        logging.error(f"Error during blog migration: {str(e)}")

if __name__ == "__main__":
    test_url = ""
    blog_migration_automator(test_url)
