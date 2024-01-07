# BlogMigrationAutomator

## 1. 프로젝트 설명

BlogMigrationAutomator는 사용자가 지정한 URL 범위 내의 블로그 글을 크롤링하여 자동으로 번역한 후, 영어 또는 일본어 워드프레스 블로그에 업로드하는 자동화 도구입니다. 이 도구는 번역된 콘텐츠를 워드프레스에 효율적으로 업로드하여 블로그 마이그레이션시의 블로그 관리자의 작업 부담을 줄여줍니다.

## 2. 사용 라이브러리

- `bs4`: HTML 문서를 파싱하고 크롤링합니다.
- `requests`: 웹 페이지 데이터를 요청하고 받아옵니다.
- `python-dotenv`: 환경 변수를 관리합니다.

- `Google Cloud Translation API` : 블로그 글을 다양한 언어로 번역합니다.
- `WordPress API` : 워드프레스에 글을 업로드 합니다.

자세한 라이브러리 목록 및 버전은 `requirements.txt` 파일에서 확인할 수 있습니다.

## 3. 설치 및 실행방법

### 설치방법
pip install -r requirements.txt
이 명령어를 통해 필요한 라이브러리를 설치할 수 있습니다.

### 실행방법
python main.py
`main.py` 스크립트를 실행하여 프로젝트를 시작합니다.

## 5. 코드 구조

- `main.py`: 프로그램의 진입점으로, 전체 프로세스를 조정합니다.
- `BlogCrawler.py` & `TistoryCrawler.py`: 특정 블로그에서 글을 크롤링하는 기능을 담당합니다.
- `uploadToWordpress.py`: 번역된 글을 워드프레스에 업로드합니다.
- `translateHTML.py`: HTML 형식의 블로그 글을 지정된 언어로 번역합니다.
- `createTitleCardByInfo.py`: 블로그 포스트 정보를 바탕으로 타이틀 카드 이미지를 생성합니다.
- `extract_mbti_tags.py`: 블로그 글에서 MBTI 태그를 추출하여 분석하는 기능을 제공합니다.
- `config.py`: 프로젝트의 설정을 관리하는 곳으로, 언어 설정, API 키 등을 포함합니다.

## 6. 설정 변경 방법

`config.py`에서 언어 설정, API 키 등 다양한 설정을 변경할 수 있습니다. 이 파일에서 목표 언어, API 키 등을 설정하여 프로그램의 동작을 사용자화할 수 있습니다.

## 7. 라이센스 및 저작권 정보

이 프로그램은 MIT 라이센스 하에 배포됩니다. 자세한 정보는 프로젝트의 `LICENSE` 파일을 참조하세요.

## 8. 개발자 정보

- GitHub: [https://github.com/larry1121](https://github.com/larry1121)
- 이메일: [ghy200000@gmail.com](mailto:ghy200000@gmail.com)
