import time

from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template

from vanjski_servis import dajDionice, dajTrenutnoVrijeme

from updatesAgent import updatesAgent

import globali


class vanjskiServisiAgent(Agent):
    class VanjskiServisPonasanje(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=9999999)
            if msg:
                print("Vanjski servisi agent primio poruku: " + msg.body)
            
                if (msg.get_metadata('tip') == "pretplata"):
                    globali.pretplate.append(msg.body)

                if (msg.get_metadata('tip') == "dionice"):
                    msg = Message(to="jglavina@rec.foi.hr")
                    msg.set_metadata('performative', 'inform')
                    msg.body = dajDionice(globali.pretplate)
                    await self.send(msg)

                if (msg.get_metadata('tip') == "vrijeme"):
                    koordinate = msg.body.split(';')
                    msg = Message(to="jglavina@rec.foi.hr")
                    msg.set_metadata('performative', 'inform')
                    msg.body = dajTrenutnoVrijeme(float(koordinate[0]), float(koordinate[1]))
                    await self.send(msg)
                
                if (msg.get_metadata('tip') == "automatsko_obavjestavanje"):
                    print()
                    self.agent.updatorAgent.period = msg.body
                    await self.agent.updatorAgent.start()
                    

    async def setup(self):
        print("Pokrenut agent za vanjske servise")
        b = self.VanjskiServisPonasanje()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)


if __name__ == "__main__":
    updator = updatesAgent("agent@rec.foi.hr", "tajna")

    vanjskiServisiAgent = vanjskiServisiAgent("jglavina2@rec.foi.hr", "Mjesecfobos12")
    vanjskiServisiAgent.updatorAgent = updator
    futureAgent1 = vanjskiServisiAgent.start(auto_register=True)
    futureAgent1.result() # pricekaj da se vanjski servisi agent pokrene

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            vanjskiServisiAgent.stop()
            break
