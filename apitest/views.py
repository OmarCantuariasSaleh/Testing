import requests
from django.shortcuts import render


# Create your views here.

def index(request):
    responseDolar = requests.get(
        'https://api.sbif.cl/api-sbifv3/recursos_api/dolar?apikey=4bf7fef2e83e5be2125b3631dc513ad6b9538331&formato=JSON')
    responseUF = requests.get(
        'https://api.sbif.cl/api-sbifv3/recursos_api/uf?apikey=4bf7fef2e83e5be2125b3631dc513ad6b9538331&formato=JSON')
    dolarData = responseDolar.json()
    ufData = responseUF.json()

    return render(request, 'apitest/index.html', {
        'title1': 'Dolar de Hoy',
        'title2': 'Uf de Hoy',
        'valorDolar': dolarData['Dolares'][0]['Valor'],
        'fechaDolar': dolarData['Dolares'][0]['Fecha'],
        'valorUf': ufData['UFs'][0]['Valor'],
        'fechaUf': ufData['UFs'][0]['Fecha'],

    })


# def dolarHoy(request):
#     response = requests.get(
#         'https://api.sbif.cl/api-sbifv3/recursos_api/dolar?apikey=4bf7fef2e83e5be2125b3631dc513ad6b9538331&formato=JSON')
#     geodata = response.json()
#     return render(request, 'apitest/dolarHoy.html', {
#         'algo': 'Dolar',
#
#     })

def monthRange(request):
    yearRange1 = request.GET["Primero"]
    yearRange2 = request.GET["Segundo"]
    if yearRange1 <= yearRange2:
        finalRange = yearRange1 + '/' + yearRange2
        payload = {'apikey': '4bf7fef2e83e5be2125b3631dc513ad6b9538331', 'formato': 'JSON'}
        responseDolar = requests.get('https://api.sbif.cl/api-sbifv3/recursos_api/dolar/periodo/%s' % finalRange,
                                     params=payload)
        responseUF = requests.get('https://api.sbif.cl/api-sbifv3/recursos_api/uf/periodo/%s' % finalRange,
                                  params=payload)
        dolarData = responseDolar.json()
        ufData = responseUF.json()
        return render(request, 'apitest/index.html', {
            'jsonListDOLAR': dolarData['Dolares'],
            'jsonListUF': ufData['UFs'],
            'fecha1': yearRange1,
            'fecha2': yearRange2,
        })
    else:
        return render(request, 'apitest/index.html', {
            'title1': 'Fecha Incorrecta',
            'title2': 'Fecha Incorrecta',
        })
