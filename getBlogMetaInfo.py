from googletrans import Translator
from TistoryCrawler import TistoryCrawler
from config import DEST_LANG

def getBlogMetaInfo(blog_url):

  # 블로그 크롤러 인스턴스 생성
  crawler = TistoryCrawler(blog_url)

  site_name = crawler.site_name
  title = crawler.title

  # Google Translate API의 번역기 초기화
  translator = Translator()

  
  BlogMetaInfo = {
      'site_name': translator.translate(site_name, DEST_LANG).text,
      'title': translator.translate(title, DEST_LANG).text
  }


  return BlogMetaInfo



if __name__ == "__main__":
    # Test with different blog names and post titles
    test_url = "https://giftedmbti.tistory.com/184"
    BlogMetaInfo = getBlogMetaInfo(test_url)
    print(BlogMetaInfo)

