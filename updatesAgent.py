from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from spade.template import Template

import vanjski_servis
import globali


class updatesAgent(Agent):
    class UpdatesAgentPonasanje(PeriodicBehaviour):
        async def run(self):
            print(vanjski_servis.dajDionice(globali.dajPretplate()))            

            
    async def setup(self):
        print("Pokrenut agent za primanje updateova")
        b = self.UpdatesAgentPonasanje(period=int(self.period))
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)
