from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Max, F
from django.core.validators import MaxValueValidator


class ColegioTabla(models.Model):
    uuid_cole = models.CharField(primary_key=True, unique=True, max_length=255)
    colegio = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    zona_horaria = models.CharField(max_length=255)
    sexo_colegio = models.CharField(max_length=255)
    pais = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'colegio_tabla'


class SalonTabla(models.Model):
    uuid_salon = models.CharField(primary_key=True, unique=True, max_length=255)
    cierre_definitivo = models.DateTimeField(default=timezone.now, null=True)
    per_puntaje = models.IntegerField(null=True)
    materia_feme = models.CharField(max_length=255, null=True)
    s_acceso = models.BooleanField(default=False)
    cv = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'salon_tabla'


class Rol(models.Model):
    rol = models.CharField(primary_key=True, unique=True, max_length=255)
    nombre = models.CharField(max_length=255)
    permisos = models.CharField(max_length=255)

    class Meta:
        db_table = 'rol'


class Usuarios(models.Model):
    id_v = models.IntegerField(primary_key=True, unique=True)
    uuid_cole = models.ForeignKey(ColegioTabla, on_delete=models.CASCADE, db_column='uuid_cole')
    uuid_salon = models.ForeignKey(SalonTabla, on_delete=models.CASCADE, db_column='uuid_salon')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='rol')
    colegio = models.CharField(max_length=255)
    grado = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    whatsapp = models.IntegerField(null=True)
    email = models.CharField(max_length=255)
    inscrito = models.CharField(max_length=2)
    user_token = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

    def get_salones(self):
        salones = SalonKpiModulo.objects.filter(id_profe=self.id_v)
        return salones

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

    def restore(self):
        self.deleted = False
        self.save()
        

class ValuThinkific(models.Model):
    id_thinkific = models.IntegerField(primary_key=True, unique=True)
    id_v = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='id_v')

    class Meta:
        db_table = 'valu_thinkific'


class EstatusThinkific(models.Model):
    id_t = models.IntegerField(primary_key=True, unique=True)
    id_thinkific = models.ForeignKey(ValuThinkific, on_delete=models.CASCADE, db_column='id_thinkific')
    modulo = models.CharField(max_length=255)
    started_at = models.DateTimeField(default=timezone.now, null=True)
    activated_at = models.DateTimeField(default=timezone.now, null=True)
    expirated_at = models.DateTimeField(default=timezone.now, null=True)
    completed_at = models.DateTimeField(default=timezone.now, null=True)
    per_completacion = models.IntegerField()
    per_videos = models.IntegerField()
    estatus = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    last_sign_in = models.DateTimeField(default=timezone.now, null=True)
    nota_quiz1 = models.FloatField(null=True)
    nota_quiz2 = models.FloatField(null=True)
    nota_quiz3 = models.FloatField(null=True)
    fecha_q1 = models.DateTimeField(default=timezone.now, null=True)
    fecha_q2 = models.DateTimeField(default=timezone.now, null=True)
    fecha_q3 = models.DateTimeField(default=timezone.now, null=True)
    nota_quizes = models.FloatField()
    nota_progreso = models.FloatField()
    nota_total = models.IntegerField()
    nota_total_l = models.CharField(max_length=255)
    e_acceso = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'estatus_thinkific'

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

    def restore(self):
        self.deleted = False
        self.save()


class EstatusValu(models.Model):
    id_ev = models.IntegerField(primary_key=True, unique=True)
    id_v = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='id_v')
    modulo = models.CharField(max_length=255)
    started_at = models.DateTimeField(null=True)
    activated_at = models.DateTimeField(default=timezone.now, null=True)
    expirated_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)
    per_completacion = models.IntegerField(null=True)
    per_videos = models.IntegerField(null=True)
    estatus = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    last_sign_in = models.DateTimeField(null=True)
    nota_quiz1 = models.FloatField(null=True)
    intento_quiz1 = models.IntegerField(null=True)
    nota_quiz2 = models.FloatField(null=True)
    intento_quiz2 = models.IntegerField(null=True)
    nota_quiz3 = models.FloatField(null=True)
    intento_quiz3 = models.IntegerField(null=True)
    fecha_q1 = models.DateTimeField(null=True)
    fecha_q2 = models.DateTimeField(null=True)
    fecha_q3 = models.DateTimeField(null=True)
    nota_total = models.IntegerField(null=True)
    nota_total_l = models.CharField(max_length=255)
    e_acceso = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    leccion_completada = models.IntegerField(null=True)

    class Meta:
        db_table = 'estatus_valu'

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

    def restore(self):
        self.deleted = False
        self.save()


