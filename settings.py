"""
Módulo para configurações do Mando
"""
from decouple import config

__version__ = '0.0.3'

TOKEN = config('TOKEN', '')
API_URL = config('STAR_DESTROYER', '')
SETTINGS_MODULE = config('SETTINGS_MODULE', 'common')
