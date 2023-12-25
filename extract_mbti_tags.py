def extract_mbti_tags(html_contents):
    """
    Extracts MBTI tags from the given HTML contents and returns their tag IDs.

    Args:
        html_contents (str): The HTML content in which to search for MBTI types.

    Returns:
        list: A list of tag IDs corresponding to the MBTI types found in the content.
    """

    # Dictionary of MBTI types with their tag IDs
    mbti_dict = {
        "enfj": {"id": 57, "description": "Persuasive, Altruistic, Harmonious"},
        "enfp": {"id": 53, "description": "Enthusiastic, Creative, Social"},
        "entj": {"id": 58, "description": "Confident, Decisive, Leader"},
        "entp": {"id": 54, "description": "Inventive, Original, Argumentative"},
        "esfj": {"id": 56, "description": "Cooperative, Warm, Organized"},
        "esfp": {"id": 52, "description": "Lively, Fun-loving, Adaptable"},
        "estj": {"id": 55, "description": "Efficient, Practical, Leader"},
        "estp": {"id": 51, "description": "Energetic, Social, Realistic"},
        "infj": {"id": 45, "description": "Insightful, Idealistic, Creative"},
        "infp": {"id": 49, "description": "Idealistic, Emotional, Creative"},
        "intj": {"id": 46, "description": "Strategic, Independent, Innovative"},
        "intp": {"id": 50, "description": "Intellectual, Curious, Theoretical"},
        "isfj": {"id": 44, "description": "Caring, Loyal, Traditional"},
        "isfp": {"id": 48, "description": "Artistic, Peaceful, Adventurous"},
        "istj": {"id": 43, "description": "Responsible, Practical, Organized"},
        "istp": {"id": 47, "description": "Practical, Analytical, Curious"}
    }

    # Lowercase the HTML content for case-insensitive matching
    content_lower = html_contents.lower()

    # Find MBTI types in the content and collect their tag IDs
    tag_ids = [mbti_dict[mbti]["id"] for mbti in mbti_dict if mbti in content_lower]
    print(f"tag_ids : {tag_ids}")

    return tag_ids

