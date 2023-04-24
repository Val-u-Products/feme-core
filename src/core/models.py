from django.db import models


class ColeTabla(models.Model):
    uuid_cole = models.TextField(primary_key=True, blank=True, null=False, db_column='uuid_cole')
    colegio = models.TextField(blank=True, null=True)
    ubicacion = models.TextField(blank=True, null=True)
    zona_horaria = models.TextField(blank=True, null=True)
    sexo_colegio = models.TextField(blank=True, null=True, db_column='sexo-colegio')
    zoho_link = models.TextField(blank=True, null=True, db_column='zoho_link_')

    class Meta:
        db_table = 'cole_tabla'


class EstudiantesTabla(models.Model):
    id_thinkific = models.TextField(primary_key=True, blank=True, null=False, db_column='id_thinkific')
    uuid_mont = models.TextField(blank=True, null=True)
    uuid_cole = models.ForeignKey(ColeTabla, on_delete=models.CASCADE, db_column='uuid_cole')
    uuid_salon = models.TextField(blank=True, null=True)
    colegio = models.TextField(blank=True, null=True)
    grado = models.TextField(blank=True, null=True)
    seccion = models.TextField(blank=True, null=True)
    nombres_estudiantes = models.TextField(blank=True, null=True)
    apellidos_estudiantes = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    whatsapp_estudiante = models.IntegerField(blank=True, null=True)
    nombres_representante = models.TextField(blank=True, null=True)
    apellidos_representante = models.TextField(blank=True, null=True)
    whatsapp_responsable = models.IntegerField(blank=True, null=True)
    email_representante = models.TextField(blank=True, null=True)
    inscrito = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        db_table = 'estudiantes_tabla'


class Modulos(models.Model):
    id_mol = models.TextField(primary_key=True, null=False, blank=True, db_column='id_mol')
    nombre = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'modulos'


class QuizTabla(models.Model):
    id_pregunta = models.TextField(primary_key=True, blank=True, null=False, db_column='id_pregunta')
    id_mol = models.ForeignKey(Modulos, on_delete=models.CASCADE, db_column='id_mol')
    quiz = models.IntegerField(blank=True, null=True)
    seccion = models.IntegerField(blank=True, null=True)
    titulo_de_seccion = models.TextField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    tipo_de_pregunta = models.TextField(blank=True, null=True)
    pregunta = models.TextField(blank=True, null=True)
    respuesta_correcta = models.TextField(blank=True, null=True)
    respuesta_incorrecta_1 = models.TextField(blank=True, null=True)
    respuesta_incorrecta_2 = models.TextField(blank=True, null=True)
    respuesta_incorrecta_3 = models.TextField(blank=True, null=True)
    respuesta_incorrecta_4 = models.TextField(blank=True, null=True)
    explicacion_de_la_respueta_correcta = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'quiz_tabla'


class MonitorTabla(models.Model):
    uuid_cole = models.ForeignKey(ColeTabla, on_delete=models.CASCADE, db_column='uuid_cole')
    uuid_mont = models.TextField(primary_key=True, null=False, blank=True, db_column='uuid_mont')
    monitor = models.TextField(blank=True, null=True)  
    materia_feme = models.TextField(blank=True, null=True)  
    field_puntaje = models.FloatField(db_column='per_puntaje', blank=True, null=True)  
    whatsapp = models.FloatField(blank=True, null=True)  
    email_m = models.TextField(blank=True, null=True)  
    id_thinki_mon = models.FloatField(blank=True, null=True)
    key = models.CharField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'monitor_tabla'


class SalonTabla(models.Model):
    uuid_salon = models.TextField(primary_key=True, null=False, blank=True)
    id_monitor = models.ForeignKey(MonitorTabla, on_delete=models.CASCADE, db_column='uuid_mont')
    cierre_definitivo = models.TextField(db_column='Cierre definitivo', blank=True, null=True)  
    l3_22_23 = models.TextField(db_column='l3-22-23', blank=True, null=True)  
    l3_22_23_2 = models.TextField(db_column='l3-22-23_2', blank=True, null=True)  
    l3_22_23_au = models.TextField(db_column='l3-22-23_au', blank=True, null=True)  

    class Meta:
        db_table = 'salon_tabla'


class SalonKpiModulo(models.Model):
    uuid_salon = models.ForeignKey(SalonTabla, on_delete=models.CASCADE, db_column='uuid_salon')
    id_mol = models.ForeignKey(Modulos, on_delete=models.CASCADE, db_column='id_mol')
    grado = models.TextField(blank=True, null=True)
    seccion = models.TextField(blank=True, null=True)
    modulos = models.TextField(blank=True, null=True) 
    total_estudiantes = models.IntegerField(blank=True, null=True)
    iniciaron = models.IntegerField(blank=True, null=True)
    llevan50 = models.IntegerField(blank=True, null=True, db_column='llevan_50')
    completaron = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'salon_kpi_modulo'


class Estatus(models.Model):
    id_thinkific = models.ForeignKey(EstudiantesTabla, on_delete=models.CASCADE, db_column='id_thinkific')
    modulo = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True, db_column='email')
    started_at = models.DateTimeField()
    activated_at = models.DateTimeField()
    expirated_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    per_completation = models.IntegerField(blank=True, null=True)
    per_videos = models.IntegerField(blank=True, null=True)
    estatus = models.TextField(blank=True, null=True, db_column='estatus')
    created_at = models.DateTimeField()
    last_sign_in = models.DateTimeField()
    nota_quiz1 = models.DecimalField(max_digits=16, decimal_places=2)
    nota_quiz2 = models.DecimalField(max_digits=16, decimal_places=2)
    nota_quiz3 = models.DecimalField(max_digits=16, decimal_places=2)
    fecha_q1 = models.DateTimeField()
    fecha_q2 = models.DateTimeField()
    fecha_q3 = models.DateTimeField()
    nota_quizes = models.DecimalField(max_digits=16, decimal_places=2)
    nota_progreso = models.DecimalField(max_digits=16, decimal_places=2)
    nota_total = models.IntegerField(blank=True, null=True)
    nota_total_l = models.TextField(blank=True, null=True, db_column='nota_total_l')

    class Meta:
        db_table = 'estatus'


class MonitorTablaBeta(models.Model):
    uuid_cole = models.TextField(blank=True, null=True)
    uuid_mont = models.TextField(primary_key=True, null=False, blank=True)
    monitor = models.TextField(blank=True, null=True)  
    materia_feme = models.TextField(blank=True, null=True)  
    field_puntaje = models.FloatField(db_column='per_puntaje', blank=True, null=True)  
    whatsapp = models.FloatField(blank=True, null=True)  
    email_m = models.TextField(blank=True, null=True)  
    id_thinki_mon = models.FloatField(blank=True, null=True)  

    class Meta:
        db_table = 'monitor_tabla_beta'


class SalonTablaBeta(models.Model):
    uuid_salon = models.TextField(primary_key=True, null=False, blank=True)
    id_monitor = models.ForeignKey(MonitorTablaBeta, on_delete=models.CASCADE, db_column='uuid_mont')
    cierre_definitivo = models.TextField(db_column='Cierre definitivo', blank=True, null=True)  
    l3_22_23 = models.TextField(db_column='l3-22-23', blank=True, null=True)  
    l3_22_23_2 = models.TextField(db_column='l3-22-23_2', blank=True, null=True)  
    l3_22_23_au = models.TextField(db_column='l3-22-23_au', blank=True, null=True)  

    class Meta:
        db_table = 'salon_tabla_beta'
