from django.db import models
from expert.models import Experto  


class Brigada(models.Model):
    brigada_id = models.AutoField(primary_key=True, db_column='brigada_id')
    investigacion_id = models.IntegerField(db_column='investigacion_id')
    
    class Meta:
        managed = False  
        db_table = 'brigada'
        #get_latest_by = 'brigada_id'


class BrigadaExperto(models.Model):
    brigada_experto_id = models.AutoField(primary_key=True)
    brigada = models.ForeignKey(Brigada, on_delete=models.CASCADE, db_column='brigada_id')
    experto_cc = models.IntegerField(db_column='experto_cc')  
    
    class Meta:
        managed = False 
        db_table = 'brigada_experto'
