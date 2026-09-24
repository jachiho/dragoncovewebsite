"""Build Dragon Cove's crawlable, static menu pages from the printed menus.

Edit MENU below when the restaurant changes dishes or prices, then run this file.
The generated HTML is committed with the site; no browser JavaScript is needed.
"""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).parent
OUT = ROOT / "dist" / "menu"
PUBLIC = "https://dragoncove.netlify.app"
ORDER = "https://order.platform.hungryhungry.com/dragoncove/menu"


def item(name, price=None, detail=None):
    return {"name": name, "price": price, "detail": detail}


MENU = {
    "yum-cha": {
        "name": "Yum Cha",
        "intro": "Steamed dumplings, crispy favourites, soft bao and small dishes. Served at lunch.",
        "description": "Dragon Cove's full yum cha menu in Sanctuary Cove: har gow, siu mai, bao, dumplings and small dishes with prices.",
        "image": "menu-yum-cha.webp",
        "image_alt": "Steamed dumplings in a bamboo basket",
        "pdf": "yum-cha.pdf",
        "note": "Yum cha is available at lunch only. Prices are in Australian dollars.",
        "sections": [
            ("Steamed dumplings", [
                item("11. Har Gow Prawn Dumpling", "19"),
                item("12. Siu Mai (Pork & Prawn)", "21.50"),
                item("13. Scallop & Prawn Dumpling", "15.50"),
                item("14. Shanghai Soup Dumpling", "18"),
                item("15. Prawn and Chive Dumpling", "14"),
                item("16. Prawn Coriander Roll", "14"),
                item("17. Truffle Mushroom Dumplings", "14"),
            ]),
            ("Crispy dumplings", [
                item("21. Crispy Prawn Wontons", "16"),
                item("22. Chicken Dumplings", "20"),
                item("23. Pork and Garlic Chives Dumplings", "20"),
            ]),
            ("Steamed bao", [
                item("31. Golden Lava Custard Buns (3 pieces)", "16"),
                item("32. BBQ Pork Buns", "14"),
                item("33. Matcha Buns", "14"),
            ]),
            ("Pan & deep fried", [
                item("41. Spring Rolls (Pork or Vegetarian)", "15"),
                item("42. Curry Puffs", "16"),
                item("43. Prawn Tofu Skin Roll", "16"),
                item("44. Prawn Toasts", "16"),
                item("45. Fried Glutinous Ball", "15"),
                item("46. Satay Chicken Skewers", "18"),
                item("47. Salt & Pepper White Bait", "18"),
            ]),
            ("Small dishes", [
                item("51. Chicken Feet", "13"),
                item("52. Garlic Spare Ribs", "14"),
                item("53. Salt & Pepper Quail", "18"),
                item("54. Steamed Beef Meat Ball", "13"),
                item("55. Honeycomb Tripe", "14"),
                item("56. Soya Noodle with Bean Sprouts", "18"),
                item("57. Rice Noodle with XO Sauce", "25"),
            ]),
        ],
    },
    "a-la-carte": {
        "name": "A la Carte",
        "intro": "Cantonese favourites and dishes made for sharing, from handmade dumplings to live seafood.",
        "description": "Explore Dragon Cove's full à la carte Chinese menu in Sanctuary Cove, including live seafood, Peking duck, dumplings, claypots, meat, vegetables and noodles.",
        "image": "menu-a-la-carte.webp",
        "image_alt": "Glazed Cantonese dish served with greens",
        "pdf": "a-la-carte.pdf",
        "note": "Prices are in Australian dollars. Live seafood is subject to market price. Please tell our team about dietary requirements; dishes may contain nuts or shellfish. A 15% public holiday surcharge applies.",
        "sections": [
            ("Specials", [
                item("Fresh Lobster with Ginger and Shallot", "188", "Approximately 700–800g each; add noodles for $15."),
                item("Queensland A-Grade Fresh Mud Crab", "158", "Approximately 900g–1kg each. Recommended Singaporean style; add six crispy mantou for $12."),
            ]),
            ("Soup", [
                item("Hot & Sour Soup", "12", "Spicy Szechuan soup with prawn, shredded pork and tofu."),
                item("Sweet Corn Soup with Chicken", "12"),
                item("Sweet Corn Soup with Crab Meat", "14"),
                item("Wonton Soup", "15"),
                item("Seafood & Tofu Soup", "16"),
            ]),
            ("Appetizers", [
                item("Home-Made Spring Rolls (4)", "15", "Pork and assorted vegetables, sweet chilli sauce."),
                item("Vegetarian Spring Rolls (4)", "15", "Assorted Chinese vegetables, sweet chilli sauce."),
                item("Prawn Thin Spring Rolls (5)", "17"),
                item("Sesame Prawn Toast (4)", "16", "Sesame and prawns on crispy toast with creamy mayonnaise."),
                item("Five Spices Quail (1 bird, 2 pieces)", "17"),
                item("Satay Chicken Skewers (4)", "18", "Chicken breast, peanut and satay sauce, with pineapple and cucumber."),
                item("Curry Puffs (3)", "16", "Pork and vegetables with curry sauce in puff pastry."),
                item("Crispy Jumbo Oysters (4)", "22", "Battered Tasmanian oysters with spicy salt."),
                item("Steamed Scallops with Garlic (3)", "21", "Australian scallops steamed in the shell with vermicelli."),
                item("Chicken San Choy Bao (4)", "19", "Wok-fried filling in lettuce leaves."),
                item("Duck San Choy Bao (4)", "21", "Wok-fried filling in lettuce leaves."),
                item("Seafood San Choy Bao (4)", "21", "Wok-fried filling in lettuce leaves."),
            ]),
            ("Dumplings", [
                item("Dim Sum Basket (6)", "24", "Prawn dumpling, siu mai and xiao long bao."),
                item("Dragon Cove Siu Mai (5)", "20", "Steamed dim sum topped with prawn and fish roe."),
                item("Xiao Long Bao (6)", "18", "Steamed pork dumplings with broth inside; vinegar on the side."),
                item("Prawn Dumplings (4)", "19"),
                item("Spicy Wontons (5)", "19", "Steamed pork wontons with spicy vinaigrette."),
                item("Steamed Vegetarian Dumplings (5)", "18"),
                item("Crispy Pork and Chives Dumplings (5)", "19"),
            ]),
            ("Peking duck", [
                item("Two courses · Half duck", "58", "Six Peking duck pancakes, then your choice of duck san choy bao (4), roast duck, duck fried rice or noodles, or duck stir-fry. Extra lettuce wraps $3 each."),
                item("Two courses · Full duck", "84", "Twelve Peking duck pancakes, then your choice of duck san choy bao (8), roast duck, duck fried rice or noodles, or duck stir-fry. Extra lettuce wraps $3 each."),
            ]),
            ("Live seafood · market price", [
                item("Lobster", "Market price", "Sashimi; sautéed in supreme broth; typhoon shelter style; garlic butter; golden spicy; or salt and pepper."),
                item("Coral Trout", "Market price", "Steamed with ginger and shallot, wok-fried with snow peas, salt and pepper, or typhoon shelter style."),
                item("Abalone", "Market price", "Steamed, poached or wok-fried with XO sauce."),
                item("Mud Crab", "Market price", "Ginger and shallot; Singaporean; salt and pepper; typhoon shelter; black pepper and butter; egg yolk; egg yolk and vermicelli; steamed with Hua Diao wine and egg white; or wok-fried with foie gras (extra cost)."),
                item("King Crab", "Market price", "Ginger and shallot; Singaporean; salt and pepper; typhoon shelter; black pepper and butter; egg yolk; egg yolk and vermicelli; steamed with Hua Diao wine and egg white; or wok-fried with foie gras (extra cost)."),
                item("Snow Crab", "Market price", "Ginger and shallot; Singaporean; salt and pepper; typhoon shelter; black pepper and butter; egg yolk; egg yolk and vermicelli; steamed with Hua Diao wine and egg white; or wok-fried with foie gras (extra cost)."),
            ]),
            ("Claypot & teppan", [
                item("Black Pepper Beef in Teppan", "43", "Diced eye fillet and mushrooms with black pepper sauce on a hot plate."),
                item("Mongolian Lamb in Teppan", "37"),
                item("Black Pepper Chicken in Teppan", "31"),
                item("Garlic or Black Pepper King Prawns in Teppan", "41"),
                item("Live Mud Crab in Clay Pot (900g)", "Market price", "With vermicelli, XO sauce and salted egg yolk."),
                item("Taiwanese Style Basil Chicken in Claypot", "33", "Chicken thigh with soy, Shaoxing wine, ginger, garlic and Thai basil."),
                item("XO King Prawns with Vermicelli in Clay Pot", "47", "Large king prawns in shell with XO sauce."),
                item("Preserved Fish and Eggplant in Clay Pot", "29", "With minced chicken, dried chilli and spice."),
                item("Braised Beef Brisket in Clay Pot", "35", "Slow-cooked beef brisket in special sauce."),
            ]),
            ("Seafood", [
                item("Seafood Supreme", "42", "Wok-fried prawns, scallops, fish, calamari, broccoli and pine nuts."),
                item("Nutty Prawns", "42", "King prawns with toasted macadamia nuts and broccoli."),
                item("XO Stir Fried Prawns and Scallops", "42", "King prawns, Australian scallops and beans in XO sauce."),
                item("Wok Fried Scallops", "48", "Australian scallops with snow peas."),
                item("Steamed Scallops with Garlic (6)", "42", "Australian scallops in the shell with vermicelli."),
                item("Steamed Fish Fillet", "37", "New Zealand orange roughy with ginger and shallot or black bean sauce."),
                item("Honey King Prawns", "39"),
                item("Salt & Pepper King Prawns", "39"),
                item("Salt & Pepper Calamari", "37"),
                item("Crispy White Bait with Golden Salt & Pepper", "32"),
            ]),
            ("Poultry", [
                item("Lychee Duck", "39", "Half duck, slow-roasted with lychee and plum sauce."),
                item("Slow Roast Duck", "37", "Half duck marinated and roasted in our oven."),
                item("Crispy Skin Chicken", "32", "Half chicken with Shandong vinaigrette."),
                item("Kung Pao Chicken", "30", "Chicken breast with chilli bean paste, dried chilli, onion, peppers and peanuts."),
                item("Honey or Lemon Chicken", "30"),
                item("Curry or Satay Chicken", "30"),
                item("Sweet & Sour Chicken", "30"),
                item("Bang Bang Chicken", "32", "Fried chicken with dried chilli, Sichuan spices and chilli oil."),
            ]),
            ("Meat", [
                item("Honey Pepper Wagyu Beef", "58", "Kiwami MB9+ wagyu with snow peas and mushrooms."),
                item("Beijing Beef", "33", "Crispy beef julienne with oriental sauce."),
                item("Stir Fried Eye Fillet with Tea Leaves", "42"),
                item("Peking Eye Fillet", "39", "Eye fillet and onion in Peking sauce."),
                item("Black Bean Beef", "30"),
                item("Sweet & Sour Pork", "30"),
                item("Garlic Pork Ribs", "39"),
                item("Sticky Glazed Pork", "39", "Pork ribs and pineapple in a sweet and tangy sauce."),
                item("Cumin Lamb", "36"),
                item("Fu Yung Combination Omelette", "30", "BBQ pork, chicken, onion and egg with gravy."),
                item("Wok Fried Lamb with Shallot", "36"),
            ]),
            ("Chinese delicacies", [
                item("Sichuan Pork Belly", "34", "With peppers, onion, capsicum, leek, fungus, shallots, chilli and mushrooms."),
                item("Free Range Chicken Hotpot", "68", "Half chicken with bones in master stock, served with vegetables."),
                item("Steamed Free Range Chicken (half)", "48"),
                item("Braised Whole Tasmanian Abalone", "From 128", "Each, in supreme oyster sauce."),
                item("Roast Baby Squab", "58", "One bird, six pieces; preorder required."),
                item("Stir Fried Pork Intestines in Spicy Sauce", "36"),
                item("Simmered Fish Fillet in Spicy Sauce", "58"),
            ]),
            ("Vegetables & tofu", [
                item("Ma Po Tofu", "26", "Chicken mince, onion and chilli paste."),
                item("Golden Crispy Tofu with Salted Egg Yolk", "32"),
                item("Braised Tofu", "26", "With seasonal vegetables, mushrooms, ginger and shallot."),
                item("Salt & Pepper Tofu", "26"),
                item("Four Seasons Beans", "26", "Green beans with chicken mince and onion."),
                item("Stir Fried Vegetables", "26", "Seasonal Chinese vegetables with garlic."),
                item("Chinese Vegetables with Oyster Sauce", "26", "Choice of kai lan, choy sum, bok choy or mixed vegetables."),
                item("Kung Pao Crispy Eggplant", "26"),
            ]),
            ("Rice & noodles", [
                item("Yangzhou Fried Rice", "22", "BBQ pork, prawn and egg."),
                item("Chicken Fried Rice", "21", "Chicken breast, lettuce and egg."),
                item("Duck Fried Rice", "23", "Roast duck, pineapple and egg."),
                item("Supreme Scallop Fried Rice", "34", "Dried scallops, local scallops and egg white."),
                item("Truffle Vegetable Fried Rice", "22", "Egg and assorted vegetables."),
                item("Seafood Noodle", "31", "Prawns, fish, calamari, scallops and vegetables with crispy noodles."),
                item("Chicken Noodle", "27", "Chicken breast and vegetables with crispy noodles."),
                item("Combination Noodle", "27", "Chicken, beef, BBQ pork and vegetables with crispy noodles."),
                item("Singapore Noodle", "27", "BBQ pork, prawns, onion, vermicelli, curry powder, capsicum, shallot and sesame."),
                item("Beef Ho Fun", "27", "Beef, onion, bean sprouts and shallots with flat rice noodles."),
                item("Jasmine Rice", "4.50"),
            ]),
        ],
    },
    "banquets": {
        "name": "Banquets",
        "intro": "Two generous set menus for a table of four or more, designed to be shared.",
        "description": "Dragon Cove's banquet menus in Sanctuary Cove: Banquet A at $58 per person and Banquet B at $88 per person, for four or more guests.",
        "image": "menu-banquets.webp",
        "image_alt": "Guests sharing Cantonese dishes around a table",
        "pdf": "banquets.pdf",
        "note": "Minimum four guests per banquet. Prices are per person in Australian dollars.",
        "sections": [
            ("Banquet A · $58 per person", [
                item("Vegetarian Spring Rolls"), item("Steamed Scallops with Ginger, Shallot & Vermicelli"),
                item("Xiao Long Bao"), item("Chicken San Choy Bao"), item("Lychee Duck"),
                item("Ginger & Shallot Fish Fillets"), item("Beijing Beef"), item("Chicken and Cashews"),
                item("Stir-fried Seasonal Vegetables"), item("Yangzhou Fried Rice"),
            ]),
            ("Banquet B · $88 per person", [
                item("Vegetarian Spring Rolls"), item("Steamed Scallops with Ginger, Shallot & Vermicelli"),
                item("Xiao Long Bao"), item("Peking Duck with Pancakes"), item("Seafood San Choy Bao"),
                item("Jumbo King Prawns in Singapore Style", detail="Served with crispy mantou."),
                item("Black Pepper Beef"), item("Mongolian Lamb"), item("Salt and Pepper Pork Ribs"),
                item("Crispy Skin Chicken"), item("Stir-fried Seasonal Vegetables"), item("Yangzhou Fried Rice"),
            ]),
        ],
    },
    "takeaway": {
        "name": "Takeaway",
        "intro": "Take Dragon Cove home. Browse the full takeaway selection, then place your order online.",
        "description": "Dragon Cove's full takeaway menu in Sanctuary Cove, including entrees, soup, seafood, poultry, beef, pork, lamb, rice and noodles with prices.",
        "image": "menu-takeaway.webp",
        "image_alt": "A neon takeaway sign",
        "pdf": None,
        "note": "Prices are in Australian dollars and may differ on Uber Eats. A 15% public holiday surcharge applies. Dishes may contain nuts or traces of nuts. Ask our team about allergens and dietary requirements.",
        "sections": [
            ("Peking duck", [
                item("Peking Duck Platter with San Choy Bao", "70", "Twelve pancakes and eight lettuce wraps."),
            ]),
            ("Entrees", [
                item("Dim Sum Basket (6)", "20"), item("Dragon Cove Siu Mai (5)", "17"),
                item("Xiao Long Bao Pork Dumplings (6)", "16"), item("Home Made Pork Spring Rolls (4)", "13"),
                item("Vegetarian Spring Rolls (4)", "13"), item("Prawn Thin Spring Rolls (4)", "16"),
                item("Spicy Wontons (5)", "16"), item("Sesame Prawn Toasts (2)", "14"),
                item("Five Spices Quail (1 bird, 2 pieces)", "15"), item("Crispy Jumbo Oysters (4)", "19"),
                item("Steamed Scallops with Garlic (3)", "15"), item("Satay Chicken Skewers (4)", "16"),
                item("Curry Puffs (3)", "14"), item("Steamed Vegetarian Dumplings (5)", "16"),
                item("Chicken San Choy Bao (4)", "16"), item("Roast Duck San Choy Bao (4)", "18"),
                item("Seafood San Choy Bao (4)", "18"),
                item("Pan Fried or Steamed Pork and Chives Dumplings (5)", "16"),
                item("Pan Fried or Steamed Chicken Dumplings (5)", "16"),
            ]),
            ("Soup", [
                item("Chicken & Corn Soup", "10"), item("Crab Meat & Corn Soup", "12"),
                item("Wonton Soup", "13"), item("Hot & Sour Soup", "10"),
                item("Seafood & Tofu Soup", "14"),
            ]),
            ("Omelette", [
                item("Fu Yung Omelette with Gravy", "25"), item("Prawn Omelette", "27"),
                item("BBQ Pork Omelette", "25"),
            ]),
            ("Seafood", [
                item("Seafood Supreme", "36"), item("Black Pepper Prawns", "33"),
                item("Garlic or Nutty Prawns", "33"), item("XO Prawns & Scallops", "36"),
                item("Crispy Jumbo Oysters (4)", "19"),
                item("Stir Fried Scallops with Snow Peas", "41"),
                item("Steamed Fish with Ginger & Shallot", "32"),
                item("Salt & Pepper King Prawns", "33"), item("Salt & Pepper Calamari", "32"),
            ]),
            ("Poultry", [
                item("Lychee Duck (half)", "33"), item("Slow Roast Duck (half)", "32"),
                item("Crispy Skin Chicken (half)", "27"), item("Taiwanese Basil Chicken", "28"),
                item("Kung Pao Chicken", "26"), item("Bang Bang Chicken", "27"),
                item("Honey or Lemon Chicken", "25"), item("Satay or Curry Chicken", "25"),
                item("Black Pepper Chicken", "25"), item("Sweet & Sour Chicken", "25"),
                item("Cashew Chicken", "26"), item("Chicken & Vegetables", "25"),
            ]),
            ("Vegetables & tofu", [
                item("Ma Po Tofu", "22"), item("Salt & Pepper Tofu", "22"),
                item("Crispy Tofu with Egg Yolk", "22"), item("Braised Tofu", "22"),
                item("Four Seasons Beans", "22"), item("Kai Lan with Oyster Sauce", "22"),
                item("Mixed Vegetables & Garlic", "22"), item("Braised Chinese Mushrooms", "32"),
            ]),
            ("Beef, pork & lamb", [
                item("Honey Pepper Wagyu", "50"), item("Black Pepper Beef Eye Fillet", "36"),
                item("Beijing Beef", "28"), item("Eye Fillet with Tea Leaves", "36"),
                item("Peking Eye Fillet", "34"), item("Black Bean Beef", "25"),
                item("Mongolian Beef", "25"), item("Cashew Beef", "25"),
                item("Sichuan Beef", "25"), item("Braised Beef Brisket", "25"),
                item("Beef & Vegetables Stir Fry", "25"), item("Sweet & Sour Pork", "25"),
                item("Garlic Pork Ribs", "33"), item("Sticky Glazed Pork Ribs", "33"),
                item("BBQ Pork with Honey & Plum", "25"), item("BBQ Pork with Vegetables", "25"),
                item("Mongolian Lamb", "31"), item("Wok Fried Lamb with Shallots", "31"),
                item("Cumin Lamb", "31"),
            ]),
            ("Rice & noodles", [
                item("Traditional Fried Rice", "19"), item("Chicken Fried Rice", "18"),
                item("Duck Fried Rice", "20"), item("Supreme Scallop Fried Rice", "29"),
                item("Truffle Vegetable Fried Rice", "18"), item("Seafood Noodle", "26"),
                item("Chicken Noodle", "23"), item("Combination Noodle", "23"),
                item("Singapore Noodle", "23"), item("Beef Ho Fun", "23"),
                item("Jasmine Rice", "5"),
            ]),
        ],
    },
}


