import os
import logging
import requests
from urllib.parse import urlparse
from config import DEST_LANG

# 기존에 정의된 외부 함수들의 임포트
from cut_before_first_a_tag import cut_before_first_a_tag
from generateCardnewsTitleImageByUrl import generateCardnewsTitleImageByUrl
from getBlogHTMLContent import getBlogHTMLContent
from translateHTML import translate_html
from uploadToWordpress import uploadToWordpress

# 로깅 설정
logging.basicConfig(level=logging.INFO)  # INFO 레벨 이상의 로그를 출력

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
        logging.info("------------------------------------------------------------------------------------------------")
        logging.info(f"Processing blog migration for URL: {blog_url}")

        # 블로그 컨텐츠 가져오기
        logging.info("Getting blog content...")
        blog_content = getBlogHTMLContent(blog_url)

        # HTML 번역
        logging.info("Translating HTML content...")
        translated_html = translate_html(cut_before_first_a_tag(blog_content), DEST_LANG)

        # 카드 뉴스 제목 이미지 생성
        logging.info("Generating card news title image...")
        generateCardnewsTitleImageByUrl(blog_url)

        # WordPress에 업로드
        logging.info("Uploading to WordPress...")
        uploadToWordpress(blog_url, translated_html)

        logging.info("Blog migration completed successfully.")
    except Exception as e:
        logging.error(f"Error during blog migration: {str(e)}")

import time

import time

if __name__ == "__main__":
    max_attempts = 3  # 최대 시도 횟수 설정
    failed_urls = []

    for i in range(1, 101):
        test_url = f"https://giftedmbti.tistory.com/{i}"

        for attempt in range(max_attempts):
            try:
                blog_migration_automator(test_url)
                break  # 성공하면 루프 종료
            except Exception as e:
                logging.error(f"Error during blog migration: {str(e)}")
                if attempt < max_attempts - 1:
                    # 재시도를 위해 잠시 기다림
                    time.sleep(5)
                else:
                    # 최대 시도 횟수를 초과하면 실패한 URL을 기록
                    failed_urls.append((test_url, str(e)))

    # 실패한 URL과 에러 사유 출력
    for url, error_reason in failed_urls:
        print(f"Failed URL: {url}, Error Reason: {error_reason}")

