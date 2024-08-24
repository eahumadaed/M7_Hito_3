from django.shortcuts import get_object_or_404
from .models import Usuario, TipoUsuario, Region, Comuna, Inmueble, SolicitudArriendo, Pago

# Servicios para el modelo Usuario
def crear_usuario(data):
    tipo_usuario = get_object_or_404(TipoUsuario, id=data['id_tipo_usuario'])
    comuna = get_object_or_404(Comuna, id=data['id_comuna'])
    region = get_object_or_404(Region, id=data['id_region'])
    usuario = Usuario.objects.create(
        nombres=data['nombres'],
        apellidos=data['apellidos'],
        rut=data['rut'],
        direccion=data['direccion'],
        telefono=data['telefono'],
        email=data['email'],
        tipo_usuario=tipo_usuario,
        comuna=comuna,
        region=region
    )
    return usuario

def obtener_usuario(id_usuario):
    return get_object_or_404(Usuario, id=id_usuario)

def actualizar_usuario(id_usuario, data):
    usuario = get_object_or_404(Usuario, id=id_usuario)
    usuario.nombres = data.get('nombres', usuario.nombres)
    usuario.apellidos = data.get('apellidos', usuario.apellidos)
    usuario.rut = data.get('rut', usuario.rut)
    usuario.direccion = data.get('direccion', usuario.direccion)
    usuario.telefono = data.get('telefono', usuario.telefono)
    usuario.email = data.get('email', usuario.email)
    if 'id_tipo_usuario' in data:
        usuario.tipo_usuario = get_object_or_404(TipoUsuario, id=data['id_tipo_usuario'])
    if 'id_comuna' in data:
        usuario.comuna = get_object_or_404(Comuna, id=data['id_comuna'])
    if 'id_region' in data:
        usuario.region = get_object_or_404(Region, id=data['id_region'])
    usuario.save()
    return usuario

def eliminar_usuario(id_usuario):
    usuario = get_object_or_404(Usuario, id=id_usuario)
    usuario.delete()
    return usuario

# Servicios para el modelo Inmueble
def crear_inmueble(data):
    comuna = get_object_or_404(Comuna, id=data['id_comuna'])
    usuario = get_object_or_404(Usuario, id=data['id_usuario'])
    inmueble = Inmueble.objects.create(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        m2_construidos=data['m2_construidos'],
        m2_totales=data['m2_totales'],
        estacionamientos=data['estacionamientos'],
        habitaciones=data['habitaciones'],
        banos=data['banos'],
        direccion=data['direccion'],
        comuna=comuna,
        tipo_inmueble=data['tipo_inmueble'],
        precio_mensual=data['precio_mensual'],
        usuario=usuario
    )
    return inmueble

def obtener_inmueble(id_inmueble):
    return get_object_or_404(Inmueble, id=id_inmueble)

def actualizar_inmueble(id_inmueble, data):
    inmueble = get_object_or_404(Inmueble, id=id_inmueble)
    inmueble.nombre = data.get('nombre', inmueble.nombre)
    inmueble.descripcion = data.get('descripcion', inmueble.descripcion)
    inmueble.m2_construidos = data.get('m2_construidos', inmueble.m2_construidos)
    inmueble.m2_totales = data.get('m2_totales', inmueble.m2_totales)
    inmueble.estacionamientos = data.get('estacionamientos', inmueble.estacionamientos)
    inmueble.habitaciones = data.get('habitaciones', inmueble.habitaciones)
    inmueble.banos = data.get('banos', inmueble.banos)
    inmueble.direccion = data.get('direccion', inmueble.direccion)
    if 'id_comuna' in data:
        inmueble.comuna = get_object_or_404(Comuna, id=data['id_comuna'])
    inmueble.tipo_inmueble = data.get('tipo_inmueble', inmueble.tipo_inmueble)
    inmueble.precio_mensual = data.get('precio_mensual', inmueble.precio_mensual)
    inmueble.save()
    return inmueble

def eliminar_inmueble(id_inmueble):
    inmueble = get_object_or_404(Inmueble, id=id_inmueble)
    inmueble.delete()
    return inmueble

# Servicios para el modelo SolicitudArriendo
def crear_solicitud_arriendo(data):
    usuario = get_object_or_404(Usuario, id=data['id_usuario'])
    inmueble = get_object_or_404(Inmueble, id=data['id_inmueble'])
    solicitud = SolicitudArriendo.objects.create(
        usuario=usuario,
        inmueble=inmueble,
        fecha_solicitud=data['fecha_solicitud'],
        estado=data['estado']
    )
    return solicitud

def obtener_solicitud_arriendo(id_solicitud):
    return get_object_or_404(SolicitudArriendo, id=id_solicitud)

def actualizar_solicitud_arriendo(id_solicitud, data):
    solicitud = get_object_or_404(SolicitudArriendo, id=id_solicitud)
    solicitud.fecha_solicitud = data.get('fecha_solicitud', solicitud.fecha_solicitud)
    solicitud.estado = data.get('estado', solicitud.estado)
    if 'id_usuario' in data:
        solicitud.usuario = get_object_or_404(Usuario, id=data['id_usuario'])
    if 'id_inmueble' in data:
        solicitud.inmueble = get_object_or_404(Inmueble, id=data['id_inmueble'])
    solicitud.save()
    return solicitud

def eliminar_solicitud_arriendo(id_solicitud):
    solicitud = get_object_or_404(SolicitudArriendo, id=id_solicitud)
    solicitud.delete()
    return solicitud

# Servicios para el modelo Pago
def crear_pago(data):
    solicitud = get_object_or_404(SolicitudArriendo, id=data['id_solicitud'])
    pago = Pago.objects.create(
        solicitud=solicitud,
        fecha_pago=data['fecha_pago'],
        monto=data['monto']
    )
    return pago

def obtener_pago(id_pago):
    return get_object_or_404(Pago, id=id_pago)

def actualizar_pago(id_pago, data):
    pago = get_object_or_404(Pago, id=id_pago)
    pago.fecha_pago = data.get('fecha_pago', pago.fecha_pago)
    pago.monto = data.get('monto', pago.monto)
    if 'id_solicitud' in data:
        pago.solicitud = get_object_or_404(SolicitudArriendo, id=data['id_solicitud'])
    pago.save()
    return pago

def eliminar_pago(id_pago):
    pago = get_object_or_404(Pago, id=id_pago)
    pago.delete()
    return pago