def esc(value):
    return html.escape(str(value), quote=True)


def price_label(value):
    if value == "Market price":
        return value
    if value.startswith("From "):
        return "From $" + value.removeprefix("From ")
    return "$" + value


def slug(value):
    import re
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def header():
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="header">
<a class="seal" href="../index.html" aria-label="Dragon Cove home" lang="zh-Hant">龍<br>軒</a>
<nav class="site-nav" aria-label="Main navigation"><a href="../index.html">Home</a><a href="../menu.html" aria-current="page">Menu</a><a href="../private-room.html">Private Room</a><a href="../index.html#gift-card">Gift Card</a><a href="../index.html#visit">Visit</a></nav>
<div class="header-actions"><a class="button button-outline" href="{esc(ORDER)}" target="_blank" rel="noopener">Order Takeaway<span class="sr-only"> (opens ordering website)</span></a><a class="button button-solid" href="../index.html#visit">Book a Table</a></div>
<details class="mobile-nav"><summary aria-label="Open navigation">Menu <span aria-hidden="true">☰</span></summary><nav aria-label="Mobile navigation"><a href="../index.html">Home</a><a href="../menu.html" aria-current="page">Menu</a><a href="../private-room.html">Private Room</a><a href="../index.html#gift-card">Gift Card</a><a href="../index.html#visit">Visit</a><a href="{esc(ORDER)}" target="_blank" rel="noopener">Order Takeaway ↗</a><a href="../index.html#visit">Book a Table</a></nav></details>
</header>'''


def schema(menu_id, data):
    url = f"{PUBLIC}/menu/{menu_id}.html"
    sections = []
    for section_name, dishes in data["sections"]:
        nodes = []
        for dish in dishes:
            node = {"@type": "MenuItem", "name": dish["name"]}
            if dish["detail"]:
                node["description"] = dish["detail"]
            if dish["price"] and dish["price"].replace(".", "", 1).isdigit():
                node["offers"] = {"@type": "Offer", "price": dish["price"], "priceCurrency": "AUD"}
            nodes.append(node)
        sections.append({"@type": "MenuSection", "name": section_name, "hasMenuItem": nodes})
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": PUBLIC + "/"},
        {"@type": "ListItem", "position": 2, "name": "Menu", "item": PUBLIC + "/menu.html"},
        {"@type": "ListItem", "position": 3, "name": data["name"], "item": url},
    ]}
    menu = {"@context": "https://schema.org", "@type": "Menu", "name": f"Dragon Cove {data['name']} Menu", "url": url, "inLanguage": "en-AU", "hasMenuSection": sections}
    scripts = []
    for obj in (breadcrumb, menu):
        payload = json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")
        scripts.append(f'<script type="application/ld+json">{payload}</script>')
    return "\n".join(scripts)


def render(menu_id, data):
    name = data["name"]
    links = "".join(
        f'<a href="{esc(other_id)}.html" {"aria-current=" + chr(34) + "page" + chr(34) if other_id == menu_id else ""}>{esc(other["name"])}</a>'
        for other_id, other in MENU.items()
    )
    section_nav = "".join(f'<a href="#{slug(title)}">{esc(title)}</a>' for title, _ in data["sections"])
    sections = []
    for title, dishes in data["sections"]:
        rows = []
        for dish in dishes:
            detail = f'<p>{esc(dish["detail"])}</p>' if dish["detail"] else ""
            price = f'<span class="dish-price">{esc(price_label(dish["price"]))}</span>' if dish["price"] else ""
            rows.append(f'<li class="dish"><div><h3>{esc(dish["name"])}</h3>{detail}</div>{price}</li>')
        sections.append(f'<section class="dish-section" id="{slug(title)}" aria-labelledby="{slug(title)}-title"><h2 id="{slug(title)}-title">{esc(title)}</h2><ul>{"".join(rows)}</ul></section>')
    pdf = f'<a class="text-link" href="../menus/{esc(data["pdf"])}" type="application/pdf" target="_blank" rel="noopener">Download PDF <span aria-hidden="true">↗</span></a>' if data["pdf"] else ""
    order = f'<a class="button button-solid" href="{esc(ORDER)}" target="_blank" rel="noopener">Order takeaway ↗</a>' if menu_id == "takeaway" else '<a class="button button-solid" href="../index.html#visit">Book a table ⟶</a>'
    title = f'{esc(name)} Menu | Dragon Cove Sanctuary Cove'
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{esc(data['description'])}">
<link rel="canonical" href="{PUBLIC}/menu/{menu_id}.html">
<meta name="theme-color" content="#761714">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23761714'/%3E%3Ctext x='32' y='45' text-anchor='middle' font-family='serif' font-size='44' fill='%23f4eee4'%3ED%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=DM+Sans:wght@400;500&family=Noto+Serif+TC:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css">
{schema(menu_id, data)}
</head>
<body>
{header()}
<main id="main" class="menu-detail-page">
<div class="menu-detail-wrap">
<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a><span aria-hidden="true">/</span><a href="../menu.html">Menu</a><span aria-hidden="true">/</span><span aria-current="page">{esc(name)}</span></nav>
<section class="menu-detail-hero" aria-labelledby="menu-detail-title"><div><p class="eyebrow">Dragon Cove · Sanctuary Cove</p><h1 id="menu-detail-title">{esc(name)}<em> menu.</em></h1><p class="menu-detail-lede">{esc(data['intro'])}</p><div class="menu-detail-actions">{order}{pdf}</div></div><img src="../assets/{esc(data['image'])}" alt="{esc(data['image_alt'])}" width="1500" height="2250" fetchpriority="high"></section>
<nav class="menu-tabs" aria-label="Menu categories">{links}</nav>
<div class="menu-detail-grid"><aside class="section-nav" aria-label="On this menu"><p class="eyebrow">On this menu</p>{section_nav}</aside><div class="dish-sections">{''.join(sections)}</div></div>
<p class="menu-disclaimer">{esc(data['note'])}</p>
</div>
<section class="page-cta"><p class="eyebrow">See you at the table</p><h2>Make it a <em>date.</em></h2><a class="button button-outline-light" href="../index.html#visit">Book a Table <span aria-hidden="true">⟶</span></a></section>
</main>
<footer><a class="footer-brand" href="../index.html">Dragon Cove <span lang="zh-Hant">龍軒</span></a><p>Cantonese cuisine · Sanctuary Cove</p><a href="#main">Back to top ↑</a></footer>
</body>
</html>
'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for menu_id, data in MENU.items():
        (OUT / f"{menu_id}.html").write_text(render(menu_id, data), encoding="utf-8")
    print("Built", ", ".join(MENU), "menu pages")


if __name__ == "__main__":
    main()
