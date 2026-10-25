"""Build Dragon Cove's Traditional Chinese home, menu index and private room pages."""
from pathlib import Path
import re

from build_chinese_pages import CATEGORIES, head, header, footer
from build_menu_pages import DELIVERY, MENU, esc, PUBLIC

ROOT = Path(__file__).parent
DIST = ROOT / 'dist'
OUT = DIST / 'zh'
GIFT = 'https://giftcards.nowbookit.com/cards?accountid=c841d62d-257b-40e7-8a6b-1fed4b87f86e&amp;venueid=14650&amp;theme=dark&amp;accent=157,157,157'
PRIVATE = 'https://www.opentable.com.au/private-dining/profile/dragon-cove-chinese-cuisine'


def home():
    english=(DIST/'index.html').read_text()
    widget=re.search(r'<div class="opentable-widget".*?</div>',english,re.S)
    assert widget
    widget=widget.group().replace('Book a table at Dragon Cove','於龍軒訂座').replace('View availability on OpenTable','在 OpenTable 查看空位')
    return (head('首頁', '龍軒位於黃金海岸 Sanctuary Cove，供應飲茶、鮮活海鮮及經典粵菜。瀏覽菜單、私人宴會、禮品卡與訂座資訊。', '/zh/', 1) + header('') + f'''<main id="main">
<section class="refurbishment-note" aria-labelledby="refurbishment-title"><div class="refurbishment-inner"><div><p class="refurbishment-kicker">餐廳裝修消息</p><h2 id="refurbishment-title">換上新貌，<br><em>期待再聚。</em></h2></div><p>龍軒將於 <strong><time datetime="2026-10-26">10月26日</time>至<time datetime="2026-11-15">11月15日</time></strong> 暫停營業，進行裝修。感謝您的支持，期待於 <strong><time datetime="2026-11-16">11月16日</time></strong> 歡迎您回來。</p><div class="refurbishment-alternatives"><p>裝修期間，歡迎到我們的姊妹餐廳用餐。</p><div><a href="https://www.jaderoomchinese.com.au/" target="_blank" rel="noopener noreferrer">Jade Room <span>Robina ↗</span></a><a href="https://jasmineroom.com.au/" target="_blank" rel="noopener noreferrer">Jasmine Room <span>Southport ↗</span></a></div></div></div></section>
<section class="opening" aria-labelledby="brand-name"><h1 id="brand-name">龍軒</h1><div class="brand-details"><p>粵式餐飲</p><p>Sanctuary Cove · 黃金海岸</p></div>
<figure class="hero"><img src="../assets/interior.jpg" alt="龍軒餐廳室內設計，設有紅色座椅與綠色大理石餐桌" fetchpriority="high" width="1600" height="1000"></figure>
<div class="introduction" id="welcome"><h2>好時光，<br><em>慢慢享。</em></h2><div><p>手製點心、鮮活海鮮與經典粵菜。<br>與親友共享一席滋味。</p><a class="button button-solid" href="menu.html">瀏覽菜單 <span aria-hidden="true">⟶</span></a></div></div></section>
<section class="story" id="story" aria-labelledby="story-title"><figure><img src="../assets/banquet.jpg" alt="一桌適合共享的粵式宴席菜餚" width="1792" height="2390" loading="lazy"><figcaption>菜餚圖片僅供參考。</figcaption></figure><div class="story-copy"><p class="eyebrow">相聚的滋味</p><h2 id="story-title">好菜餚。<br>好時光。</h2><p>從午間飲茶到晚間聚餐，龍軒在 Sanctuary Cove 的水岸旁，為您呈獻適合共享的粵式滋味。</p><a class="text-link" href="#visit">到訪龍軒 <span aria-hidden="true">⟶</span></a></div></section>
<section class="gift section-space" id="gift-card" aria-labelledby="gift-title"><div><p class="eyebrow">一份心意</p><h2 id="gift-title">送上一席<br><em>相聚時光。</em></h2></div><div class="gift-copy"><p>無論是悠閒午餐、溫馨晚宴，還是讓親友自由選擇喜愛菜式，龍軒禮品卡都能為相聚添上心意。</p><a class="button button-solid" href="{GIFT}" target="_blank" rel="noopener">購買禮品卡 <span aria-hidden="true">⟶</span></a></div></section>
<section class="visit section-space" id="visit" aria-labelledby="visit-title"><div class="visit-booking"><p class="eyebrow">Sanctuary Cove · 黃金海岸</p><h2 id="visit-title">期待與您<br><em>相聚。</em></h2>{widget}</div><div class="visit-details"><div><h3>餐廳地址</h3><address>Shop 03D, Sanctuary Cove Marine Village<br>Masthead Way, Sanctuary Cove<br>Queensland 4212</address><a class="text-link" href="https://www.google.com/maps/search/?api=1&amp;query=Dragon%20Cove%20Sanctuary%20Cove" target="_blank" rel="noopener">查看路線 <span aria-hidden="true">↗</span></a><p class="small">Marine Village 停車場提供免費泊車。</p></div><div><h3>營業時間</h3><p>星期三至星期一<br>午市 · 中午12時至下午3時<br>晚市 · 下午5時至晚上9時<br>星期二休息</p><p class="small">廚房於下午2時30分及晚上8時30分停止接單。</p></div><div class="contact"><h3>聯絡我們</h3><a href="tel:+61755779918">(07) 5577 9918</a><a href="mailto:info@dragoncove.com.au">info@dragoncove.com.au</a><h3 class="visit-order-title">網上點餐</h3><a href="{esc(DELIVERY)}" target="_blank" rel="noopener noreferrer">在 Uber Eats 訂購 ↗</a></div></div></section>
</main>''' + footer())


