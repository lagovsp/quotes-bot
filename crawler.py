from datetime import datetime

import bs4
import requests

QUOTES_DATA = "https://metalbulletin.ru/allprices/87/892/"
MIN, MAX = 3500, 5000
CIRCLES = "🔴🟠🟡🟢🔵"


def get_circle(sr: float) -> str:
    """
    Choosing the colour of the status circle to indicate how good the market is
    """
    if sr <= MIN:
        return CIRCLES[0]
    if sr >= MAX:
        return CIRCLES[-1]

    step = (MAX - MIN) / len(CIRCLES)
    lb, rb, it = MIN, MIN + step, 0
    while True:
        if lb <= sr <= rb:
            return CIRCLES[it]
        it += 1
        lb, rb = rb, rb + step


def get_message() -> str:
    cur_time = datetime.now()
    res = requests.get(QUOTES_DATA, headers={"User-agent": "Mozilla/5.0"})

    soup = bs4.BeautifulSoup(res.text, "lxml")
    table = soup.find(
        "table",
        {
            "cellpadding": "0",
            "cellspacing": "0",
            "style": "padding:5px;font-family: Arial;font-size:13;margin-bottom: 25px;width:538px;",
        },
    )

    date, they_buy_quote, *_ = map(
        lambda x: x.text.lstrip(),
        table.find_all("td", {"style": "border-bottom:1px solid #b7bebf;"}),
    )
    they_sell_quote = table.find(
        "td", {"style": "border-bottom:1px solid #b7bebf;text-align:center;"}
    ).text.lstrip()

    res = cur_time.strftime(
        "{} %Y-%m-%d %H:%M".format(get_circle(float(they_sell_quote)))
    )
    res += "\n<b>1g Palladium Sberbank</b>\n"
    res += "<code>{} / {} ₽</code>".format(they_sell_quote, they_buy_quote)

    return res


if __name__ == "__main__":
    get_message()
