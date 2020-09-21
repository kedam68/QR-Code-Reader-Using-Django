from django.db import models
# import numpy as np
# from PIL import Image
# from .utils import convert

# Create your models here.
class QR(models.Model): 
    image = models.ImageField(upload_to='qr/')

    # def __str__(self):
    #     return str(self.id)

    # def save(self, *args, **kwargs):

    #     pil_img = Image.open(self.image)
    #     cv_img = np.array(pil_img)
    #     data = convert(cv_img)
    #     print(data)
