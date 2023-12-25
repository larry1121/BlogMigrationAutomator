from config import DEST_LANG
from tag_dict import tag_dict 


def get_affiliate_text_by_info(title, tag_ids):
    

    mbti_tag_0 = next((mbti for mbti, info in tag_dict.items() if info["id"] == tag_ids[0]), None)
    mbti_tag_1 = next((mbti for mbti, info in tag_dict.items() if info["id"] == tag_ids[1]), None)

    affiliate_text_en = f'''<h2>Discover Your MBTI-Inspired Style with Boare Morts MBTI Store's Collection 🎒👜</h1>

    <p>Welcome, <em>fashion enthusiasts</em> and <em>MBTI aficionados</em>! Following our exploration of <strong>{title}</strong>, it's time to discover how your MBTI type can influence your fashion choices. At Boare Morts MBTI Store, you'll find trendy, chic, and uniquely designed bags that perfectly complement your personality. Let's dive into their exciting collection!</p>

    <h2>Why Boare Morts MBTI Store?</h2>
    <p>Just like the fascinating blend of <strong>{mbti_tag_0}</strong> and <strong>{mbti_tag_1}</strong> traits, Boare Morts MBTI Store offers a harmonious mix of style and personality in their women's backpacks, shoulder bags, and handbags. These bags are not just accessories; they're a celebration of your individuality, catered to those with a deep interest in MBTI and fashion. Plus, enjoy the best deals on AliExpress with ongoing discounts!</p>

    <h2>Rave Reviews:</h2>
    <p>Boare Morts MBTI Store boasts a remarkable <strong>97.1%</strong> positive feedback and over <strong>5675</strong> followers, a testament to their popularity among fashionistas and MBTI enthusiasts. Be part of this satisfied customer base and elevate your fashion game.</p>

    <h2>Featured Products:</h2>
    <ul>
        <li><strong>MBTI Silver Y2k Tote Bags:</strong> Aesthetic luxury for the pragmatic <strong>{mbti_tag_0}</strong> or the adventurous <strong>{mbti_tag_1}</strong>.</li>
        <li><strong>MBTI Vintage Y2k Messenger Bag:</strong> Perfect for students or those who cherish nostalgia and practicality.</li>
        <li><strong>MBTI Designer Pleated Women's Shoulder Bag:</strong> A blend of Korean style and simplicity, ideal for any occasion.</li>
        <li><strong>MBTI Black Y2k Women Shoulder Bag:</strong> Unleash your bold side, resonating with the punk and goth vibes.</li>
    </ul>

    <h2>Why You Should Grab These MBTI-inspired Bags:</h2>
    <p>Boare Morts MBTI Store products are a fusion of fashion-forward design and budget-friendly pricing. Just as <strong>{mbti_tag_0}</strong>s and <strong>{mbti_tag_1}</strong>s can form a unique and fulfilling relationship, these bags offer a unique way to express your personality through fashion.</p>

    <h2>Conclusion:</h2>
    <p>For those intrigued by MBTI and passionate about fashion, Boare Morts MBTI Store is your ultimate destination. Embrace the opportunity to redefine your fashion identity. Click, shop, and let your style speak volumes!</p>'''
    

    affiliate_text_ja = f'''<h2>ボアーモーツMBTIストアのコレクションでMBTIにインスパイアされたスタイルを発見 🎒👜</h1>

    <p>ようこそ、<em>ファッション愛好者</em> と <em>MBTI愛好者</em> の皆さん！弊社が<strong>{title}</strong>を探求した後、MBTIタイプがファッションの選択にどのように影響するかを発見する時がきました。ボアーモーツMBTIストアでは、個性に完璧に合ったトレンディでシック、ユニークなデザインのバッグが見つかります。さあ、彼らのエキサイティングなコレクションに飛び込んでみましょう！</p>

    <h2>ボアーモーツMBTIストアの魅力は？</h2>
    <p><strong>{mbti_tag_0}</strong> と <strong>{mbti_tag_1}</strong> の特性が絶妙に調和したように、ボアーモーツMBTIストアは、女性向けのバックパック、ショルダーバッグ、ハンドバッグにスタイルと個性を見事に融合させています。これらのバッグは単なるアクセサリーではなく、MBTIとファッションに深い興味を抱く人々への賛美の意であり、さらにAliExpressでのお得な取引を楽しむことができます！</p>

    <h2>絶賛のレビュー：</h2>
    <p>ボアーモーツMBTIストアは驚異的な<strong>97.1%</strong>の好意的なフィードバックと<strong>5675</strong>を超えるフォロワーを誇り、ファッショニスタとMBTI愛好者の間での人気の証です。この満足いく顧客層に参加し、あなたのファッションゲームを引き上げましょう。</p>

    <h2>注目の商品：</h2>
    <ul>
        <li><strong>MBTI Silver Y2k トートバッグ：</strong> 実用的な<strong>{mbti_tag_0}</strong> または冒険心旺盛な<strong>{mbti_tag_1}</strong> にぴったり。</li>
        <li><strong>MBTI Vintage Y2k メッセンジャーバッグ：</strong> 学生やノスタルジアと実用性を大切にする方に最適。</li>
        <li><strong>MBTI デザイナープリーテッドウィメンズショルダーバッグ：</strong> 韓国スタイルとシンプルさの融合で、どんな場面にも理想的。</li>
        <li><strong>MBTI Black Y2k ウィメンズショルダーバッグ：</strong> 大胆な一面を引き出し、パンクとゴスの雰囲気に共感。</li>
    </ul>

    <h2>これらのMBTIにインスパイアされたバッグを手に入れる理由：</h2>
    <p>ボアーモーツMBTIストアの製品は、ファッション感覚と予算に優れたデザインの融合です。ちょうど<strong>{mbti_tag_0}</strong> と <strong>{mbti_tag_1}</strong> がユニークで充実した関係を築けるように、これらのバッグはファッションを通じて個性を表現するユニークな方法を提供します。</p>

    <h2>結論：</h2>
    <p>MBTIに興味を抱き、ファッションに情熱を注ぐ方々にとって、ボアーモーツMBTIストアは究極の目的地です。ファッションアイデンティティを再定義するチャンスを受け入れましょう。クリックして、ショッピングを楽しんで、あなたのスタイルで大いに語りかけましょう！</p>'''


    return affiliate_text_en if DEST_LANG == 'en' else affiliate_text_ja


# Example usage:
# title = "ESTJ and ISTP Love Dynamics"
# tag_ids = [55, 47]
# result = get_affiliate_text_by_info(title, tag_ids)
# print(result)