def menu_index():
    cards=[]
    copy={
      'yum-cha':('手製點心、蒸餃、包點與小食，適合一桌共享。','查看完整飲茶菜單'),
      'a-la-carte':('經典粵菜、鮮活海鮮及各式美味，從午餐到晚餐皆宜。','查看完整單點菜單'),
      'banquets':('以豐盛宴席慶祝特別時刻，與親友盡情相聚。','查看宴會套餐'),
      'takeaway':('把龍軒的味道帶回家。可網上預訂自取，或透過 Uber Eats 送餐。','查看完整外賣菜單'),
    }
    for key,data in MENU.items():
        name,_,_,_,_,alt=CATEGORIES[key]
        desc,label=copy[key]
        delivery=''
        cards.append(f'<article><img src="../assets/{esc(data["image"])}" alt="{esc(alt)}" width="1500" height="2250" loading="lazy"><div class="offering-copy"><h3>{esc(name)}</h3><p>{esc(desc)}</p><a class="text-link" href="menu/{key}.html">{esc(label)} <span aria-hidden="true">⟶</span></a>{delivery}</div></article>')
    return (head('菜單', '瀏覽龍軒的飲茶、單點菜式、宴會套餐及外賣菜單，於 Sanctuary Cove 共享粵式美味。', '/zh/menu', 1) + header('menu') + f'''<main id="main"><section class="subpage-head menu-head"><p class="eyebrow">龍軒 · Sanctuary Cove</p><h1>龍軒<em>菜單。</em></h1><div class="subpage-intro"><p>從一席悠閒飲茶，到滿桌喜愛的粵式菜餚。看看今天想與誰分享。</p><a class="text-link" href="index.html#visit">立即訂座 <span aria-hidden="true">⟶</span></a></div></section>
<section class="menu-feature" aria-label="龍軒飲茶"><figure><img src="../assets/dumplings.jpg" alt="竹籠中的鮮蝦蒸餃" width="900" height="1200" fetchpriority="high"><figcaption>菜餚圖片僅供參考。</figcaption></figure><div><p class="eyebrow">用心分享</p><h2>一籠點心，<br><em>一桌歡聚。</em></h2><p>從一杯熱茶開始，慢慢品嚐熟悉的滋味。</p></div></section>
<section class="menu-offerings section-space" aria-labelledby="menu-offerings-title"><div class="section-intro"><p class="eyebrow">細選滋味</p><h2 id="menu-offerings-title">尋找您的<br><em>心頭好。</em></h2></div><div class="offering-list">{''.join(cards)}<div class="menu-delivery"><p>想享用外送？可透過 Uber Eats 訂購龍軒菜式。</p><a class="button button-outline" href="{esc(DELIVERY)}" target="_blank" rel="noopener noreferrer">在 Uber Eats 訂購 ↗</a></div></div></section>
<section class="page-cta"><p class="eyebrow">歡迎光臨</p><h2>相聚，<em>就從這裡開始。</em></h2><a class="button button-outline-light" href="index.html#visit">立即訂座 <span aria-hidden="true">⟶</span></a></section></main>''' + footer())