class Modulos(models.Model):
    id_mol = models.CharField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'modulos'


class ContenidosColegio(models.Model):
    id_c = models.IntegerField(primary_key=True, unique=True)
    uuid_salon = models.ForeignKey(SalonTabla, on_delete=models.CASCADE, db_column='uuid_salon')
    lapso = models.CharField(max_length=255)
    id_mol = models.ForeignKey(Modulos, on_delete=models.CASCADE, db_column='id_mol')
    c_acceso = models.BooleanField(default=True)

    class Meta:
        db_table = 'contenidos_colegio'


class ModuloContenido(models.Model):
    id_mol = models.ForeignKey(Modulos, on_delete=models.CASCADE, db_column='id_mol', null=True)
    id_cont = models.CharField(primary_key=True, unique=True, max_length=255)
    orden_c = models.IntegerField(null=True)
    semana_recom = models.IntegerField(null=True)
    tipo = models.CharField(max_length=255, null=True)
    cm_acceso = models.BooleanField(default=True, null=True)

    class Meta:
        db_table = 'modulo_contenido'


class QuizTabla(models.Model):
    id_q = models.IntegerField(unique=True)
    id_cont = models.ForeignKey(ModuloContenido, on_delete=models.CASCADE, db_column='id_cont', null=True)
    id_pregunta = models.CharField(primary_key=True, max_length=255)
    tipo = models.CharField(max_length=255, null=True)
    quiz = models.IntegerField(null=True)

    class Meta:
        db_table = 'quiz_tabla'


class MiniQuiz(models.Model):
    id_mq = models.IntegerField(null=True)
    id_cont = models.ForeignKey(ModuloContenido, on_delete=models.CASCADE, db_column='id_cont', null=True)
    opciones = models.TextField(null=True)
    valor = models.BooleanField(default=True, null=True)
    correcta = models.TextField(null=True)

    class Meta:
        db_table = 'mini_quiz'


class Guias(models.Model):
    id_g = models.IntegerField(null=True)
    id_cont = models.ForeignKey(ModuloContenido, on_delete=models.CASCADE, db_column='id_cont', null=True)
    contenido = models.TextField(null=True)
    orden = models.IntegerField(null=True)
    url_g = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'guias'


class SeleccionTodas(models.Model):
    id_pregunta = models.ForeignKey(QuizTabla, on_delete=models.CASCADE, db_column='id_pregunta', null=True)
    opciones = models.TextField(null=True)
    valor = models.BooleanField(default=True, null=True)
    pregunta = models.TextField(null=True)
    explicacion = models.TextField(null=True)
    puntos = models.IntegerField(null=True)
    correcta = models.TextField(null=True)

    class Meta:
        db_table = 'seleccion_todas'


class Orden(models.Model):
    id_pregunta = models.ForeignKey(QuizTabla, on_delete=models.CASCADE, db_column='id_pregunta', null=True)
    pregunta = models.TextField(null=True)
    opciones = models.TextField(null=True)
    orden_opcion = models.IntegerField(null=True)
    explicacion = models.TextField(null=True)
    puntos = models.IntegerField(null=True)

    class Meta:
        db_table = 'orden'


class Pareo(models.Model):
    id_pregunta = models.ForeignKey(QuizTabla, on_delete=models.CASCADE, db_column='id_pregunta', null=True)
    pregunta = models.TextField(null=True)
    opciones = models.TextField(null=True)
    lado_izq = models.CharField(max_length=255, null=True)
    explicacion = models.TextField(null=True)
    puntos = models.IntegerField(null=True)

    class Meta:
        db_table = 'pareo'


