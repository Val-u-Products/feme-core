from django.db import models


class ColeTabla(models.Model):
    uuid_cole = models.TextField(blank=True, null=True)
    colegio = models.TextField(db_column='Colegio', blank=True, null=True) 
    pais = models.TextField(db_column='País', blank=True, null=True)  
    ubicacion = models.TextField(db_column='Ubicacion', blank=True, null=True)  
    zona_horaria = models.TextField(db_column='Zona Horaria', blank=True, null=True)  
    sexo_colegio = models.TextField(db_column='Sexo-Colegio', blank=True, null=True)  
    tipo_de_inscripcion_actual = models.TextField(db_column='Tipo de Inscripcion Actual', blank=True, null=True)  
    tipo_de_inscripcion_historico = models.TextField(db_column='Tipo de Inscripcion historico', blank=True, null=True)  
    zoho_link_field = models.TextField(db_column='Zoho Link ', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'cole_tabla'


class DfSalonKpi(models.Model):
    colegio = models.TextField(db_column='Colegio', blank=True, null=True)  
    id_monitor = models.TextField(db_column='ID_Monitor', blank=True, null=True)  
    monitor = models.TextField(db_column='Monitor', blank=True, null=True)  
    apellido_monitor = models.TextField(db_column='Apellido Monitor', blank=True, null=True)  
    grado = models.TextField(db_column='Grado', blank=True, null=True) 
    seccion = models.TextField(db_column='Sección', blank=True, null=True)  
    materia_feme = models.TextField(db_column='Materia FEME', blank=True, null=True)  
    zoho_link = models.TextField(db_column='Zoho Link', blank=True, null=True)  
    modulos = models.TextField(db_column='Modulos', blank=True, null=True)  
    salon_mol = models.TextField(db_column='Salon_Mol', blank=True, null=True) 
    id_salon = models.TextField(db_column='ID_Salon', blank=True, null=True)  
    inscripcion_correcto_t_l3 = models.BigIntegerField(db_column='Inscripcion_correcto_T_L3', blank=True, null=True)  
    id_mol = models.TextField(db_column='ID_Mol', blank=True, null=True)  
    uuid_salon = models.TextField(blank=True, null=True)
    total_estudiantes = models.BigIntegerField(db_column='Total estudiantes', blank=True, null=True)  
    iniciaron = models.BigIntegerField(db_column='Iniciaron', blank=True, null=True)  
    llevan_50_field = models.BigIntegerField(db_column='Llevan +50%', blank=True, null=True)  
    completaron = models.BigIntegerField(db_column='Completaron', blank=True, null=True) 
    fecha_insc = models.TextField(db_column='Fecha_Insc', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'df_salon_kpi'


class EstudiantesTabla(models.Model):
    id_thinki = models.FloatField(db_column='ID_thinki', blank=True, null=True)  
    uuid_salon = models.TextField(blank=True, null=True)
    uuid_mont = models.TextField(blank=True, null=True)
    colegio = models.TextField(db_column='Colegio', blank=True, null=True)  
    grado = models.TextField(db_column='Grado', blank=True, null=True)  
    sección = models.TextField(db_column='Sección', blank=True, null=True) 
    nombres_estudiantes = models.TextField(db_column='Nombres estudiantes', blank=True, null=True)  
    apellidos_estudiantes = models.TextField(db_column='Apellidos estudiantes', blank=True, null=True)  
    email = models.TextField(db_column='Email', blank=True, null=True)  
    whatsapp_estudiante = models.FloatField(db_column='WhatsApp estudiante', blank=True, null=True)  
    nombres_representante = models.TextField(db_column='Nombres representante', blank=True, null=True)  
    apellidos_representante = models.TextField(db_column='Apellidos representante', blank=True, null=True)  
    whatsapp_responsable = models.FloatField(db_column='WhatsApp responsable', blank=True, null=True)  
    email_representante = models.TextField(db_column='Email representante', blank=True, null=True)  
    inscrito = models.TextField(db_column='Inscrito', blank=True, null=True)  
    id_monitor = models.TextField(db_column='ID_Monitor', blank=True, null=True)  
    lapsos_de_inscripcion_21 = models.TextField(db_column='Lapsos de Inscripcion_21', blank=True, null=True)  
    lapsos_de_inscripcion_22 = models.TextField(db_column='Lapsos de Inscripcion_22', blank=True, null=True)  
    q_de_inscripcion_21 = models.TextField(db_column='Q de Inscripcion_21', blank=True, null=True)  
    q_de_inscripcion_22 = models.TextField(db_column='Q de Inscripcion_22', blank=True, null=True)  
    q_de_inscripcion_23 = models.TextField(db_column='Q de Inscripcion_23', blank=True, null=True) 
    sexo = models.TextField(db_column='Sexo', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'estudiantes_tabla'


class MonitorTabla(models.Model):
    uuid_mont = models.TextField(blank=True, null=True)
    monitor = models.TextField(db_column='Monitor', blank=True, null=True)  
    apellido_monitor = models.TextField(db_column='Apellido Monitor', blank=True, null=True)  
    materia_feme = models.TextField(db_column='Materia FEME', blank=True, null=True)  
    field_puntaje = models.FloatField(db_column='% Puntaje', blank=True, null=True)  
    whatsapp = models.FloatField(db_column='Whatsapp', blank=True, null=True)  
    email_m = models.TextField(db_column='Email_M', blank=True, null=True)  
    id_thinki_mon = models.FloatField(db_column='ID_thinki_Mon', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'monitor_tabla'


class SalonTabla(models.Model):
    uuid_salon = models.TextField(blank=True, null=True)
    id_monitor = models.TextField(db_column='ID_Monitor', blank=True, null=True)  
    cierre_1 = models.DateTimeField(db_column='Cierre 1', blank=True, null=True)  
    cierre_2 = models.DateTimeField(db_column='Cierre 2', blank=True, null=True)  
    cierre_3 = models.DateTimeField(db_column='Cierre 3', blank=True, null=True)  
    cierre_definitivo = models.TextField(db_column='Cierre definitivo', blank=True, null=True)  
    l1_22_23 = models.TextField(db_column='L1-22-23', blank=True, null=True)  
    l1_22_23_2 = models.TextField(db_column='L1-22-23_2', blank=True, null=True)  
    l1_22_23_au = models.TextField(db_column='L1-22-23_AU', blank=True, null=True)  
    l2_22_23 = models.TextField(db_column='L2-22-23', blank=True, null=True)  
    l2_22_23_2 = models.TextField(db_column='L2-22-23_2', blank=True, null=True)  
    l2_22_23_au = models.TextField(db_column='L2-22-23_AU', blank=True, null=True)  
    l2_22_23_au_2 = models.TextField(db_column='L2-22-23_AU_2', blank=True, null=True)  
    l3_22_23 = models.TextField(db_column='L3-22-23', blank=True, null=True)  
    l3_22_23_2 = models.TextField(db_column='L3-22-23_2', blank=True, null=True)  
    l3_22_23_au = models.TextField(db_column='L3-22-23_AU', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'salon_tabla'
