from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
import time

class interactionAgent(Agent):
    class PonasanjeInteractionAgenta(CyclicBehaviour):
        async def run(self):
            komanda = input("""
            Komande:
            1) Pretplata na neku od dionica (TSLA, GME, AAPL)
            2) Dohvaćanje cijena svih pretplaćenih dionica
            3) Dohvaćanje trenutnih vremenskih prilika za dane koordinate
            4) Postavljanje automatskih obavještavanja o stanju dionica
            Upisi komandu:""")
            
            msg = Message(to="jglavina2@rec.foi.hr")
            msg.set_metadata('performative', 'inform')

            if (komanda == "1"):
                dionica = input("Unesite kraticu dionice na koju se pretplacujete: ")
                msg.set_metadata('tip', 'pretplata')
                msg.body = dionica
                await self.send(msg)
            if (komanda == "2"):
                msg.set_metadata('tip', 'dionice')
                msg.body = ";"
                await self.send(msg)
            if (komanda == "3"):
                msg.set_metadata('tip', 'vrijeme')
                latitude = input("Unesi latitude: ")
                longitude = input("Unesi longitude: ")
                msg.body = latitude + ";" + longitude
                await self.send(msg)
            if (komanda == "4"):
                msg.set_metadata('tip', 'automatsko_obavjestavanje')
                interval = input("Unesi interval obavještavanja u sekundama: ")
                msg.body = interval
                await self.send(msg)

            msg = await self.receive(timeout=5)
            if msg:
                print("Korisnik interaction poruka\n" + msg.body)
                

            

    async def setup(self):
        print("Pokrenut agent za interakciju")
        b = self.PonasanjeInteractionAgenta()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)


if __name__ == "__main__":
    interactionAgent = interactionAgent("jglavina@rec.foi.hr", "Mjesecfobos12")
    futureAgent2 = interactionAgent.start(auto_register=True)
    futureAgent2.result() # pricekaj da se interaction agent pokrene


    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            interactionAgent.stop()
            break
