from django.db import models
import uuid

rango_edades = (
    ('', 'Seleccione su rango de edad'),
    ('0', '18 a 25'),
    ('1', '26 a 33'),
    ('2', '34 a 40'),
    ('3', '40+'),
)

sexo = (
    ('', 'Seleccione horientación sexual'),
    ('0', 'Hombre'),
    ('1', 'Mujer'),
    ('2', 'Otro'),
)

red_social = (
    ('', 'Seleccione red social favorita'),
    ('0', 'Facebook'),
    ('1', 'WhatsApp'),
    ('2', 'Twitter'),
    ('3', 'Instagram'),
    ('4', 'Tiktok'),
    ('5', 'Otro'),
)

tiempo = (
    ('', 'Seleccione promedio al día'),
    ('0', '1 hr'),
    ('1', '3 hrs'),
    ('2', '5hrs'),
    ('3', '6+ hrs'),
)


class Employee(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    Correo = models.EmailField()
    Edad = models.CharField(max_length=1, choices=rango_edades)
    Sexo = models.CharField(max_length=1, choices=sexo)
    Social = models.CharField(max_length=1, choices=red_social)
    Facebook = models.CharField(max_length=1, choices=tiempo)
    WhatsApp = models.CharField(max_length=1, choices=tiempo)
    Twitter = models.CharField(max_length=1, choices=tiempo)
    Instagram = models.CharField(max_length=1, choices=tiempo)
    Tiktok = models.CharField(max_length=1, choices=tiempo)

    # image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.Correo

    # @property
    # def imageURL(self):
    #     try:
    #         url = 'self.image.url'
    #     except:
    #         url = ''

    #     return url