class Feedback(models.Model):
    # id_f = models.IntegerField(primary_key=True, unique=True)
    id_f = models.AutoField(primary_key=True, unique=True)
    id_v = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='id_v')
    feedback = models.CharField(max_length=255, null=True)
    errores = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'feedback'


class Monitoreo(models.Model):
    id_m = models.IntegerField(primary_key=True, unique=True)
    id_v = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='id_v')
    tiempo_sesion = models.IntegerField()
    sign_out = models.DateTimeField()
    sign_in = models.DateTimeField()
    dia = models.DateField()

    class Meta:
        db_table = 'monitoreo'


class Jerarquium(models.Model):
    id_j = models.IntegerField(primary_key=True, unique=True)
    id_estudiante = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='id_v')
    id_coordinador = models.IntegerField(null=True)
    id_profe = models.IntegerField(null=True)
    id_representante = models.IntegerField(null=True)

    class Meta:
        db_table = 'jerarquia'


class ActividadesCurriculum(models.Model):
    id_cont = models.ForeignKey(ModuloContenido, on_delete=models.CASCADE, db_column='id_cont')
    grado = models.CharField(max_length=255, null=True)
    titulo = models.TextField(null=True)
    curriculo = models.CharField(max_length=255, null=True)
    leccion = models.TextField(null=True)
    conceptos_claves = models.TextField(null=True)
    objetivos = models.TextField(null=True)
    tiempo = models.CharField(max_length=255, null=True)
    preparacion = models.TextField(null=True)
    materiales = models.TextField(null=True)
    resumen = models.TextField(null=True)
    descripcion = models.TextField(null=True)
    imagen_descriptiva = models.TextField(null=True)
    tipo_actividad = models.CharField(max_length=255, null=True)
    modalidad = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'actividades_curriculum'


class Interactivo(models.Model):
    id_cont = models.ForeignKey(ModuloContenido, on_delete=models.CASCADE, db_column='id_cont')
    id_escena = models.CharField(max_length=255, null=True)
    id_escena_siguiente = models.CharField(max_length=255, null=True)
    contenido = models.TextField(null=True)
    imagen = models.CharField(max_length=255, null=True)
    valor = models.TextField(null=True)
    tipo = models.CharField(max_length=1)

    class Meta:
        db_table = 'interactivo'


class Quiz1(models.Model):
    id_v = models.IntegerField(null=True)
    nota_quiz = models.FloatField()
    fecha_q = models.DateTimeField()
    intento_permitido = models.IntegerField(null=True, validators=[MaxValueValidator(3)])
    intento_extra = models.IntegerField(null=True)
    intento_t = models.IntegerField(null=True)

    class Meta:
        db_table = 'quiz_1'


class Quiz2(models.Model):
    id_v = models.IntegerField(null=True)
    nota_quiz = models.FloatField()
    fecha_q = models.DateTimeField()
    intento_permitido = models.IntegerField(null=True, validators=[MaxValueValidator(3)])
    intento_extra = models.IntegerField(null=True)
    intento_t = models.IntegerField(null=True)

    class Meta:
        db_table = 'quiz_2'


class Quiz3(models.Model):
    id_v = models.IntegerField(null=True)
    nota_quiz = models.FloatField()
    fecha_q = models.DateTimeField()
    intento_permitido = models.IntegerField(null=True, validators=[MaxValueValidator(3)])
    intento_extra = models.IntegerField(null=True)
    intento_t = models.IntegerField(null=True)

    class Meta:
        db_table = 'quiz_3'


class JProfeEst(models.Model):
    id_v = models.IntegerField()
    colegio = models.CharField(max_length=255)
    grado = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    whatsapp = models.IntegerField()
    email = models.CharField(max_length=255)
    inscrito = models.CharField(max_length=2)
    rol = models.CharField(max_length=255)
    uuid_cole = models.CharField(max_length=255)
    uuid_salon = models.CharField(max_length=255)
    user_token = models.CharField(max_length=255)
    id_profe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'j_profe_est'