if __name__ == "__main__":
    input_text = '''<div class="tt_article_useless_p_margin contents_style"><p data-ke-size="size16">💡 Introducing tips and interesting examples that will help INTJs dreaming of ideal love!I want to find a partner that goes with myself<b>INTJ</b>Special guide for them, start now!👀</p>
<h2 data-ke-size="size26"><b>INTJ</b>: Types that dominate unknown souls</h2>
<p data-ke-size="size16"><b>INTJ</b>Heard<b>MBTI</b>It is the rarest type of the most, with its unique thinking and high intelligence.I have my own world and constantly think and plan to achieve my goals.But when they start dating, they often don't know what to do.Now with us<b>INTJ</b>Find the ideal love for them!🚀</p>
<hr data-ke-style="style1"/>
<h2 data-ke-size="size26">Attractive challenger,<b>INTJ</b>What is your ideal lover?</h2>
<p data-ke-size="size16"><b>INTJ</b>Because they know their strengths and weaknesses well, they never live or follow by others.What are the ideal lovers that are attractive to them?👫</p>
<h3 data-ke-size="size23">A partner who can understand yourself</h3>
<p data-ke-size="size16"><b>INTJ</b>Sometimes it is too logical and tends to express feelings well.Therefore, we need a person who understands himself and knows how to talk to them.If you get emotional support<b>INTJ</b>You can get out of the feeling of living with anxiety.🤝</p>
<h3 data-ke-size="size23">Independent and cooperative partner</h3>
<p data-ke-size="size16"><b>INTJ</b>They have an independent tendency, but they also want love and support.To have an ideal relationship with them, the other person must have an independent and cooperative tendency.A partner who knows how to work together to solve the problem and achieve the goal<b>INTJ</b>You can capture your hearts.🤝</p>
<hr data-ke-style="style1"/>
<h2 data-ke-size="size26"><b>INTJ</b>Love Tips: Focus on the results rather than the process</h2>
<p data-ke-size="size16"><b>INTJ</b>They often do not focus on the love process because of their intellectual curiosity and goal -oriented personality.What is a love tip that can help them?🤔</p>
<h3 data-ke-size="size23">Set a clear goal</h3>
<p data-ke-size="size16"><b>INTJ</b>I like to plan and run everything.Therefore, it is helpful to set a clear goal for love.If you clarify "What kind of relationship do you want to have a relationship with?"<b>INTJ</b>You can have a more satisfactory relationship.🎯</p>
<h3 data-ke-size="size23">Try to make an emotional combination</h3>
<p data-ke-size="size16"><b>INTJ</b>It is often poor in expressing emotions.But you need to know that emotional bonds are important in love.Trying to express your emotions more and having a time to emotionally connect with your partner.<b>INTJ</b>You can create an ideal love for them.❤️</p>
<h3 data-ke-size="size23">Don't be afraid of failure</h3>
<p data-ke-size="size16"><b>INTJ</b>It tends to be afraid of failure.But love is a process of failure and success.<b>INTJ</b>To find the ideal love for them, it is necessary to cherish the lessons that are obtained.🚀📈</p>
<hr data-ke-style="style1"/>
<h2 data-ke-size="size26"><b>INTJ</b>Special moments in love of love 💘</h2>
<p data-ke-size="size16"><b>INTJ</b>It can take a little more time to fall in love.But the moment they fall in love are really special and touching.<b>INTJ</b>See the special moments in which they fall in love and see how they react!😍</p>
<h3 data-ke-size="size23">Love that started with deep friendship</h3>
<p data-ke-size="size16"><b>INTJ</b>There is a tendency to have time to get to know your opponent before you start dating.Therefore, the moment they fall in love, they usually share their friendship and suddenly realize it.They are like treasure 💞</p>
<h3 data-ke-size="size23">Emotional</h3>
<p data-ke-size="size16"><b>INTJ</b>It can be difficult for emotional combinations in general, but if they are emotionally connected, the moment is really touching.I didn't show any feelings to the other person<b>INTJ</b>Suddenly, they fall into the sea of emotions and experience the emotions they have never felt before.😢😊</p>
<h3 data-ke-size="size23">The moment you imagine the future together</h3>
<p data-ke-size="size16"><b>INTJ</b>I am passionate about planning and dreaming of the future.When they fall in love, they have a happy time with their opponents imagine the future.Share the dreams that the two people want to achieve together, and create a plan for each other<b>INTJ</b>It is one of the special moments that fall in love.🏰 🏰</p>
<hr data-ke-style="style1"/>
<h2 data-ke-size="size26">conclusion:<b>INTJ</b>Towards the ideal love of 🏹💕</h2>
<p data-ke-size="size16"><b>INTJ</b>It is intellectual and independent and is unique.In order to find their ideal love, it is important to understand themselves well and clarify the goals.In the process of trying to make an emotional bond, not afraid of failure, and knowing the opponent deeply<b>INTJ</b>They can have more meaningful love.</p>
<p data-ke-size="size16"><b>INTJ</b>The moment of falling in love is special and touching.From the moment you suddenly fall in love after sharing your friendship, to the moment you fall into an emotional combination, and the moment you imagine the future together,<b>INTJ</b>My love is full of surprise.</p>
<p data-ke-size="size16">Now everyone<b>INTJ</b>Try to try your ideal love!🚀</p>
<p data-ke-size="size16"> </p>
<p data-ke-size="size16"><a href="https://giftedmbti.tistory.com/181" rel="noopener" target="_blank">[MBTI] ISFP ideal love 💕</a></p>
<figure contenteditable="false" data-ke-align="alignCenter" data-ke-type="opengraph" data-og-description="안녕하세요! MBTI 연애의 마법에 푹 빠져 살고 있는 여러분, 오늘은 특별한 MBTI 유형인 ISFP에게 이상적인 연애에 대해 이야기하려고 해요. ISFP는 정말 독특하고 아름다운 성격을 가진 사람들이에" data-og-host="giftedmbti.tistory.com" data-og-image="https://scrap.kakaocdn.net/dn/HqJds/hyTx06nI8y/GXwbnllCIGNLVLn15DKhxk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/eUCKN/hyTx0rKJw5/xz6PA7noiAwu7nqymo9MGk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500" data-og-source-url="https://giftedmbti.tistory.com/181" data-og-title="[MBTI] ISFP에게 이상적인 연애 💕" data-og-type="article" data-og-url="https://giftedmbti.tistory.com/181" id="og_1691197637106"><a data-source-url="https://giftedmbti.tistory.com/181" href="https://giftedmbti.tistory.com/181" rel="noopener" target="_blank">
<div class="og-image" style="background-image: url('https://scrap.kakaocdn.net/dn/HqJds/hyTx06nI8y/GXwbnllCIGNLVLn15DKhxk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/eUCKN/hyTx0rKJw5/xz6PA7noiAwu7nqymo9MGk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500');"> </div>
<div class="og-text">
<p class="og-title" data-ke-size="size16">[MBTI] ISFP ideal love 💕</p>
<p class="og-desc" data-ke-size="size16">hello!Everyone who lives in the magic of MBTI love, today I'm going to talk about ISFP, a special MBTI type.ISFP is a very unique and beautiful person</p>
<p class="og-host" data-ke-size="size16">giftedmbti.tistory.com</p>
</div>
</a></figure>
<p data-ke-size="size16"><a href="https://giftedmbti.tistory.com/178" rel="noopener" target="_blank">[MBTI] Ideal for ESFJ 💖</a></p>
<figure contenteditable="false" data-ke-align="alignCenter" data-ke-type="opengraph" data-og-description="ESFJ, 당신은 늘 주변 사람들을 배려하고 챙기는 따뜻한 성격의 소유자입니다. 여러 사람들과 어울리는 것을 즐기며 사회적으로 활발하고 친근한 성향을 가지고 있죠. 이런 당신이 연애할 때는 " data-og-host="giftedmbti.tistory.com" data-og-image="https://scrap.kakaocdn.net/dn/O5TTN/hyTxZTUF9L/NXklBDIqKZUF10JoQjDYG0/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/czJzPJ/hyTxUSBkGM/y8e2dTL3pB0Myxd1SSFiK0/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500" data-og-source-url="https://giftedmbti.tistory.com/178" data-og-title="[MBTI] ESFJ에게 이상적인 연애 💖💌" data-og-type="article" data-og-url="https://giftedmbti.tistory.com/178" id="og_1691197642678"><a data-source-url="https://giftedmbti.tistory.com/178" href="https://giftedmbti.tistory.com/178" rel="noopener" target="_blank">
<div class="og-image" style="background-image: url('https://scrap.kakaocdn.net/dn/O5TTN/hyTxZTUF9L/NXklBDIqKZUF10JoQjDYG0/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/czJzPJ/hyTxUSBkGM/y8e2dTL3pB0Myxd1SSFiK0/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500');"> </div>
<div class="og-text">
<p class="og-title" data-ke-size="size16">[MBTI] Ideal for ESFJ 💖</p>
<p class="og-desc" data-ke-size="size16">ESFJ, you are the owner of a warm personality who always cares about and takes care of the people around you.He enjoys hanging out with many people and has a social and friendly tendency.When you are dating like this</p>
<p class="og-host" data-ke-size="size16">giftedmbti.tistory.com</p>
</div>
</a></figure>
<p data-ke-size="size16"><a href="https://giftedmbti.tistory.com/175" rel="noopener" target="_blank">[MBTI] ISFJ ideal love 💖</a></p>
<figure contenteditable="false" data-ke-align="alignCenter" data-ke-type="opengraph" data-og-description="안녕하세요, 여러분! 오늘은 MBTI 성격 유형 중 ISFJ에게 이상적인 연애에 대해 이야기해 볼게요. ISFJ는 따뜻하고 세심한 성향으로 유명한데요, 이런 특징들이 연애 생활에서 어떻게 발휘되는지 알" data-og-host="giftedmbti.tistory.com" data-og-image="https://scrap.kakaocdn.net/dn/E0Qo1/hyTxUykhGh/nCQWriD2O8AimJJ96ENE70/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/cVPplx/hyTxVcVT7T/PFT6x0YLKYWzGsolVvuuyk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500" data-og-source-url="https://giftedmbti.tistory.com/175" data-og-title="[MBTI] ISFJ에게 이상적인 연애 💖💌" data-og-type="article" data-og-url="https://giftedmbti.tistory.com/175" id="og_1691197649027"><a data-source-url="https://giftedmbti.tistory.com/175" href="https://giftedmbti.tistory.com/175" rel="noopener" target="_blank">
<div class="og-image" style="background-image: url('https://scrap.kakaocdn.net/dn/E0Qo1/hyTxUykhGh/nCQWriD2O8AimJJ96ENE70/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500,https://scrap.kakaocdn.net/dn/cVPplx/hyTxVcVT7T/PFT6x0YLKYWzGsolVvuuyk/img.jpg?width=500&amp;height=500&amp;face=0_0_500_500');"> </div>
<div class="og-text">
<p class="og-title" data-ke-size="size16">[MBTI] ISFJ ideal love 💖</p>
<p class="og-desc" data-ke-size="size16">hello everyone!Today, let's talk to ISFJ about the ideal love of MBTI personality.ISFJ is famous for its warm and meticulous tendency.</p>
<p class="og-host" data-ke-size="size16">giftedmbti.tistory.com</p>
</div>
</a></figure>
<p data-ke-size="size16"> </p></div>
System - START
<div class="revenue_unit_wrap">
<div class="revenue_unit_item adfit">
<div class="revenue_unit_info">728x90</div>
<ins class="kakao_ad_area" data-ad-height="90px" data-ad-unit="DAN-oBV7q4jFitHkXDzp" data-ad-width="728px" style="display: none;"></ins>
<script async="async" src="//t1.daumcdn.net/kas/static/ba.min.js" type="text/javascript"></script>
</div>
</div>
<div class="revenue_unit_wrap">
<div class="revenue_unit_item adsense responsive">
<div class="revenue_unit_info">Reactive</div>
<script async="async" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle" data-ad-client="ca-pub-7529335719399218" data-ad-format="auto" data-ad-host="ca-host-pub-9691043933427338" style="display: block;"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
</div>
System - END
<script async="" crossorigin="anonymous" onerror="changeAdsenseToAdfit()" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9527582522912841"></script>
inventory
<ins class="adsbygoogle" data-ad-adfit-unit="DAN-HCZEy0KQLPMGnGuC" data-ad-client="ca-pub-9527582522912841" data-ad-format="auto" data-ad-slot="4947159016" data-ad-type="inventory" data-full-width-responsive="true" style="margin:50px 0; display:block"></ins>
<script id="adsense_script">(adsbygoogle = window.adsbygoogle || []).push({});</script>
<script>if(window.ObserveAdsenseUnfilledState !== undefined){ ObserveAdsenseUnfilledState(); }</script>'''

    
    
    extract_mbti_tags(input_text)
    