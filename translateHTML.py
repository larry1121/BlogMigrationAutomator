from googletrans import Translator
from bs4 import BeautifulSoup

# Google Translate API의 번역기 초기화
translator = Translator()
translator.raise_Exception = True

def translate_html(html_doc, dest_language='en'):
    soup = BeautifulSoup(html_doc, 'html.parser')

    # 모든 텍스트 노드를 찾아 번역
    for element in soup.find_all(text=True):
        if element.strip():  # 공백이 아닌 텍스트에 대해서만 번역
            translated_text = translator.translate(element, dest=dest_language).text
            element.replace_with(translated_text)

    # 번역된 HTML 반환
    return str(soup)

# 예제 HTML 문서
html_doc = """
<div class="tt_article_useless_p_margin contents_style"><p data-ke-size="size16">💡 이상적인 연애를 꿈꾸는 INTJ들에게 도움이 될만한 팁과 흥미로운 사례를 소개합니다! 자신과 어울리는 파트너를 찾고 싶은 <b>INTJ</b>들을 위한 특별한 가이드, 지금 시작해보세요! 👀</p>
<h2 data-ke-size="size26"><b>INTJ</b>: 미지의 영혼을 지배하는 유형</h2>
<p data-ke-size="size16"><b>INTJ</b>들은 <b>MBTI</b>에서 가장 희귀한 유형으로서, 독특한 사고력과 높은 지능을 지녔습니다. 자신만의 세계를 갖고 있으며, 목표를 이루기 위해 끊임없이 사고하고 계획합니다. 그러나 그들이 연애를 시작할 때, 어떻게 해야 할지 모르는 경우가 많습니다. 이제 우리와 함께 <b>INTJ</b>들에게 이상적인 연애를 찾아가보세요! 🚀</p>
<hr data-ke-style="style1"/>
<h2 data-ke-size="size26">매력적인 도전자, <b>INTJ</b>에게 필요한 이상적인 연인은?</h2>
<p data-ke-size="size16"><b>INTJ</b>들은 자신의 강점과 약점을 잘 알기 때문에, 결코 남들에게 지배받거나 좇아서 살지 않습니다. 그들에게 매력적인 이상적인 연인은 무엇일까요? 👫</p>
<h3 data-ke-size="size23">자신을 이해해 줄 수 있는 상대</h3>
<p data-ke-size="size16"><b>INTJ</b>들은 때로는 너무 논리적이고 감정을 잘 표현하지 않는 경향이 있습니다. 따라서, 자신을 이해해주고 그들과 대화할 줄 아는 상대가 필요합니다. 감정적인 지지를 받는다면 <b>INTJ</b>들은 마치 불안한 마음을 안고 사는 느낌에서 벗어날 수 있습니다. 🤝</p>
<h3 data-ke-size="size23">독립적이면서 협력적인 파트너</h3>
<p data-ke-size="size16"><b>INTJ</b>들은 독립적인 성향을 가지고 있지만, 그들도 사랑과 지지를 원합니다. 이들과 이상적인 연애를 하려면 상대가 독립적이면서도 협력적인 성향을 가져야 합니다. 함께 문제를 해결하고 목표를 달성하는 데에 협력할 줄 아는 파트너가 <b>INTJ</b>들의 마음을 사로잡을 수 있습니다. 🤝💪</p>
<hr data-ke-style="style1"/>
<h2 data-ke-size="size26"><b>INTJ</b>의 연애 팁: 과정보다는 결과에 집중하라</h2>
<p data-ke-size="size16"><b>INTJ</b>들은 지적 호기심과 목표지향적인 성격 때문에 종종 연애 과정에 집중하지 못하는 경우가 있습니다. 이들에게 도움이 될 수 있는 연애 팁은 무엇일까요? 🤔</p>
<h3 data-ke-size="size23">명확한 목표를 설정하라</h3>
<p data-ke-size="size16"><b>INTJ</b>들은 모든 것을 계획하고 실행하기를 좋아합니다. 따라서, 연애에도 명확한 목표를 설정하는 것이 도움이 됩니다. "어떤 사람과 어떤 관계를 원하는지?"를 명확히 하고, 그에 맞는 파트너를 찾는 데에 집중하면 <b>INTJ</b>들은 보다 만족스러운 연애를 할 수 있습니다. 🎯</p>
<h3 data-ke-size="size23">감정적인 결합을 위해 노력하라</h3>
<p data-ke-size="size16"><b>INTJ</b>들은 감정 표현에 서투른 경우가 많습니다. 하지만 감정적인 결합이 연애에서 중요하다는 것을 알아야 합니다. 감정을 더 표현하는 데에 노력하고, 파트너와 감정적으로 연결되는 시간을 갖는 것이 <b>INTJ</b>들에게 이상적인 연애를 만들어줄 수 있습니다. ❤️</p>
<h3 data-ke-size="size23">실패를 두려워하지 마라</h3>
<p data-ke-size="size16"><b>INTJ</b>들은 실패를 두려워하는 경향이 있습니다. 하지만 연애는 실패와 성공이 번갈아 오는 과정입니다. <b>INTJ</b>들에게 이상적인 연애를 찾으려면 실패를 두려워하지 않고, 그로 인해 얻는 교훈을 소중히 여길 필요가 있습니다. 🚀📈</p>
<hr data-ke-style="style1"/>
<h2 data-ke-size="size26"><b>INTJ</b>의 사랑에 빠지는 특별한 순간들 💘</h2>
<p data-ke-size="size16"><b>INTJ</b>들은 보통 사랑에 빠지는 데에 조금 더 많은 시간이 걸릴 수 있습니다. 하지만 그들이 사랑에 빠지는 순간은 정말 특별하고 감동적입니다. <b>INTJ</b>들이 사랑에 빠지는 특별한 순간들을 escribe 그리고 그들이 어떻게 반응하는지 확인해보세요! 😍</p>
<h3 data-ke-size="size23">깊은 우정에서 시작된 사랑</h3>
<p data-ke-size="size16"><b>INTJ</b>들은 연애를 시작하기 전에 상대를 깊이 알아가는 시간을 가지는 경향이 있습니다. 따라서, 그들이 사랑에 빠지는 순간은 보통 오랜 우정을 나누다가 갑자기 깨닫는 경우가 많습니다. 그들은 마치 보물💞</p>
<h3 data-ke-size="size23">감정적인 결합에 빠지다</h3>
<p data-ke-size="size16"><b>INTJ</b>들은 일반적으로 감정적인 결합이 어려울 수 있지만, 만약 그들이 감정적으로 연결된다면 그 순간은 정말 감동적입니다. 상대에게 쉽게 감정을 보이지 않던 <b>INTJ</b>들이 갑자기 감정의 바다에 빠져들며, 이전에는 느끼지 못했던 감정들을 경험하게 됩니다. 😢😊</p>
<h3 data-ke-size="size23">미래를 함께 상상하는 순간</h3>
<p data-ke-size="size16"><b>INTJ</b>들은 미래를 계획하고 꿈꾸는 데에 열정적입니다. 사랑에 빠지게 되면, 그들은 상대와 함께 미래를 상상하며 행복한 시간을 보냅니다. 두 사람이 함께 이루고 싶은 꿈들을 공유하며, 서로를 위한 계획을 만들어나가는 것이 <b>INTJ</b>들의 사랑에 빠지는 특별한 순간 중 하나입니다. 🌈🏰</p>
<hr data-ke-style="style1"/>
<h2 data-ke-size="size26">결론: <b>INTJ</b>의 이상적인 연애를 향해 🏹💕</h2>
<p data-ke-size="size16"><b>INTJ</b>들은 지적이면서도 독립적인 성향으로 독보적인 유형입니다. 그들의 이상적인 연애를 찾기 위해서는 자신을 잘 이해하고, 목표를 명확히 하는 것이 중요합니다. 감정적인 결합을 위해 노력하고, 실패를 두려워하지 않으며, 상대를 깊이 알아가는 과정에서 <b>INTJ</b>들은 보다 의미 있는 연애를 할 수 있습니다.</p>
<p data-ke-size="size16"><b>INTJ</b>들의 사랑에 빠지는 순간은 특별하고 감동적입니다. 오랜 우정을 나누다가 갑자기 사랑에 빠지는 순간부터 감정적인 결합에 빠지는 순간, 미래를 함께 상상하는 순간까지, <b>INTJ</b>들의 사랑은 놀라움으로 가득합니다.</p>
<p data-ke-size="size16">이제 여러분도 <b>INTJ</b>들에게 이상적인 연애를 위해 노력해보세요! 🌟🚀</p>
<p data-ke-size="size16"> </p>
<p data-ke-size="size16"><a href="https://giftedmbti.tistory.com/181" rel="noopener" target="_blank">[MBTI] ISFP에게 이상적인 연애 💕</a></p>
<figure contenteditable="false" data-ke-align="alignCenter" data-ke-type="opengraph" data-og-description="안녕하세요! MBTI 연애의 마법에 푹 빠져 살고 있는 여러분, 오늘은 특별한 MBTI 유형인 ISFP에게 이상적인 연애에 대해 이야기하려고 해요. ISFP는 정말 독특하고 아름다운 성격을 가진 사람들이에" data-og-host="giftedmbti.tistory.com" data-og-image="https://scrap.kakaocdn.net/dn/HqJds/hyTx06nI8y/GXwbnllCIGNLVLn15DKhxk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/eUCKN/hyTx0rKJw5/xz6PA7noiAwu7nqymo9MGk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500" data-og-source-url="https://giftedmbti.tistory.com/181" data-og-title="[MBTI] ISFP에게 이상적인 연애 💕" data-og-type="article" data-og-url="https://giftedmbti.tistory.com/181" id="og_1691197637106"><a data-source-url="https://giftedmbti.tistory.com/181" href="https://giftedmbti.tistory.com/181" rel="noopener" target="_blank">
<div class="og-image" style="background-image: url('https://scrap.kakaocdn.net/dn/HqJds/hyTx06nI8y/GXwbnllCIGNLVLn15DKhxk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/eUCKN/hyTx0rKJw5/xz6PA7noiAwu7nqymo9MGk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500');"> </div>
<div class="og-text">
<p class="og-title" data-ke-size="size16">[MBTI] ISFP에게 이상적인 연애 💕</p>
<p class="og-desc" data-ke-size="size16">안녕하세요! MBTI 연애의 마법에 푹 빠져 살고 있는 여러분, 오늘은 특별한 MBTI 유형인 ISFP에게 이상적인 연애에 대해 이야기하려고 해요. ISFP는 정말 독특하고 아름다운 성격을 가진 사람들이에</p>
<p class="og-host" data-ke-size="size16">giftedmbti.tistory.com</p>
</div>
</a></figure>
<p data-ke-size="size16"><a href="https://giftedmbti.tistory.com/178" rel="noopener" target="_blank">[MBTI] ESFJ에게 이상적인 연애 💖💌</a></p>
<figure contenteditable="false" data-ke-align="alignCenter" data-ke-type="opengraph" data-og-description="ESFJ, 당신은 늘 주변 사람들을 배려하고 챙기는 따뜻한 성격의 소유자입니다. 여러 사람들과 어울리는 것을 즐기며 사회적으로 활발하고 친근한 성향을 가지고 있죠. 이런 당신이 연애할 때는 " data-og-host="giftedmbti.tistory.com" data-og-image="https://scrap.kakaocdn.net/dn/O5TTN/hyTxZTUF9L/NXklBDIqKZUF10JoQjDYG0/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/czJzPJ/hyTxUSBkGM/y8e2dTL3pB0Myxd1SSFiK0/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500" data-og-source-url="https://giftedmbti.tistory.com/178" data-og-title="[MBTI] ESFJ에게 이상적인 연애 💖💌" data-og-type="article" data-og-url="https://giftedmbti.tistory.com/178" id="og_1691197642678"><a data-source-url="https://giftedmbti.tistory.com/178" href="https://giftedmbti.tistory.com/178" rel="noopener" target="_blank">
<div class="og-image" style="background-image: url('https://scrap.kakaocdn.net/dn/O5TTN/hyTxZTUF9L/NXklBDIqKZUF10JoQjDYG0/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/czJzPJ/hyTxUSBkGM/y8e2dTL3pB0Myxd1SSFiK0/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500');"> </div>
<div class="og-text">
<p class="og-title" data-ke-size="size16">[MBTI] ESFJ에게 이상적인 연애 💖💌</p>
<p class="og-desc" data-ke-size="size16">ESFJ, 당신은 늘 주변 사람들을 배려하고 챙기는 따뜻한 성격의 소유자입니다. 여러 사람들과 어울리는 것을 즐기며 사회적으로 활발하고 친근한 성향을 가지고 있죠. 이런 당신이 연애할 때는</p>
<p class="og-host" data-ke-size="size16">giftedmbti.tistory.com</p>
</div>
</a></figure>
<p data-ke-size="size16"><a href="https://giftedmbti.tistory.com/175" rel="noopener" target="_blank">[MBTI] ISFJ에게 이상적인 연애 💖💌</a></p>
<figure contenteditable="false" data-ke-align="alignCenter" data-ke-type="opengraph" data-og-description="안녕하세요, 여러분! 오늘은 MBTI 성격 유형 중 ISFJ에게 이상적인 연애에 대해 이야기해 볼게요. ISFJ는 따뜻하고 세심한 성향으로 유명한데요, 이런 특징들이 연애 생활에서 어떻게 발휘되는지 알" data-og-host="giftedmbti.tistory.com" data-og-image="https://scrap.kakaocdn.net/dn/E0Qo1/hyTxUykhGh/nCQWriD2O8AimJJ96ENE70/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/cVPplx/hyTxVcVT7T/PFT6x0YLKYWzGsolVvuuyk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500" data-og-source-url="https://giftedmbti.tistory.com/175" data-og-title="[MBTI] ISFJ에게 이상적인 연애 💖💌" data-og-type="article" data-og-url="https://giftedmbti.tistory.com/175" id="og_1691197649027"><a data-source-url="https://giftedmbti.tistory.com/175" href="https://giftedmbti.tistory.com/175" rel="noopener" target="_blank">
<div class="og-image" style="background-image: url('https://scrap.kakaocdn.net/dn/E0Qo1/hyTxUykhGh/nCQWriD2O8AimJJ96ENE70/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/cVPplx/hyTxVcVT7T/PFT6x0YLKYWzGsolVvuuyk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500');"> </div>
<div class="og-text">
<p class="og-title" data-ke-size="size16">[MBTI] ISFJ에게 이상적인 연애 💖💌</p>
<p class="og-desc" data-ke-size="size16">안녕하세요, 여러분! 오늘은 MBTI 성격 유형 중 ISFJ에게 이상적인 연애에 대해 이야기해 볼게요. ISFJ는 따뜻하고 세심한 성향으로 유명한데요, 이런 특징들이 연애 생활에서 어떻게 발휘되는지 알</p>
<p class="og-host" data-ke-size="size16">giftedmbti.tistory.com</p>
</div>
</a></figure>
<p data-ke-size="size16"> </p></div>
<!-- System - START -->
<div class="revenue_unit_wrap">
<div class="revenue_unit_item adfit">
<div class="revenue_unit_info">728x90</div>
<ins class="kakao_ad_area" data-ad-height="90px" data-ad-unit="DAN-oBV7q4jFitHkXDzp" data-ad-width="728px" style="display: none;"></ins>
<script async="async" src="//t1.daumcdn.net/kas/static/ba.min.js" type="text/javascript"></script>
</div>
</div>
<div class="revenue_unit_wrap">
<div class="revenue_unit_item adsense responsive">
<div class="revenue_unit_info">반응형</div>
<script async="async" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle" data-ad-client="ca-pub-7529335719399218" data-ad-format="auto" data-ad-host="ca-host-pub-9691043933427338" style="display: block;"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
</div>
<!-- System - END -->
<script async="" crossorigin="anonymous" onerror="changeAdsenseToAdfit()" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9527582522912841"></script>
<!-- inventory -->
<ins class="adsbygoogle" data-ad-adfit-unit="DAN-HCZEy0KQLPMGnGuC" data-ad-client="ca-pub-9527582522912841" data-ad-format="auto" data-ad-slot="4947159016" data-ad-type="inventory" data-full-width-responsive="true" style="margin:50px 0; display:block"></ins>
<script id="adsense_script">
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
<script>
    if(window.ObserveAdsenseUnfilledState !== undefined){ ObserveAdsenseUnfilledState(); }
</script>

"""

# HTML 문서 번역
#translated_html = translate_html(html_doc)

##print(translated_html)
