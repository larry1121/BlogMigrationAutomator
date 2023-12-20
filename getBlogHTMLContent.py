from TistoryCrawler import TistoryCrawler

def getBlogHTMLContent(blog_url):

  #  블로그 크롤러 인스턴스 생성
  crawler = TistoryCrawler(blog_url)

  # 블로그 글 내용 출력
  blog_content = crawler.content
  print(blog_content)
  return blog_content