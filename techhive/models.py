from django.db import models

class TechHiveDeparments(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department_name
    
