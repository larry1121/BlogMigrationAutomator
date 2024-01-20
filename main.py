import logging
import time
from tqdm import tqdm
from blog_migration_automate_by_url import blog_migration_automate_by_url

def main(start_i, end_i):
    max_attempts = 3  # 최대 시도 횟수 설정
    failed_urls = []
    success_count = 0

    total_posts = end_i - start_i + 1
    progress_bar_width = 30  # 진행 상황 막대의 길이

    with tqdm(total=total_posts, desc="Progress", unit="post") as pbar:
        for i in range(start_i, end_i + 1):
            test_url = f"https://giftedmbti.tistory.com/{i}"

            for attempt in range(max_attempts):
                try:
                    # 현재 진행 중인 블로그 정보 출력
                    logging.info("------------------------------------------------------------------------------------------------")
                    logging.info(f"Processing {i}/{end_i} - Attempt {attempt + 1}/{max_attempts}")

                    blog_migration_automate_by_url(test_url)
                    success_count += 1
                    pbar.update(1)  # 프로그레스 바 업데이트
                    break  # 성공하면 루프 종료
                except Exception as e:
                    logging.error(f"Error during blog migration: {str(e)}")
                    if attempt < max_attempts - 1:
                        # 재시도를 위해 잠시 기다림
                        time.sleep(5)
                    else:
                        # 최대 시도 횟수를 초과하면 실패한 URL을 기록
                        failed_urls.append((test_url, str(e)))

    # 전체 진행 상황 출력
    success_percentage = (success_count / total_posts) * 100
    logging.info(f"Total Success: {success_count}/{total_posts} ({success_percentage:.2f}%)")

    # 실패한 URL과 에러 사유 출력
    for url, error_reason in failed_urls:
        print(f"Failed URL: {url}, Error Reason: {error_reason}")

if __name__ == "__main__":
    # Example: Run main for URLs in the range [84, 100]
    main(201,248)
    
    
