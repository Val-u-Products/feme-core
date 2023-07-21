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
    user_token = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'


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
    nombre = models.CharField(max_length=255)

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
    id_mol = models.ForeignKey(Modulos, on_delete=models.CASCADE, db_column='id_mol')
    id_cont = models.CharField(primary_key=True, unique=True, max_length=255)
    orden = models.IntegerField()
    contenido = models.CharField(max_length=255)
    semana_recom = models.IntegerField()
    tipo = models.IntegerField()
    cm_acceso = models.BooleanField(default=True)

    class Meta:
        db_table = 'modulo_contenido'


class QuizTabla(models.Model):
    id_q = models.IntegerField(primary_key=True, unique=True)
    id_cont = models.ForeignKey(ModuloContenido, on_delete=models.CASCADE, db_column='id_cont')
    id_pregunta = models.CharField(max_length=255)
    quiz = models.IntegerField()
    seccion = models.IntegerField()
    titulo_de_seccion = models.CharField(max_length=255)
    pregunta = models.CharField(max_length=255)
    respuesta_correcta = models.CharField(max_length=255)
    respuesta_incorrecta_1 = models.CharField(max_length=255)
    respuesta_incorrecta_2 = models.CharField(max_length=255)
    respuesta_incorrecta_3 = models.CharField(max_length=255)
    respuesta_incorrecta_4 = models.CharField(max_length=255)
    explicacion_correcta = models.CharField(max_length=255)

    class Meta:
        db_table = 'quiz_tabla'


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
