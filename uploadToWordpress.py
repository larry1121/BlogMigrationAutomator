import json
import os
import requests
from urllib.parse import urljoin
from datetime import datetime
from dotenv import load_dotenv
from extract_mbti_tags import extract_mbti_tags

from getBlogMetaInfo import getBlogMetaInfo
from get_affiliate_text_by_url import get_affiliate_text_by_info
from remove_emoji import remove_emoji
import config
from sanitize_filename import sanitize_filename
# POST https://www.tistory.com/apis/post/write?
#   access_token={access-token}
#   &output={output-type}
#   &blogName={blog-name}
#   &title={title}
#   &content={content}
#   &visibility={visibility}
#   &category={category-id}
#   &published={published}
#   &slogan={slogan}
#   &tag={tag}
#   &acceptComment={acceptComment}
#   &password={password}

# def uploadToWordpress(blog_url,translated_html,image,category_ids,tag_ids,media_id):

#카테고리,태그 커스텀/url유효성검사

def uploadToWordpress(blog_url,translated_html):


  load_dotenv(verbose=True)
  # WP_URL = os.getenv('WP_URL')
  # WP_USERNAME = os.getenv('WP_USERNAME')
  # WP_PASSWORD = os.getenv('WP_PASSWORD')

  

  if config.DEST_LANG == "en":
      WP_URL = os.getenv('WP_URL')
      WP_USERNAME = os.getenv('WP_USERNAME')
      WP_PASSWORD = os.getenv('WP_PASSWORD')
  elif config.DEST_LANG == "ja":
      WP_URL = os.getenv('JP_WP_URL')
      WP_USERNAME = os.getenv('JP_WP_USERNAME')
      WP_PASSWORD = os.getenv('JP_WP_PASSWORD')
  else:
    # 다른 언어에 대한 처리
      raise ValueError("Unsupported DEST_LANG value")

  status = 'draft' #즉시발행：publish, 임시저장：draft

  BlogMetaInfo = getBlogMetaInfo(blog_url)

  slug = BlogMetaInfo['title'] #슬러그를 입력하세요

  title = BlogMetaInfo['title'] #글의 제목
  
  


  category_ids = [59] #카테고리 아이디는 글/카테고리/ 해당카테고리에 커서를 가져가면 하다나에 카테고리 아이디값이 나온다. 숫자다
  tag_ids = extract_mbti_tags(translated_html) #태그아이디도 카테고리 아이디 찾는 방법과 동일
  
  ImageCount = 0
  post_title = remove_emoji(str(BlogMetaInfo['title']))
  ImageName = f"{sanitize_filename(post_title)}_{ImageCount}"
  filename=f"{ImageName}.webp"  #이미지 파일이름
  folder_path=os.path.join(config.save_dir_path, f"{sanitize_filename(post_title)}")
  filepath=os.path.join(folder_path, filename)  # Save as JPG format

  url = urljoin(WP_URL, '/wp-json/wp/v2/media/')  
  f = open(filepath, 'rb')
  image_data = f.read()
  f.close()
  espSequence = bytes(filename, "utf-8").decode("unicode_escape")  

  headers = {
    'Content-Type': 'image/png',
    'Content-Disposition': 'attachment; filename=%s' % espSequence,                                 
}
  try:
    res2 = requests.post(
        url,
        data=image_data,
        headers=headers,
        auth=(WP_USERNAME, WP_PASSWORD),
    )

    res2.raise_for_status()  # 에러가 발생하면 예외를 일으킵니다.

    if res2.ok:
        print(f"TitleImage 업로드 성공 code:{res2.status_code}")
        media_info = res2.json()
        media_id = media_info['id']
        media_url = media_info['source_url']
    else:
        print(f"TitleImage 업로드 실패 code:{res2.status_code} reason:{res2.reason} msg:{res2.text}")

  except requests.exceptions.RequestException as e:
      print(f"TitleImage 업로드 Request Exception: {e}")

  media_info = res2.json()

  media_id = media_info['id'] 
  media_url = media_info['source_url'] 

  img_contents = f'''[caption id="attachment_{media_id}" align="aligncenter" width="500"]<img class="size-full wp-image-{media_id}" src="{media_url}" alt="{title}" width="500" height="500"> {title}[/caption]
<p>&nbsp;</p><br />
<p>&nbsp;</p>
'''

  affiliate_text = get_affiliate_text_by_info(title,tag_ids)

  content = img_contents + translated_html + affiliate_text  #본문내용을 적을것. html 로 적으면 된다



#===============================================================
#===============================================================

  user_ = WP_USERNAME
  pass_ = WP_PASSWORD

  payload = {"status": status,
            "slug": slug,
            "title": title,
            "content": content,
            "date": datetime.now().isoformat(),
            "categories": category_ids,
            "tags": tag_ids}
  if media_id is not None:
      payload['featured_media'] = media_id

  try:
    res = requests.post(urljoin(WP_URL, "wp-json/wp/v2/posts"),
                        data=json.dumps(payload),
                        headers={'Content-type': "application/json"},
                        auth=(user_, pass_))

    res.raise_for_status()  # 에러가 발생하면 예외를 일으킵니다.

    if res.ok:
         
        

        # JSON으로 디코딩하여 객체로 반환
        try:
            json_data = res.json()
            print(f"post 업로드 성공 code : {res.status_code} link : {json_data['guid']['raw']} generated_slug : {json_data['generated_slug']}")
            
        except json.JSONDecodeError:
            print("Response is not in JSON format.")
        
    else:
        print(f"실패 code:{res.status_code} reason:{res.reason} msg:{res.text}")

  except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")
