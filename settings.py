"""
Módulo para configurações do Mando
"""
from decouple import config

__version__ = '0.0.0'

TOKEN = config('TOKEN', '')
API_URL = config('STAR_DESTROYER', '')
