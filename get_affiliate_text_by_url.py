import tag_dict


def get_affiliate_text_by_info(title, tag_ids):
    

    mbti_tag_0 = next((mbti for mbti, info in tag_dict.items() if info["id"] == tag_ids[0]), None)
    mbti_tag_1 = next((mbti for mbti, info in tag_dict.items() if info["id"] == tag_ids[1]), None)

    affiliate_text = f'''<h2>Discover Your MBTI-Inspired Style with Boare Morts MBTI Store's Collection 🎒👜</h1>

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

    return affiliate_text

# Example usage:
# title = "ESTJ and ISTP Love Dynamics"
# tag_ids = [55, 47]
# result = get_affiliate_text_by_info(title, tag_ids)
# print(result)
