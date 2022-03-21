from typing import List
from app.data_models.bounty_models import Bounty
import requests
import json.decoder

def get_bounties() -> List[Bounty]:
    response = requests.get('https://www.sigmateaches.com/_functions/allbounties/150')

    print(response.headers)
    items = json.loads(response.content)
    bounties = []
    #print(items)
    if items:
        for k in items["items"]:
            _b = Bounty(title=k["name"], description=k["bountyDescription"], reward=k["rewardAmount"])
            bounties.append(_b)
        pass
    else:
        description = '''
                This is a test Bounty! We are seeing how this looks.
                Does it look good? Or bad? Or just like normal?
    
                How does <code>html</code> look in the Bounty literal?
            '''
        bounties.append(Bounty(title="Test Bounty", description=response))
        bounties.append(Bounty(title="Test Bounty 2", description=description))
        bounties.append(Bounty(title="Test BountyThe Third", description=description))
    return bounties
