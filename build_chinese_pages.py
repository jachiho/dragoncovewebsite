"""Build Traditional Chinese counterparts for every Dragon Cove page."""
from __future__ import annotations

import json
import re
from pathlib import Path

from build_menu_pages import MENU, DELIVERY, ORDER, PUBLIC, esc, slug
from chinese_menu_translations import NAME_ZH, DETAIL_ZH

ROOT = Path(__file__).parent
OUT = ROOT / 'dist' / 'zh'

CATEGORIES = {
    'yum-cha': ('飲茶', '蒸點、煎炸點心、包點與地道小食，午市供應。', '細看龍軒飲茶菜單，包括蝦餃、燒賣、小籠包、包點及各式點心。', '蒸點與小食，與親友一起慢慢分享。', '飲茶只於午市供應。價格均為澳元。', '竹籠蒸點'),
    'a-la-carte': ('單點菜式', '從鮮活海鮮到經典粵菜，選幾道喜愛的菜式一起分享。', '瀏覽龍軒單點菜單：鮮活海鮮、北京烤鴨、煲仔菜、肉類、蔬菜及麵飯。', '細選經典粵菜與時令鮮味。', '價格均為澳元。鮮活海鮮按市價計算。菜式可能含有堅果或貝類；如有飲食需要，請告知職員。公眾假期加收15%。', '粵式菜餚配時蔬'),
    'banquets': ('宴會套餐', '為歡聚而設的豐盛套餐，適合慶祝與團體聚餐。', '瀏覽龍軒宴會套餐，包括菜式與每位價格。', '與親友共享一席好味。', '每款套餐最少四位起。價格以每位計算，均為澳元。', '親友圍桌共享宴席'),
    'takeaway': ('外賣', '把龍軒的味道帶回家。瀏覽菜式，選擇自取或 Uber Eats 送餐。', '瀏覽龍軒完整外賣菜單，包括前菜、海鮮、雞肉、牛肉、蔬菜及麵飯。', '喜愛的粵菜，帶回家慢慢享用。', '價格均為澳元，Uber Eats 價格及供應情況可能不同。公眾假期加收15%。菜式可能含有堅果或堅果微量成分；如有過敏或飲食需要，請向職員查詢。', '外賣菜式'),
}
SECTIONS = {
    'Steamed dumplings':'蒸餃', 'Crispy dumplings':'香脆餃點', 'Steamed bao':'蒸包', 'Pan & deep fried':'煎炸點心', 'Small dishes':'特色小食',
    'Specials':'招牌推介', 'Soup':'湯羹', 'Appetizers':'前菜', 'Dumplings':'餃子點心', 'Peking duck':'北京烤鴨',
    'Live seafood · market price':'鮮活海鮮 · 市價', 'Claypot & teppan':'煲仔與鐵板', 'Seafood':'海鮮', 'Poultry':'雞鴨', 'Meat':'肉類',
    'Chinese delicacies':'中式珍饈', 'Vegetables & tofu':'蔬菜與豆腐', 'Rice & noodles':'飯與麵',
    'Banquet A · $60 per person':'套餐 A · 每位 $60', 'Banquet B · $90 per person':'套餐 B · 每位 $90',
    'Entrees':'前菜', 'Omelette':'炒蛋', 'Beef, pork & lamb':'牛肉、豬肉與羊肉',
}


