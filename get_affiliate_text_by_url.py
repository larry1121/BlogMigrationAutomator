from config import DEST_LANG
from get_ali_afil_image_html import get_ali_afil_image_html
from tag_dict import tag_dict 


def get_affiliate_text_by_info(title, tag_ids):
    

    mbti_tag_0 = next((mbti for mbti, info in tag_dict.items() if info["id"] == tag_ids[0]), None)
    mbti_tag_1 = next((mbti for mbti, info in tag_dict.items() if info["id"] == tag_ids[1]), None)

    affiliate_text_en = f'''<h2>Discover Your MBTI-Inspired Style with Boare Morts MBTI Store's Collection 🎒👜</h2>

    <p>Welcome, <em>fashion enthusiasts</em> and <em>MBTI aficionados</em>! Following our exploration of <strong>{title}</strong>, it's time to discover how your MBTI type can influence your fashion choices. At Boare Morts MBTI Store, you'll find trendy, chic, and uniquely designed bags that perfectly complement your personality. Let's dive into their exciting collection!</p>

    <h3>Why Boare Morts MBTI Store?</h3>
    <p>Just like the fascinating blend of <strong>{mbti_tag_0}</strong> and <strong>{mbti_tag_1}</strong> traits, Boare Morts MBTI Store offers a harmonious mix of style and personality in their women's backpacks, shoulder bags, and handbags. These bags are not just accessories; they're a celebration of your individuality, catered to those with a deep interest in MBTI and fashion. Plus, enjoy the best deals on AliExpress with ongoing discounts!</p>

    <h3>Rave Reviews:</h3>
    <p>Boare Morts MBTI Store boasts a remarkable <strong>97.1%</strong> positive feedback and over <strong>5675</strong> followers, a testament to their popularity among fashionistas and MBTI enthusiasts. Be part of this satisfied customer base and elevate your fashion game.</p>

    <h2>Featured Products: click to get!!</h2>
    
    {get_ali_afil_image_html()}


    <h2>Why You Should Grab These MBTI-inspired Bags:</h2>
    <p>Boare Morts MBTI Store products are a fusion of fashion-forward design and budget-friendly pricing. Just as <strong>{mbti_tag_0}</strong>s and <strong>{mbti_tag_1}</strong>s can form a unique and fulfilling relationship, these bags offer a unique way to express your personality through fashion.</p>

    <h2>Conclusion:</h2>
    <p>For those intrigued by MBTI and passionate about fashion, Boare Morts MBTI Store is your ultimate destination. Embrace the opportunity to redefine your fashion identity. Click, shop, and let your style speak volumes!</p>'''
    

    affiliate_text_ja = f'''<h2>Boare Morts MBTI StoreのコレクションでMBTIにインスパイアされたスタイルを発見しよう 🎒👜</h2>

<p>ようこそ、<em>ファッション愛好者</em>および<em>MBTI愛好者</em>の皆さん！私たちが<strong>{title}</strong>を探求した後、MBTIタイプがあなたのファッションの選択にどのように影響を与えるかを発見する時がきました。Boare Morts MBTI Storeでは、あなたの個性に完璧に合ったトレンディでシックなデザインのバッグを見つけることができます。さあ、彼らのエキサイティングなコレクションに飛び込みましょう！</p>

<h3>なぜBoare Morts MBTI Storeを選ぶのか？</h3>
<p>まるで魅力的な<strong>{mbti_tag_0}</strong>と<strong>{mbti_tag_1}</strong>の特性のブレンドのように、Boare Morts MBTI Storeは女性のバックパック、ショルダーバッグ、ハンドバッグでスタイルと個性のハーモニアスなミックスを提供しています。これらのバッグは単なるアクセサリーではありません。MBTIとファッションに深い興味を持つ個人の個性を祝うものです。さらに、AliExpressでの ongoing discounts で最高のお得感をお楽しみください！</p>

<h3>熱狂的なレビュー：</h3>
<p>Boare Morts MBTI Storeは驚異的な<strong>97.1%</strong>の好意的なフィードバックと<strong>5675</strong>以上のフォロワーを誇り、ファッショニスタやMBTI愛好者の間での人気の証です。この満足のいく顧客ベースの一員になり、あなたのファッションゲームを向上させましょう。</p>

<h2>注目の商品: クリックして入手!!</h2>

{get_ali_afil_image_html()}

<h2>これらのMBTIにインスパイアされたバッグを手に入れるべき理由：</h2>
<p>Boare Morts MBTI Storeの製品はファッションフォワードなデザインと予算に優しい価格の融合です。まるで<strong>{mbti_tag_0}</strong>や<strong>{mbti_tag_1}</strong>がユニークで充実した関係を形成できるように、これらのバッグはファッションを通じて個性を表現するユニークな方法を提供します。</p>

<h2>結論：</h2>
<p>MBTIに興味を持ち、ファッションに情熱を注いでいる方々にとって、Boare Morts MBTI Storeは究極の目的地です。ファッションアイデンティティを再定義するチャンスを掴んでください。クリックして、ショッピングし、あなたのスタイルが大いに語るのを許してください！</p>
'''


    return affiliate_text_en if DEST_LANG == 'en' else affiliate_text_ja


# Example usage:
# title = "ESTJ and ISTP Love Dynamics"
# tag_ids = [55, 47]
# result = get_affiliate_text_by_info(title, tag_ids)
# print(result)
