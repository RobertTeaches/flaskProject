from typing import List
from app.data_models.bounty_models import Bounty, BountyTheme
import requests
import json.decoder
import random

def image_from_wix(url:str) -> str:
    raw_source = url.replace("wix:image://v1/", "")
    raw_source = raw_source[0:raw_source.index('/')]
    raw_source = "https://static.wixstatic.com/media/" + raw_source
    return raw_source

def get_bounties() -> List[Bounty]:
    response = requests.get('https://www.sigmateaches.com/_functions/allbounties/150')

    #print(response.headers)
    items = json.loads(response.content)
    bounties = []
    #print(items)
    if items:
        for k in items["items"]:
            _b = Bounty(title=k["name"], description=k["bountyDescription"], reward=k["rewardAmount"],
                        theme=k["bountyTheme"])
            if "bountyImage" in k:
                raw_source: str = k["bountyImage"]
                _b.image_src = image_from_wix(raw_source)
            # else:
                # print(f"{_b.title} does not have an image, apparently")

            bounties.append(_b)
    return bounties

def get_bounty_theming() -> {}:
    response = requests.get("https://www.sigmateaches.com/_functions/bountytheming/")
    content = json.loads(response.content)
    themes = {}
    if content:
        for k in content["items"]:
            if "icon" in k and "title" in k and "color" in k:
                _t = BountyTheme(name=k["title"], header_color=k["color"], icon_url = k["icon"])
                themes[_t.name] = _t

    return themes


def get_themes(bounties: List[Bounty]) -> List[str]:
    _themes = []
    for b in bounties:
        if b.theme not in _themes and len(b.theme) > 1:
            _themes.append(b.theme)

    return _themes