def head(title: str, description: str, slug_path: str, depth: int, *, menu_schema=None) -> str:
    css = '../' * depth + 'styles.css'
    url = PUBLIC + slug_path
    en = PUBLIC + (slug_path.removeprefix('/zh') or '/')
    schema = ''
    if menu_schema:
        schema = '<script type="application/ld+json">' + json.dumps(menu_schema, ensure_ascii=False).replace('</', '<\\/') + '</script>'
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | 龍軒 Dragon Cove · Sanctuary Cove</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{esc(url)}">
<link rel="alternate" hreflang="zh-Hant" href="{esc(url)}">
<link rel="alternate" hreflang="en-AU" href="{esc(en)}">
<meta name="theme-color" content="#761714">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=DM+Sans:wght@400;500&family=Noto+Serif+TC:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
{schema}
</head>
<body>'''


def header(page: str, detail=False) -> str:
    z = '../' if detail else ''
    e = '../../' if detail else '../'
    other = e + page + '.html' if page else e + 'index.html'
    current = 'menu' if page.startswith('menu/') else page
    links = [
        ('index.html', '首頁', ''), ('menu.html', '菜單', 'menu'), ('private-room.html', '私人宴會', 'private-room'),
        ('index.html#gift-card', '禮品卡', 'gift-card'), ('index.html#visit', '到訪資訊', 'visit'),
    ]
    nav = ''.join(f'<a href="{z}{href}"{(" aria-current=" + chr(34) + "page" + chr(34)) if current == key else ""}>{label}</a>' for href,label,key in links)
    return f'''<a class="skip" href="#main">跳至內容</a>
<header class="header">
<a class="seal" href="{z}index.html" aria-label="龍軒首頁">龍<br>軒</a>
<nav class="site-nav" aria-label="主選單">{nav}</nav>
<div class="header-actions"><a class="delivery-link" href="{esc(DELIVERY)}" target="_blank" rel="noopener noreferrer" aria-label="透過 Uber Eats 訂購龍軒外賣">Uber Eats <span aria-hidden="true">↗</span></a><a class="lang-switch" href="{other}" lang="en-AU" hreflang="en-AU" aria-label="View this page in English">English</a><a class="button button-outline" href="{esc(ORDER)}" target="_blank" rel="noopener">網上外賣</a><a class="button button-solid" href="{z}index.html#visit">立即訂座</a></div>
<details class="mobile-nav"><summary aria-label="開啟選單">選單 <span aria-hidden="true">☰</span></summary><nav aria-label="手機選單">{nav}<a href="{esc(DELIVERY)}" target="_blank" rel="noopener noreferrer">Uber Eats 送餐 ↗</a><a class="lang-switch" href="{other}" lang="en-AU" hreflang="en-AU">English</a><a class="mobile-primary" href="{esc(ORDER)}" target="_blank" rel="noopener">網上外賣 ↗</a><a class="mobile-primary mobile-book" href="{z}index.html#visit">立即訂座</a></nav></details>
</header>'''


def footer(detail=False) -> str:
    z = '../' if detail else ''
    return f'''<footer><a class="footer-brand" href="{z}index.html">龍軒 <span lang="en">Dragon Cove</span></a><p>粵式餐飲 · Sanctuary Cove</p><a href="#main">返回頁首 ↑</a></footer>\n</body></html>'''


def price(value: str) -> str:
    if not value: return ''
    if value == 'Market price': return '市價'
    if value.startswith('From '): return '$' + value[5:] + '起'
    return '$' + value


def menu_page(menu_id: str, data: dict) -> str:
    name, intro, description, _, note, alt = CATEGORIES[menu_id]
    sections=[]; section_links=[]; structured=[]
    for english, dishes in data['sections']:
        chinese = SECTIONS[english]
        ident = slug(english)
        section_links.append(f'<a href="#{ident}">{esc(chinese)}</a>')
        rows=[]; nodes=[]
        for dish in dishes:
            zh_name = NAME_ZH[dish['name']]
            detail = '<p>' + esc(DETAIL_ZH[dish['detail']]) + '</p>' if dish['detail'] else ''
            amount = '<span class="dish-price">' + esc(price(dish['price'])) + '</span>' if dish['price'] else ''
            rows.append(f'<li class="dish"><div><h3>{esc(zh_name)}</h3>{detail}</div>{amount}</li>')
            node={'@type':'MenuItem','name':zh_name}
            if dish['detail']: node['description']=DETAIL_ZH[dish['detail']]
            if dish['price'] and dish['price'].replace('.', '', 1).isdigit(): node['offers']={'@type':'Offer','price':dish['price'],'priceCurrency':'AUD'}
            nodes.append(node)
        structured.append({'@type':'MenuSection','name':chinese,'hasMenuItem':nodes})
        sections.append(f'<section class="dish-section" id="{ident}" aria-labelledby="{ident}-title"><h2 id="{ident}-title">{esc(chinese)}</h2><ul>{"".join(rows)}</ul></section>')
    schema={'@context':'https://schema.org','@type':'Menu','name':'龍軒'+name+'菜單','url':PUBLIC+'/zh/menu/'+menu_id,'inLanguage':'zh-Hant','hasMenuSection':structured}
    tabs=''.join(f'<a href="{key}.html"{" aria-current=" + chr(34) + "page" + chr(34) if key==menu_id else ""}>{esc(CATEGORIES[key][0])}</a>' for key in MENU)
    order=(f'<a class="button button-solid" href="{esc(ORDER)}" target="_blank" rel="noopener">網上外賣 ↗</a><a class="text-link" href="{esc(DELIVERY)}" target="_blank" rel="noopener noreferrer">Uber Eats 送餐 <span aria-hidden="true">↗</span></a>' if menu_id=='takeaway' else '<a class="button button-solid" href="../index.html#visit">立即訂座 ⟶</a>')
    delivery_block = (f'<div class="menu-delivery menu-delivery-detail"><p>想享用外送？可透過 Uber Eats 訂購龍軒菜式。</p><a class="button button-outline" href="{esc(DELIVERY)}" target="_blank" rel="noopener noreferrer">在 Uber Eats 訂購 ↗</a></div>' if menu_id=="takeaway" else "")
    pdf=(f'<a class="text-link" href="../../menus/{esc(data["pdf"])}" type="application/pdf" target="_blank" rel="noopener">查看英文版 PDF <span aria-hidden="true">↗</span></a>' if data['pdf'] else '')
    return (head(name, description, '/zh/menu/'+menu_id, 2, menu_schema=schema) + header('menu/'+menu_id, True) + f'''<main id="main" class="menu-detail-page"><div class="menu-detail-wrap">
