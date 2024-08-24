from django.test import TestCase
from .models import Usuario, TipoUsuario, Region, Comuna

class UsuarioModelTest(TestCase):
    def setUp(self):
        print("Configurando datos de prueba...")
        region = Region.objects.create(nombre='Metropolitana')
        print(f"Región creada: {region.nombre}")
        
        comuna = Comuna.objects.create(nombre='Santiago', region=region)
        print(f"Comuna creada: {comuna.nombre}")
        
        tipo_usuario = TipoUsuario.objects.create(descripcion='Arrendatario')
        print(f"Tipo de usuario creado: {tipo_usuario.descripcion}")
        
        usuario = Usuario.objects.create(
            nombres='Juan',
            apellidos='Perez',
            rut='12345678-9',
            direccion='Calle Falsa 123',
            telefono='987654321',
            email='juan.perez@example.com',
            tipo_usuario=tipo_usuario,
            comuna=comuna,
            region=region
        )
        print(f"Usuario creado: {usuario.nombres} {usuario.apellidos}")

    def test_usuario_creation(self):
        print("Iniciando test de creación de usuario...")
        usuario = Usuario.objects.get(email='juan.perez@example.com')
        print(f"Usuario obtenido: {usuario.nombres} {usuario.apellidos}")
        
        self.assertEqual(usuario.nombres, 'Juan')
        print("Test de nombres pasado.")
        
        self.assertEqual(usuario.apellidos, 'Perez')
        print("Test de apellidos pasado.")
