from django.db import models
from django.utils import timezone


class ColegioTabla(models.Model):
    uuid_cole = models.CharField(primary_key=True, unique=True, max_length=255)
    colegio = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    zona_horaria = models.CharField(max_length=255)
    sexo_colegio = models.CharField(max_length=255)

    class Meta:
        db_table = 'colegio_tabla'


class SalonTabla(models.Model):
    uuid_salon = models.CharField(primary_key=True, unique=True, max_length=255)
    cierre_definitivo = models.DateTimeField(default=timezone.now, null=True)
    per_puntaje = models.IntegerField(null=True)
    materia_feme = models.CharField(max_length=255, null=True)
    s_acceso = models.BooleanField(default=True)

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

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
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

    class Meta:
        db_table = 'estatus_thinkific'


class EstatusValu(models.Model):
    id_ev = models.IntegerField(primary_key=True, unique=True)
    id_v = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='id_v')
    modulo = models.CharField(max_length=255)
    started_at = models.DateTimeField(default=timezone.now)
    activated_at = models.DateTimeField(default=timezone.now)
    expirated_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(default=timezone.now, null=True)
    per_completacion = models.IntegerField()
    per_videos = models.IntegerField()
    estatus = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    last_sign_in = models.DateTimeField(default=timezone.now)
    nota_quiz1 = models.FloatField()
    intento_quiz1 = models.IntegerField(null=True)
    nota_quiz2 = models.FloatField()
    intento_quiz2 = models.IntegerField(null=True)
    nota_quiz3 = models.FloatField()
    intento_quiz3 = models.IntegerField(null=True)
    fecha_q1 = models.DateTimeField(default=timezone.now, null=True)
    fecha_q2 = models.DateTimeField(default=timezone.now, null=True)
    fecha_q3 = models.DateTimeField(default=timezone.now, null=True)
    nota_total = models.IntegerField()
    nota_total_l = models.CharField(max_length=255)
    e_acceso = models.BooleanField(default=True)

    class Meta:
        db_table = 'estatus_valu'


class Modulos(models.Model):
    id_mol = models.CharField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'modulos'


# class ContenidosColegio(models.Model):
#     id_c = models.IntegerField(primary_key=True, unique=True)
#     uuid_salon = models.ForeignKey(SalonTabla, on_delete=models.CASCADE, db_column='uuid_salon')
#     lapso = models.CharField(max_length=255)
#     id_mol = models.ForeignKey(Modulos, on_delete=models.CASCADE, db_column='id_mol')
#     c_acceso = models.BooleanField(default=True)

#     class Meta:
#         db_table = 'contenidos_colegio'


class ModuloContenido(models.Model):
    id_mol = models.ForeignKey(Modulos, on_delete=models.CASCADE, db_column='id_mol', null=True)
    id_cont = models.CharField(primary_key=True, unique=True, max_length=255)
    orden_c = models.IntegerField(null=True)
    # contenido = models.CharField(max_length=255)
    semana_recom = models.IntegerField(null=True)
    tipo = models.IntegerField(null=True)
    cm_acceso = models.BooleanField(default=True, null=True)

    class Meta:
        db_table = 'modulo_contenido'


class QuizTabla(models.Model):
    id_q = models.IntegerField(primary_key=True, unique=True)
    id_cont = models.ForeignKey(ModuloContenido, on_delete=models.CASCADE, db_column='id_cont', null=True)
    id_pregunta = models.CharField(max_length=255, null=True)
    tipo = models.CharField(max_length=255, null=True)
    quiz = models.IntegerField(null=True)
    # seccion = models.IntegerField()
    # titulo_de_seccion = models.CharField(max_length=255)
    pregunta = models.CharField(max_length=255, null=True)
    # respuesta_correcta = models.CharField(max_length=255)
    # respuesta_incorrecta_1 = models.CharField(max_length=255)
    # respuesta_incorrecta_2 = models.CharField(max_length=255)
    # respuesta_incorrecta_3 = models.CharField(max_length=255)
    # respuesta_incorrecta_4 = models.CharField(max_length=255)
    explicacion_correcta = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'quiz_tabla'


class MiniQuiz(models.Model):
    id_mq = models.IntegerField(null=True)
    id_cont = models.ForeignKey(ModuloContenido, on_delete=models.CASCADE, db_column='id_cont', null=True)
    opciones = models.CharField(max_length=255, null=True)
    valor = models.BooleanField(default=True, null=True)

    class Meta:
        db_table = 'mini_quiz'


class Guias(models.Model):
    id_g = models.IntegerField(null=True)
    id_cont = models.ForeignKey(ModuloContenido, on_delete=models.CASCADE, db_column='id_cont', null=True)
    contenido = models.CharField(max_length=255, null=True)
    orden = models.IntegerField(null=True)
    url_g = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'guias'


class SeleccionTodas(models.Model):
    id_pregunta = models.ForeignKey(QuizTabla, on_delete=models.CASCADE, db_column='id_pregunta', null=True)
    opciones = models.CharField(max_length=255, null=True)
    valor = models.BooleanField(default=True, null=True)

    class Meta:
        db_table = 'seleccion_todas'


class Orden(models.Model):
    id_pregunta = models.ForeignKey(QuizTabla, on_delete=models.CASCADE, db_column='id_pregunta', null=True)
    correcta = models.CharField(max_length=255, null=True)
    opcion_1 = models.CharField(max_length=255, null=True)
    opcion_2 = models.CharField(max_length=255, null=True)
    opcion_3 = models.CharField(max_length=255, null=True)
    opcion_4 = models.CharField(max_length=255, null=True)
    opcion_5 = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'orden'


class Pareo(models.Model):
    id_pregunta = models.ForeignKey(QuizTabla, on_delete=models.CASCADE, db_column='id_pregunta', null=True)
    correcta = models.CharField(max_length=255, null=True)
    lado_izq = models.CharField(max_length=255, null=True)
    opcion_1 = models.CharField(max_length=255, null=True)
    opcion_2 = models.CharField(max_length=255, null=True)
    opcion_3 = models.CharField(max_length=255, null=True)
    opcion_4 = models.CharField(max_length=255, null=True)
    opcion_5 = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'pareo'


class Feedback(models.Model):
    id_f = models.IntegerField(primary_key=True, unique=True)
    id_v = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='id_v')
    feedback = models.CharField(max_length=255)
    errores = models.CharField(max_length=255)

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
