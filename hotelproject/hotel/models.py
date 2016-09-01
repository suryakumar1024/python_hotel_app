from django.db import models

# Create your models here.


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    opening_time = models.TimeField(auto_now_add=False, blank=True)
    closing_time = models.TimeField(auto_now_add=False, blank=True)

    def get_timing(self):
        return self.opening_time.strftime('%I%p') + "-" + self.closing_time.strftime('%I%p')

    # def get_menus(self):
    #     menu_obj = Menu.objects.get(fk=self.id)
    #     return


class Menu(models.Model):
    hotel = models.ForeignKey(Hotel)
    item_one = models.CharField(max_length=100,default='none')
    item_two = models.CharField(max_length=100, default='none')
