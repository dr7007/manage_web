from django.db import models

from user.models import MyUser

# Create your models here.
class Review(models.Model):
    
    STATUS_TYPE_CHOICES = (
        ('Deleted', 'Deleted'),
        ('Writing', 'Writing'),
        ('Modified', 'Modified'),
        ('Deactivated', 'Deactivated'),
        ('StandBy', 'StandBy'),
        ('Approved', 'Approved'),
    )
    status = models.CharField(max_length=11, choices=STATUS_TYPE_CHOICES)
    register_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    restaurant =  models.ForeignKey('Restaurant', null=True, on_delete=models.SET_NULL)

    REVIEW_TYPE_CHOICES = (
        ('RSTRT','Restaurant'),
        ('BAR','Bar'),
    )
    reviewer = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)
    review_type = models.CharField(max_length=5, choices=REVIEW_TYPE_CHOICES)
    visit_date = models.DateField(auto_now=False, auto_now_add=False)

    rstrt_overview = models.CharField(max_length=500)
    rstrt_atmosphere = models.CharField(max_length=500)
    comment = models.CharField(max_length=500)

    taste_score = models.PositiveSmallIntegerField()
    taste_summary = models.CharField(max_length=45)
    atmosphere_score = models.PositiveSmallIntegerField()
    atmosphere_summary = models.CharField(max_length=45)
    efficiency_score = models.PositiveIntegerField()
    efficiency_summary =models.CharField(max_length=5)
    summary = models.CharField(max_length=40)


class Menu(models.Model):
    MENU_TYPE_CHOICES = (
        ('GM', 'General Menu'),
        ('SM', 'Set Menu'),
        ('CM', 'Course Menu'),
        ('BM', 'Buffet Menu'),
    )
    PRICE_TYPE_CHOICES = (
        ('General', 'General'),
        ('Portion', 'Portion'),
        ('Size', 'Size'),
    )
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    menu_type = models.CharField(max_length=2, choices=MENU_TYPE_CHOICES)
    name = models.CharField(max_length=50)
    menu_review = models.CharField(max_length=500)
    price_type = models.CharField(max_length=10, choices=PRICE_TYPE_CHOICES)
    price_unit = models.CharField(max_length=10)
    price = models.PositiveIntegerField()
    star_rating = models.PositiveSmallIntegerField()


class Food(models.Model):
    
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    review = models.CharField(max_length=500)


class Restaurant(models.Model):
    
    STATUS_TYPE_CHOICES = (
        ('c_Conflict', 'c_Conflict'),
        ('c_Approved', 'c_Approved'),
        ('p_Disapproved', 'p_Disapproved'),
        ('p_Standby', 'p_Standby'),
        ('p_Approved', 'p_Approved'),
    
    )
    
    key = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=30)
    floor = models.PositiveSmallIntegerField()
    possible_review_type = models.CharField(max_length=3)
    status = models.CharField(max_length=13, choices=STATUS_TYPE_CHOICES)
    register_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    info_register_info = models.DateTimeField(auto_now=False, auto_now_add=False)
    rstrt_detail_info = models.OneToOneField('RSTRT_Detail_INFO', on_delete=models.CASCADE)
    sales_info = models.OneToOneField('Sales_INFO', on_delete=models.CASCADE)
    category_info = models.OneToOneField('Category_INFO', on_delete=models.CASCADE)
    
    building = models.ForeignKey('Building', on_delete=models.PROTECT)

    is_active = models.BooleanField()
    active_id = models.OneToOneField('self', blank=True, on_delete=models.PROTECT)



class RSTRT_Detail_INFO(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('G', 'Grand'),
    )
    CLEANLIESS_CHOICES = (
        ('High', 'High'),
        ('Mid', 'Mid'),
        ('Low', 'Low'),
    )
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    is_multiple = models.BooleanField()
    is_room = models.BooleanField()
    is_self_service = models.BooleanField()
    is_bar_table = models.BooleanField()
    restroom = models.BooleanField()
    restroom_cleanliess = models.CharField(max_length=4, choices=CLEANLIESS_CHOICES)
    
    
    
class Sales_INFO(models.Model):
    
    STATUS_TYPE_CHOICES=(
        ('Standby', 'Standby'),
        ('Approved', 'Approved'),
    )
    status = models.CharField(max_length=8, choices=STATUS_TYPE_CHOICES)
    
    phone_number_1 = models.CharField(max_length=15, blank=True)
    phone_number_2 = models.CharField(max_length=15, blank=True)
    days_off = models.CharField(max_length=7)
    days_24h = models.CharField(max_length=7)
    business_hour = models.OneToOneField('Business_Hour', on_delete=models.CASCADE)
    last_order = models.OneToOneField('Last_Order', on_delete=models.CASCADE)
    break_time = models.OneToOneField('Break_Time', on_delete=models.CASCADE)

    PARKING_LOT_CHOICES = (
        ('Inside', 'Inside'),
        ('Outside', 'Outside'),
        ('None', 'None'),
    )
    is_group_reservation = models.BooleanField()
    group_reservation_maximum = models.PositiveSmallIntegerField()
    parking_lot = models.CharField(max_length=7, choices=PARKING_LOT_CHOICES)
    parking_lot_info = models.CharField(max_length=100)
    is_valet_parking = models.BooleanField()
    valet_parking_price = models.CharField(max_length=100)
    is_package = models.BooleanField()
    is_delivery = models.BooleanField()
    is_corkage = models.BooleanField()
    corkage_price = models.CharField(max_length=100)



