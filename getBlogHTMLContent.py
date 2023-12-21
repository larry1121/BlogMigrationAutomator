from TistoryCrawler import TistoryCrawler

def getBlogHTMLContent(blog_url):

  #  블로그 크롤러 인스턴스 생성
  crawler = TistoryCrawler(blog_url)

  # 블로그 글 내용 출력
  blog_content = crawler.content

  return blog_content

if __name__ == "__main__":
    test_url ="https://giftedmbti.tistory.com/167"
    getBlogHTMLContent(test_url)
