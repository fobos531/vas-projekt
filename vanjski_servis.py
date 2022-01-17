import yfinance
from pyowm import OWM

def dajDionice(pretplate):
    response = ""
    podaci_dionica = []
    response += "\nPodaci o dionicama:\n"
    for dionica in pretplate:
        data = yfinance.download(tickers=dionica, period='1d', interval='1m')
        data = data.reset_index()
        response += f"-----{dionica}-----\n"
        podaci_dionica.append([dionica])
        kolone = ['Dio./Dat.']
      
        for indeks, redak in data.iterrows():
            pozicija_dionice = len(podaci_dionica) - 1
            cijena = round(redak['Close'], 2)
            format_date = redak['Datetime'].strftime('%d.%m. %HH:%mm')
            response += f"{format_date}: {cijena}\n"
            podaci_dionica[pozicija_dionice].append(cijena)
            kolone.append(format_date)
        print()

        response = f"{kolone[0] : <10}{kolone[1] : ^10}\n"
        for redak in podaci_dionica:
            response += f"{redak[0] : <10}{redak[1] : ^10} USD\n"
       
    return response


def dajTrenutnoVrijeme(latitude, longitude):
    owm = OWM("da1d5f83395449949871f34128d893be") 
    mgr = owm.weather_manager()
    obs = mgr.one_call(latitude, longitude)
    weather = obs.current

    temperature = str(weather.temperature('celsius').get('temp', 0))
    wind = str(weather.wind().get('speed', 0))
    return f'Vjetar: {wind} na koordinatama {latitude}, {longitude}, a temperatura {temperature} C'