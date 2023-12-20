import json
import os
import requests
from urllib.parse import urljoin
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(verbose=True)

WP_URL = os.getenv('WP_URL')
WP_USERNAME = os.getenv('WP_USERNAME')
WP_PASSWORD = os.getenv('WP_PASSWORD')

status = 'draft' #즉시발행：publish, 임시저장：draft

slug = 'python-auto-post-rest-api-test' #슬러그를 입력하세요

title = '파이썬 자동포스팅' #글의 제목
content = '여기에 내용을 적으세요' #본문내용을 적을것. html 로 적으면 된다
category_ids = [22] #카테고리 아이디는 글/카테고리/ 해당카테고리에 커서를 가져가면 하다나에 카테고리 아이디값이 나온다. 숫자다
tag_ids = [21] #태그아이디도 카테고리 아이디 찾는 방법과 동일
media_id=None   #이번에는 이미지 업로드를 하지 않을거기 때문에 None 을 입력했습니다. 
#추후에 이미지를 업로드 하게 된다면 업로드 된 이미지의 아이디를 입력하시면 특성이미지로 설정이 됩니다.

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

res = requests.post(urljoin(WP_URL, "wp-json/wp/v2/posts"),
                    data=json.dumps(payload),
                    headers={'Content-type': "application/json"},
                    auth=(user_, pass_))

if res.ok:
    print("성공 code:{res.status_code}")    
else:
    print(f"실패 code:{res.status_code} reason:{res.reason} msg:{res.text}")