<nav class="breadcrumbs" aria-label="頁面路徑"><a href="../index.html">首頁</a><span aria-hidden="true">/</span><a href="../menu.html">菜單</a><span aria-hidden="true">/</span><span aria-current="page">{esc(name)}</span></nav>
<section class="menu-detail-hero" aria-labelledby="menu-detail-title"><div><p class="eyebrow">龍軒 · Sanctuary Cove</p><h1 id="menu-detail-title">{esc(name)}<em>菜單</em></h1><p class="menu-detail-lede">{esc(intro)}</p><div class="menu-detail-actions">{order}{pdf}</div></div><img src="../../assets/{esc(data['image'])}" alt="{esc(alt)}" width="1500" height="2250" fetchpriority="high"></section>
<nav class="menu-tabs" aria-label="菜單類別">{tabs}</nav>{delivery_block}
<div class="menu-detail-grid"><aside class="section-nav" aria-label="本頁菜式類別"><p class="eyebrow">本頁菜式</p>{''.join(section_links)}</aside><div class="dish-sections">{''.join(sections)}</div></div>
<p class="menu-disclaimer">{esc(note)}</p></div>
<section class="page-cta"><p class="eyebrow">歡迎光臨</p><h2>期待與您<em>相聚。</em></h2><a class="button button-outline-light" href="../index.html#visit">立即訂座 <span aria-hidden="true">⟶</span></a></section></main>''' + footer(True))


def main():
    OUT.mkdir(exist_ok=True)
    (OUT/'menu').mkdir(exist_ok=True)
    all_names={d['name'] for m in MENU.values() for _, dishes in m['sections'] for d in dishes}
    all_details={d['detail'] for m in MENU.values() for _, dishes in m['sections'] for d in dishes if d['detail']}
    assert all_names == NAME_ZH.keys(), (all_names-NAME_ZH.keys(), NAME_ZH.keys()-all_names)
    assert all_details == DETAIL_ZH.keys(), (all_details-DETAIL_ZH.keys(), DETAIL_ZH.keys()-all_details)
    for key,data in MENU.items():
        (OUT/'menu'/f'{key}.html').write_text(menu_page(key,data),encoding='utf-8')
    print('Built Traditional Chinese menu pages')

if __name__ == '__main__': main()