class Business_Hour(models.Model):
    mon_start = models.TimeField(auto_now=False, auto_now_add=False)
    mon_end = models.TimeField(auto_now=False, auto_now_add=False)
    tue_start = models.TimeField(auto_now=False, auto_now_add=False)
    tue_end = models.TimeField(auto_now=False, auto_now_add=False)
    wed_start = models.TimeField(auto_now=False, auto_now_add=False)
    wed_end = models.TimeField(auto_now=False, auto_now_add=False)
    thu_start = models.TimeField(auto_now=False, auto_now_add=False)
    thu_end = models.TimeField(auto_now=False, auto_now_add=False)
    fri_start = models.TimeField(auto_now=False, auto_now_add=False)
    fri_end = models.TimeField(auto_now=False, auto_now_add=False)
    sat_start = models.TimeField(auto_now=False, auto_now_add=False)
    sat_end = models.TimeField(auto_now=False, auto_now_add=False)
    sun_start = models.TimeField(auto_now=False, auto_now_add=False)
    sun_end = models.TimeField(auto_now=False, auto_now_add=False)

class Last_Order(models.Model):
    mon_end = models.TimeField(auto_now=False, auto_now_add=False)
    tue_end = models.TimeField(auto_now=False, auto_now_add=False)
    wed_end = models.TimeField(auto_now=False, auto_now_add=False)
    thu_end = models.TimeField(auto_now=False, auto_now_add=False)
    fri_end = models.TimeField(auto_now=False, auto_now_add=False)
    sat_end = models.TimeField(auto_now=False, auto_now_add=False)
    sun_end = models.TimeField(auto_now=False, auto_now_add=False)

class Break_Time(models.Model):
    mon_start = models.TimeField(auto_now=False, auto_now_add=False)
    mon_end = models.TimeField(auto_now=False, auto_now_add=False)
    tue_start = models.TimeField(auto_now=False, auto_now_add=False)
    tue_end = models.TimeField(auto_now=False, auto_now_add=False)
    wed_start = models.TimeField(auto_now=False, auto_now_add=False)
    wed_end = models.TimeField(auto_now=False, auto_now_add=False)
    thu_start = models.TimeField(auto_now=False, auto_now_add=False)
    thu_end = models.TimeField(auto_now=False, auto_now_add=False)
    fri_start = models.TimeField(auto_now=False, auto_now_add=False)
    fri_end = models.TimeField(auto_now=False, auto_now_add=False)
    sat_start = models.TimeField(auto_now=False, auto_now_add=False)
    sat_end = models.TimeField(auto_now=False, auto_now_add=False)
    sun_start = models.TimeField(auto_now=False, auto_now_add=False)
    sun_end = models.TimeField(auto_now=False, auto_now_add=False)


class Category_INFO(models.Model):
    large_category = models.OneToOneField('Large_Category', on_delete=models.CASCADE)
    small_category = models.OneToOneField('Small_Category', on_delete=models.CASCADE)
    
    PRICE_RANGE_TYPE_CHOICES = (
        ('General', 'General'),
        ('Portion', 'Portion'),
        ('Size', 'Size'),
    )
    price_range_type = models.CharField(max_length=10, choices=PRICE_RANGE_TYPE_CHOICES)
    price_range_unit = models.CharField(max_length=10)
    price_range = models.PositiveIntegerField()


class Large_Category(models.Model):
    name = models.CharField(max_length=10)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Small_Category(models.Model):
    name = models.CharField(max_length=10)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Building(models.Model):
    address = models.CharField(max_length=50)
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()


class RSTRT_Feedback(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    editor = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=False, auto_now_add=False)

    information = models.CharField(max_length=800)
    menu_pic = models.CharField(max_length=800)
    rstrt_pic = models.CharField(max_length=800)


class Review_Feedback(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    editor = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=False, auto_now_add=False)

    rstrt_overview = models.CharField(max_length=800)
    rstrt_atmosphere = models.CharField(max_length=800)
    comment = models.CharField(max_length=800)

    taste = models.CharField(max_length=300)
    atmosphere = models.CharField(max_length=300)
    efficiency = models.CharField(max_length=300)
    summary = models.CharField(max_length=300)


class Menu_Feedback(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    editor = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=False, auto_now_add=False)

    menu_fb = models.CharField(max_length=500)
    menu_pic = models.CharField(max_length=500)
