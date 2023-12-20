import os
import logging
from generateCardnewsTitleImageByUrl import generateCardnewsTitleImageByUrl
from getBlogHTMLContent import getBlogHTMLContent
from getBlogMetaInfo import getBlogMetaInfo
from translateHTML import translate_html



def BlogMigrationAutoamtor(blog_url):

  blog_content = getBlogHTMLContent(blog_url)
  translated_html = translate_html(blog_content)
  generateCardnewsTitleImageByUrl(blog_url)




uploadToWordpress



if __name__ == "__main__":
    test_url ="https://giftedmbti.tistory.com/167"
