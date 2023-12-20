import os
import logging
from cut_before_first_a_tag import cut_before_first_a_tag
from generateCardnewsTitleImageByUrl import generateCardnewsTitleImageByUrl
from getBlogHTMLContent import getBlogHTMLContent
from getBlogMetaInfo import getBlogMetaInfo
from translateHTML import translate_html
from uploadToWordpress import uploadToWordpress



def BlogMigrationAutoamtor(blog_url):

  blog_content = getBlogHTMLContent(blog_url)
  
  translated_html = translate_html(cut_before_first_a_tag(blog_content))
  generateCardnewsTitleImageByUrl(blog_url)




  uploadToWordpress(blog_url,translated_html)



if __name__ == "__main__":
    test_url ="https://giftedmbti.tistory.com/167"
    BlogMigrationAutoamtor(test_url)