class EstProfe(models.Model):
    id_v = models.IntegerField(primary_key=True)
    colegio = models.CharField(max_length=255)
    grado = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    whatsapp = models.IntegerField()
    email = models.CharField(max_length=255)
    inscrito = models.CharField(max_length=2)
    rol = models.CharField(max_length=255)
    uuid_cole = models.CharField(max_length=255)
    uuid_salon = models.CharField(max_length=255)
    user_token = models.CharField(max_length=255)
    id_profe = models.IntegerField()
    nombre_monitor = models.CharField(max_length=255)
    apellido_monitor = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'est_profe'


class RankingEstudiantes(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    uuid_salon = models.CharField(max_length=255)
    id_v = models.IntegerField(primary_key=True)
    nota_promedio = models.BigIntegerField()
    modulos_completados = models.BigIntegerField()
    ranking = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ranking_estudiantes'


class EstatusGeneral(models.Model):
    id_v = models.IntegerField(primary_key=True)
    colegio = models.CharField(max_length=255)
    grado = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    modulo = models.CharField(max_length=255)
    started_at = models.DateTimeField()
    activated_at = models.DateTimeField()
    expirated_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    per_completacion = models.IntegerField()
    per_videos = models.IntegerField()
    estatus = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    last_sign_in = models.DateTimeField()
    nota_quiz1 = models.FloatField()
    nota_quiz2 = models.FloatField()
    nota_quiz3 = models.FloatField()
    fecha_q1 = models.DateTimeField()
    fecha_q2 = models.DateTimeField()
    fecha_q3 = models.DateTimeField()
    nota_total = models.IntegerField()
    nota_total_l = models.CharField(max_length=255)
    e_acceso = models.BooleanField(default=True)
    uuid_salon = models.CharField(max_length=255)
    uuid_cole = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'estatus_general_2'


class ModulosRankingEstudiantes(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    uuid_salon = models.CharField(max_length=255)
    nombre_monitor = models.CharField(max_length=255)
    apellido_monitor = models.CharField(max_length=255)
    modulo = models.CharField(max_length=255)
    id_v = models.IntegerField()
    nota_total = models.IntegerField()
    id_modulo = models.BigIntegerField()
    ranking = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'modulos_ranking_estudiantes'


class SalonKpiModulo(models.Model):
    total_estudiantes = models.BigIntegerField(db_column='total_estudiantes')
    estudiantes_iniciados = models.BigIntegerField(db_column='estudiantes_iniciados')
    estudiantes_50 = models.BigIntegerField(db_column='estudiantes_50')
    estudiantes_completados = models.BigIntegerField(db_column='estudiantes_completados')
    uuid_salon = models.CharField(primary_key=True, max_length=255)
    grado = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    modulo = models.CharField(max_length=255)
    nombre_monitor = models.CharField(max_length=255)
    apellido_monitor = models.CharField(max_length=255)
    id_profe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salon_kpi_modulo'


class SalonInfoProfe(models.Model):
    uuid_cole = models.CharField(max_length=255)
    uuid_salon = models.CharField(primary_key=True, max_length=255)
    colegio = models.CharField(max_length=255)
    grado = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    total_estudiantes = models.BigIntegerField()
    per_completados = models.BigIntegerField()
    per_avanzado = models.BigIntegerField()
    per_solo_iniciado = models.BigIntegerField()
    per_no_iniciaron = models.BigIntegerField()
    per_pendiente = models.BigIntegerField()
    completados = models.BigIntegerField()
    avanzado = models.BigIntegerField()
    solo_iniciado = models.BigIntegerField()
    no_iniciaron = models.BigIntegerField()
    pendiente = models.BigIntegerField()
    id_profe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salon_info_profe'


class InfoProfe(models.Model):
    colegio = models.CharField(max_length=255)
    grado = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    uuid_cole = models.CharField(primary_key=True, max_length=255)
    uuid_salon = models.CharField(max_length=255)
    id_profe = models.IntegerField()
    nombre_monitor = models.CharField(max_length=255)
    apellido_monitor = models.CharField(max_length=255)
    whatsapp_monitor = models.IntegerField()
    email_monitor = models.CharField(max_length=255)
    inscrito_monitor = models.CharField(max_length=2)
    user_token_monitor = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'est_profe2'


class Actividades(models.Model):
    id_mol = models.ForeignKey(Modulos, on_delete=models.CASCADE, db_column='id_mol')
    titulo = models.CharField(max_length=255, null=True)
    leccion = models.CharField(max_length=255, null=True)
    conceptos_claves = models.TextField(null=True)
    objetivo = models.TextField(null=True)
    lapso_vz = models.CharField(max_length=255, null=True)
    lapso_mx = models.CharField(max_length=255, null=True)
    tiempo = models.CharField(max_length=255, null=True)
    preparacion = models.TextField(null=True)
    materiales = models.TextField(null=True)
    resumen = models.TextField(null=True)
    descripcion = models.TextField(null=True)
    imagen_descriptiva = models.CharField(max_length=255, null=True)
    modalidad = models.CharField(max_length=255, null=True)
    tipo_actividad = models.CharField(max_length=255, null=True)
    competencias = models.TextField(null=True)

    class Meta:
        db_table = 'actividades'


class ActividadSiguiente(models.Model):
    id_profe = models.IntegerField()
    uuid_salon = models.CharField(primary_key=True, max_length=255)
    grado = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    contenido = models.TextField(null=True)
    titulo = models.TextField(null=True)
    fecha_siguiente_semana = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'leccion_siguiente'


class ActividadSemanalEstudiantes(models.Model):
    id_profe = models.IntegerField()
    uuid_salon = models.CharField(primary_key=True, max_length=255)
    grado = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    numero_estudiantes = models.IntegerField()
    lecciones_completadas = models.BigIntegerField()
    porcentaje_lecciones_completadas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leccion_semanal_estudiantes'


class ActividadCvProfe(models.Model):
    fecha_recom = models.DateTimeField(auto_now_add=True)
    id_mol = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    id_profe = models.IntegerField()
    uuid_salon = models.CharField(primary_key=True, max_length=255)
    grado = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    colegio = models.CharField(max_length=255)
    cv = models.CharField(max_length=255)
    id_cont = models.CharField(max_length=255)
    titulo = models.TextField(null=True)
    leccion = models.TextField(null=True)
    conceptos_claves = models.TextField(null=True)
    objetivos = models.TextField(null=True)
    tiempo = models.CharField(max_length=255)
    preparacion = models.TextField(null=True)
    materiales = models.TextField(null=True)
    resumen = models.TextField(null=True)
    descripcion = models.TextField(null=True)
    imagen_descriptiva = models.TextField(null=True)
    tipo_actividad = models.CharField(max_length=255)
    modalidad = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'actividad_cv_profe'


class Respuestas(models.Model):
    salon = models.CharField(max_length=255)
    numero_quiz = models.IntegerField()
    modulos = models.CharField(primary_key=True, max_length=255)
    nivel = models.TextField(null=True)
    edad = models.TextField(null=True)
    preguntas = models.TextField(null=True)
    respuesta_correcta = models.TextField(null=True)
    explicacion = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'respuestas'


@receiver(post_save, sender=ContenidosColegio)
def crear_registros_estatus(sender, instance, **kwargs):
    # Obtén el valor máximo actual de id_ev
    max_id_ev = EstatusValu.objects.aggregate(Max('id_ev'))['id_ev__max'] or 0
    
    usuarios_con_mismo_uuid_salon = Usuarios.objects.filter(uuid_salon=instance.uuid_salon)

    for i, usuario in enumerate(usuarios_con_mismo_uuid_salon, start=1):
        user_instance = Usuarios.objects.get(id_v=usuario.id_v)
        modulo_nombre = instance.id_mol.nombre
        EstatusValu.objects.create(
            id_ev=max_id_ev + i,
            modulo = modulo_nombre,
            activated_at=timezone.now(),
            per_completacion=0,
            per_videos=0,
            estatus='no iniciado',
            created_at=timezone.now(),
            nota_quiz1=0,
            intento_quiz1=0,
            nota_quiz2=0,
            intento_quiz2=0,
            nota_quiz3=0,
            intento_quiz3=0,
            nota_total=0,
            nota_total_l='0',
            e_acceso=True,
            id_v=user_instance,
            leccion_completada=0,
            deleted=False
        )
