import logging
import time
from tqdm import tqdm
from datetime import datetime
from blog_migration_automate_by_url import blog_migration_automate_by_url

def main(start_i, end_i):
    max_attempts = 3
    failed_urls = []
    success_logs = []

    total_posts = end_i - start_i + 1

    with tqdm(total=total_posts, desc="Progress", unit="post") as pbar:
        for i in range(start_i, end_i + 1):
            start_time = datetime.now()
            test_url = f"https://giftedmbti.tistory.com/{i}"

            for attempt in range(max_attempts):
                try:
                    logging.info("------------------------------------------------------------------------------------------------")
                    logging.info(f"Processing {i}/{end_i} - Attempt {attempt + 1}/{max_attempts}")

                    # 예상되는 변환 후의 URL 형식
                    new_url = f"https://newblog.com/posts/{i}"

                    # blog_migration_automate_by_url 함수가 변환 후의 URL을 반환하도록 가정
                    result_url = blog_migration_automate_by_url(test_url)
                    elapsed_time = datetime.now() - start_time
                    success_logs.append((test_url, result_url, elapsed_time))
                    pbar.update(1)
                    break
                except Exception as e:
                    logging.error(f"Error during blog migration: {str(e)}")
                    if attempt < max_attempts - 1:
                        time.sleep(5)
                    else:
                        failed_urls.append((test_url, str(e)))

    generate_report(success_logs, failed_urls, total_posts)

def generate_report(success_logs, failed_urls, total_posts):
    success_count = len(success_logs)
    success_percentage = (success_count / total_posts) * 100

    with open("migration_report.txt", "w") as file:
        file.write(f"Total Success: {success_count}/{total_posts} ({success_percentage:.2f}%)\n")
        file.write("Successful Migrations:\n")

        for original_url, new_url, elapsed_time in success_logs:
            file.write(f"Original URL: {original_url}, New URL: {new_url}, Time Taken: {elapsed_time}\n")

        file.write("\nFailed Migrations:\n")
        for url, error_reason in failed_urls:
            file.write(f"Failed URL: {url}, Error Reason: {error_reason}\n")

if __name__ == "__main__":
    main(101, 200)
