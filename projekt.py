#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from korisnikInteractionAgent import interactionAgent

if __name__ == "__main__":
    interactionAgent = interactionAgent("jglavina@rec.foi.hr", "Mjesecfobos12")
    futureAgent2 = interactionAgent.start(auto_register=True)
    futureAgent2.result() # pricekaj da se telegram agent pokrene


    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            interactionAgent.stop()
            break
