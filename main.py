from requests_html import HTMLSession
from bs4 import BeautifulSoup
from collections import Counter
import pprint


def get_card_info(url, list_of_cards):
    session = HTMLSession()
    request = session.get(url)
    html = BeautifulSoup(request.text, 'lxml')

    turf_boost = html.select('div.skill')
    card_name = html.select('h2')[0].contents[0]

    card = {}
    card['name'] = card_name

    for boost in turf_boost:
        bonus_text = boost.contents[0]
        if ":" not in bonus_text:
            continue
        temp = bonus_text.split(":")
        level = temp[0]
        bonus = temp[1]
        list_of_cards.append(bonus)
        #card[level] = bonus

    #with open('cards.json',  'a', newline='') as f:
    #    json.dump(card, f)


def get_data_from_website():
    session = HTMLSession()
    baseURL = f'https://lordsmobilemaps.com'
    url = f'https://lordsmobilemaps.com/en/td/chapters'

    request = session.get(url)

    html = BeautifulSoup(request.text, 'lxml')

    chapters = html.select('div.cards')

    list_of_cards = []
    for cards in chapters:
        spec_card = cards.select('a')
        for card in spec_card:
            href = card['href']
            full_url = baseURL + href
            get_card_info(full_url, list_of_cards)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(Counter(list_of_cards))


    # guild_members_list = guild_info.select('div.toptabrow')

    # for member in guild_members_list:
    #     member_name = member.select('div:nth-child(2) a')[0].string
    #     member_might = member.select('div:nth-child(5)')[0].string
    #     member_kills = member.select('div:nth-child(6)')[0].string
    #     member_kingdom = member.select('div:nth-child(3)')[0].string


if __name__ == '__main__':
    get_data_from_website()
