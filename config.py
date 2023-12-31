# OpenAI(not yet)
OPENAI_API_KEY = 'sk-'

DEST_LANG="en"

import os
import sys

if getattr(sys, 'frozen', False):
    # The application is frozen
    bundle_dir = sys._MEIPASS
else:
    # The application is not frozen
    # Change this bit to the path where you store your data files:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

BUNDLE_DIR_PATH = bundle_dir

save_dir_path = bundle_dir

def set_save_path(save_path):
    global save_dir_path  # 전역 변수임을 명시
    save_dir_path = save_path



if DEST_LANG == "ja":
    FONT_PATH = os.path.join(bundle_dir, 'NotoSansJP-Regular.ttf')
elif DEST_LANG == "en":
    FONT_PATH = os.path.join(bundle_dir, 'NotoSans-Regular.ttf')
else:
    # 다른 언어에 대한 처리를 추가하려면 여기에 추가 코드 작성
    raise ValueError("Unsupported DEST_LANG: {}".format(DEST_LANG))

# FONT_PATH를 사용하여 필요한 작업을 수행

IMAGE_SIZE = (1080, 1080)  # Instagram card news size
BACKGROUND_COLOR = (255, 220, 220)  # 연한 핑크색
# (255, 235, 235) 더 연한 핑크색
TEXT_COLOR = (0, 0, 0) # 검은색 글씨
BORDER_COLOR = (255, 255, 255) #하얀색 경계선
BORDER_WIDTH = 15

# TITLE_CONSTANT
TITLE_BLOG_NAME_FONT_SIZE = 65

# CONTENT_CONSTANT
BASE_FONT_SIZE = 50

# BRANDING_CONSTANT
BRANDING_CIRCLE_RADIUS = 200
BRANDING_TEXT = "매일 MBTI 연애 팁을 올립니다.\n팔로우 하시고 매일 연애 팁 받아보세요."
BRANDING_TEXT_FONT_SIZE = 50
BRANDING_BLOG_NAME_FONT_SIZE = 70
HASHTAG = "      . . .        #MBTI#ENFP#ISTJ#ISFJ#INFJ#INTJ#ISTP#ISFP#INFP#INTP#ESTP#ESFP#ENTP#ESTJ#ESFJ#ENFJ#ENTJ#인스타툰"
