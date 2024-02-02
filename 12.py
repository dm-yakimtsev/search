import sys
from io import BytesIO
from Samples.geocoder import get_coordinates, get_ll_span
from Samples.mapapi_PG import show_map
import requests


# Пусть наше приложение предполагает запуск:
toponym_to_find = " ".join(sys.argv[1:])

if toponym_to_find:
    lat, lon = get_coordinates(toponym_to_find)
    ll_spn = f'll={lat},{lon}&spn=0.005,0.005'
    show_map(ll_spn, 'sat')
    ll, spn = get_ll_span(toponym_to_find)
    ll_spn = f'll={ll}&spn={spn}'
    show_map(ll_spn, 'sat')
    point_paramn = f'pt={ll}'
    show_map(ll_spn, "sat", add_params=point_paramn)
else:
    print('No data')
