import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')
django.setup()

from inmuebles.models import Usuario, TipoUsuario, Region, Comuna

def limpiar_tablas():
    Usuario.objects.all().delete()
    TipoUsuario.objects.all().delete()
    Region.objects.all().delete()
    Comuna.objects.all().delete()
    print("Todas las tablas han sido limpiadas.")


def crear_objetos():
    tipo_usuario, created = TipoUsuario.objects.get_or_create(descripcion='Arrendatario')
    region, created = Region.objects.get_or_create(nombre='Metropolitana')
    comuna, created = Comuna.objects.get_or_create(nombre='Santiago', region=region)

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
    print(f'Usuario creado: {usuario}')

def enlistar_usuarios():
    usuarios = Usuario.objects.all()
    for usuario in usuarios:
        print(usuario.nombres, usuario.apellidos)

def actualizar_usuario(usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.direccion = 'Nueva Direccion 456'
    usuario.telefono = '123456789'
    usuario.save()
    print(f'Usuario actualizado: {usuario}')

def borrar_usuario(usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    print(f'Usuario borrado: {usuario}')

if __name__ == '__main__':
    limpiar_tablas()
    crear_objetos()
    enlistar_usuarios()
    actualizar_usuario(12)
    borrar_usuario(12)