def private_room():
    return (head('私人宴會', '在龍軒 Sanctuary Cove 的私人用餐空間，舉辦家庭聚會、慶祝晚宴及團體宴席。歡迎查詢。', '/zh/private-room', 1) + header('private-room') + f'''<main id="main"><section class="subpage-head private-head"><p class="eyebrow">私人宴會 · Sanctuary Cove</p><h1>私人<em>宴會。</em></h1><div class="subpage-intro"><p>值得紀念的相聚，值得一個專屬空間。在龍軒，讓親友自在共享美食與時光。</p><a class="text-link" href="{PRIVATE}" target="_blank" rel="noopener">查詢私人宴會 <span aria-hidden="true">↗</span></a></div></section>
<figure class="private-hero"><img src="../assets/private-room-fitout.jpg" alt="龍軒私人宴會房設計，設有圓形綠色大理石餐桌及柔和燈光" width="2752" height="1536" fetchpriority="high"><figcaption>私人宴會房設計效果圖。</figcaption></figure>
<section class="private-intro section-space" aria-labelledby="private-intro-title"><div><p class="eyebrow">專屬聚會</p><h2 id="private-intro-title">珍貴時刻，<br><em>自在相聚。</em></h2></div><div><p>家庭慶祝、紀念晚宴，或與重要的人圍桌細談。我們的私人宴會房讓您擁有專屬空間，共享為相聚而設的粵菜。</p><a class="text-link" href="menu.html">瀏覽菜單 <span aria-hidden="true">⟶</span></a></div></section>
<section class="private-enquiry section-space"><div><p class="eyebrow">籌備聚會</p><h2>告訴我們<br><em>您的安排。</em></h2></div><div><p>請告知理想日期、參加人數及聚會場合。我們樂意與您討論私人宴會空間及套餐選擇。</p><div class="enquiry-actions"><a class="button button-outline-light" href="{PRIVATE}" target="_blank" rel="noopener">在 OpenTable 查詢 <span aria-hidden="true">↗</span></a><a class="phone-link" href="mailto:info@dragoncove.com.au?subject=Private%20Dining%20Enquiry">電郵聯絡</a><a class="phone-link" href="tel:+61755779918">致電 (07) 5577 9918</a></div></div></section></main>''' + footer())


def main():
    OUT.mkdir(exist_ok=True)
    for name,html in [('index.html',home()),('menu.html',menu_index()),('private-room.html',private_room())]:
        (OUT/name).write_text(html,encoding='utf-8')
    paths=['/','/menu','/private-room']+[f'/menu/{key}' for key in MENU]
    paths+=['/zh/','/zh/menu','/zh/private-room']+[f'/zh/menu/{key}' for key in MENU]
    lines=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    lines += [f'  <url><loc>{PUBLIC}{path}</loc></url>' for path in paths]
    lines.append('</urlset>')
    (DIST/'sitemap.xml').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (DIST/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {PUBLIC}/sitemap.xml\n',encoding='utf-8')
    print('Built Traditional Chinese home, menu overview and private-room pages')

if __name__=='__main__': main()
