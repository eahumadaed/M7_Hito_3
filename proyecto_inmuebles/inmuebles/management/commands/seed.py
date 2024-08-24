import json
import os
from django.core.management.base import BaseCommand
from inmuebles.models import Region, Comuna

class Command(BaseCommand):
    help = 'Poblar la base de datos con las regiones y comunas de Chile'

    def handle(self, *args, **kwargs):
        # Obtener la ruta absoluta al archivo JSON
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, '../../../comunas_regiones.json')

        # Cargar el JSON
        with open(json_path, encoding='utf-8') as file:
            data = json.load(file)

        # Poblar las regiones y comunas
        for region_data in data['regiones']:
            region, created = Region.objects.get_or_create(nombre=region_data['region'])
            for comuna_nombre in region_data['comunas']:
                Comuna.objects.get_or_create(nombre=comuna_nombre, region=region)

        self.stdout.write(self.style.SUCCESS('Población de regiones y comunas completada.'))
