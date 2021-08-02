from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import SET_NULL
from django.db.models.signals import post_save, pre_save




# Создали пользователя по классу AbstractUser
class User(AbstractUser):
	pass



#! Пробная штука
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

	def __str__(self):
			return self.user.username

#! До сюда. Также смотри в class Operators

class Admins(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	login = models.CharField(max_length=45)
	password = models.CharField(max_length=200)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = 'Админ'
		verbose_name_plural = 'Админы'


class Modems(models.Model):
	name = models.CharField(max_length=45)
	model = models.ForeignKey('ModemType', null=True, blank=True, on_delete=models.SET_NULL)
	serial = models.CharField(max_length=45, null=True, blank=True)
	mac = models.CharField(max_length=45, null=True, blank=True)
	id_ipgroup = models.ForeignKey('IpGroups', null=True, blank=True, on_delete=models.SET_NULL)
	ip = models.CharField(max_length=100, null=True, blank=True)
	mask = models.IntegerField(null=True, blank=True)
	desc = models.CharField(max_length=250, null=True, blank=True)
	satellite = models.ForeignKey('Satellite', null=True, blank=True, on_delete=models.SET_NULL)
	buc = models.ForeignKey('Buc', null=True, blank=True, on_delete=models.SET_NULL)
	antenna = models.ForeignKey('Antenna', null=True, blank=True, on_delete=models.SET_NULL)
	status = models.ForeignKey('ModemStatus', null=True, blank=True, on_delete=models.SET_NULL)
	serial_buc = models.CharField(max_length=45, null=True, blank=True)
	owner = models.ForeignKey('ModemOwner', null=True, blank=True, on_delete=models.SET_NULL)
	date_update = models.CharField(max_length=40, blank=True, null=True)
	# date_update = models.DateField(default=date.today, null=True, blank=True)
	id_author_update = models.ForeignKey(Admins, null=True, blank=True, on_delete=models.SET_NULL)
	file = models.CharField(max_length=1000, null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Модем'
		verbose_name_plural = 'Модемы'


class ModemsComments(models.Model):
	id_model = models.ForeignKey(Modems, null=True, blank=True, on_delete=models.SET_NULL)
	# data = models.DateField(null=True, blank=True, default=date.today)
	# data = models.IntegerField(null=True, blank=True)
	data = models.DateField(auto_now_add=True, null=True, blank=True)
	datum = models.CharField(max_length=11, null=True, blank=True)
	comment = models.TextField(blank=True, null=True)
	id_author = models.IntegerField(null=True, blank=True)

	class Meta:
		verbose_name = 'Комментарий по модему'
		verbose_name_plural = 'Комментарии по модемам'

	def __str__(self):
		return self.id_model


class ModemOwner(models.Model):
	name = models.CharField(max_length=45)

	class Meta:
		verbose_name = 'Владелец модема'
		verbose_name_plural = 'Владельцы модема'

	def __str__(self):
		return self.name


class ModemStatus(models.Model):
	name = models.CharField(max_length=45)

	class Meta:
		verbose_name = 'Статус модема'
		verbose_name_plural = 'Статус модемов'

	def __str__(self):
		return self.name


class ModemType(models.Model):
	name = models.CharField(max_length=45)

	class Meta:
		verbose_name = 'Тип модема'
		verbose_name_plural = 'Типы модемов'

	def __str__(self):
		return self.name


class Satellite(models.Model):
	name = models.CharField(max_length=256)
	degree = models.IntegerField(null=True)

	class Meta:
		verbose_name = 'Спутник'
		verbose_name_plural = 'Спутники'

	def __str__(self):
		return self.name


class Buc(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'BUC'
		verbose_name_plural = 'BUC'


class Antenna(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тип антенны'
		verbose_name_plural = 'Типы антенн'


class Operator(models.Model):
	fullname = models.CharField(max_length=256)
	host = models.CharField(max_length=128)
	login = models.CharField(max_length=40)
	password = models.CharField(max_length=50)
	nds = models.IntegerField(null=True)
	proc = models.IntegerField(null=True)
	rod = models.CharField(max_length=256, null=True)
	sogl = models.DateField(auto_now_add=False, default=date.today, null=True)
	sogl_date = models.DateField(auto_now_add=False, default=date.today, null=True)
	name = models.CharField(max_length=256, null=True)
	name_podp = models.CharField(max_length=256, null=True)
	inn = models.CharField(max_length=256, null=True)
	proc_case = models.TextField(null=True)
	kpp = models.CharField(max_length=256, null=True)
	id_parent = models.IntegerField(null=True)
	tel = models.CharField(max_length=128, null=True)
	mail = models.CharField(max_length=128, null=True)
			#! Пробная штука
	organisation = models.ForeignKey('UserProfile', on_delete=SET_NULL, null=True)
			#! До сюда
	class Meta:
		verbose_name = 'Оператор'
		verbose_name_plural = 'Операторы'



	def __str__(self):
		return str(self.fullname)



class Service(models.Model):
	name = models.CharField(max_length=100)
	speed = models.CharField(max_length=20, null=True, blank=True)
	p_speed = models.CharField(max_length=20, null=True, blank=True)
	limit = models.BigIntegerField(null=True, blank=True)
	price = models.IntegerField(null=True, blank=True)
	work_name = models.CharField(max_length=100, null=True, blank=True)
	rate_limit = models.CharField(max_length=30, null=True, blank=True)
	burst_rate = models.CharField(max_length=30, null=True, blank=True)
	burst_threshold = models.CharField(max_length=30, null=True, blank=True)
	burst_time = models.CharField(max_length=30, null=True, blank=True)
	uptime_limit = models.CharField(max_length=30, null=True, blank=True)
	uptime_used = models.CharField(max_length=30, null=True, blank=True)
	desc = models.TextField(null=True, blank=True)
	limit2 = models.BigIntegerField(null=True, blank=True)
	sort = models.IntegerField(null=True, blank=True)
	connect_disabled = models.IntegerField(null=True, blank=True)
	time_limit = models.IntegerField(null=True, blank=True)
	type = models.CharField(max_length=30, default='default', blank=True)
	sname_second = models.CharField(max_length=100, null=True, blank=True)
	sname_third = models.CharField(max_length=100, null=True, blank=True)
	active = models.BigIntegerField(null=True, blank=True)
	turbo_show = models.IntegerField(null=True, blank=True)
	fap_id = models.IntegerField(null=True, blank=True)
	hidden = models.IntegerField(null=True, blank=True)
	dops = models.CharField(max_length=100, null=True, blank=True)
	discount = models.IntegerField(null=True, blank=True)
	parent_id = models.IntegerField(null=True, blank=True)
	lft = models.IntegerField(null=True, blank=True)
	rgt = models.IntegerField(null=True, blank=True)
	depth = models.IntegerField(null=True, blank=True)

	class Meta:
		verbose_name = 'Тариф'
		verbose_name_plural = 'Тарифы'

	def __str__(self):
		return str(self.name)


class Hotspots(models.Model):
	name = models.CharField(max_length=100)
	ip = models.CharField(max_length=64)

	class Meta:
		verbose_name = 'Hotspot'
		verbose_name_plural = 'Hotspots'

	def __str__(self):
		return str(self.name)


class ChannelID(models.Model):
	name = models.CharField(max_length=30)
	name_local = models.CharField(max_length=30)
	operator_id = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True)

	class Meta:
		verbose_name = 'Номер канала'
		verbose_name_plural = 'Номера каналов'

	def __str__(self):
		return self.name


class IpGroups(models.Model):
	name = models.CharField(max_length=20)
	ip = models.CharField(max_length=20, null=True)
	mask = models.CharField(max_length=20, null=True)
	router_ip = models.CharField(max_length=20, null=True)
	login = models.CharField(max_length=20, null=True, blank=True)
	password = models.CharField(max_length=20, null=True, blank=True)
	is_def = models.IntegerField(null=True, blank=True)
	id_partner = models.ForeignKey('Partner', on_delete=models.SET_NULL, null=True, blank=True)
	showms = models.IntegerField(default=0, blank=True)
	id_hotspot = models.ForeignKey(Hotspots, on_delete=models.SET_NULL, null=True, blank=True)
	operators = models.CharField(max_length=50, null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	gmt = models.IntegerField(null=True)
	channel_id = models.ForeignKey(ChannelID, null=True, on_delete=models.SET_NULL, blank=True)

	class Meta:
		verbose_name = 'IP-группа'
		verbose_name_plural = 'IP-группы'

	def __str__(self):
		return self.name


class Partner(models.Model):
	fullname = models.CharField(max_length=256)
	host = models.CharField(max_length=128, null=True, blank=True)
	login = models.CharField(max_length=40, null=True)
	password = models.CharField(max_length=50, null=True)
	nds = models.IntegerField(default=0, null=True, blank=True)
	proc = models.IntegerField(null=True, blank=True)
	rod = models.CharField(max_length=256, null=True, blank=True)
	sogl = models.DateField(auto_now_add=False, default=date.today, null=True, blank=True)
	sogl_date = models.DateField(auto_now_add=False, default=date.today, null=True, blank=True)
	name = models.CharField(max_length=256, null=True, blank=True)
	name_podp = models.CharField(max_length=256, null=True, blank=True)
	inn = models.CharField(max_length=256, null=True, blank=True)
	proc_case = models.TextField(null=True, blank=True)
	kpp = models.CharField(max_length=256, null=True, blank=True)
	id_parent = models.IntegerField(null=True, blank=True)
	tel = models.CharField(max_length=128, null=True, blank=True)
	mail = models.CharField(max_length=128, null=True, blank=True)
	remember_token = models.CharField(max_length=100, null=True, blank=True)

	class Meta:
		verbose_name = 'Партнер'
		verbose_name_plural = 'Партнеры'

	def __str__(self):
		return self.fullname


class DeliveryAddress(models.Model):
	partner_id = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True)
	postal_code = models.IntegerField(null=True, blank=True)
	region = models.CharField(max_length=45, null=True, blank=True)
	city = models.CharField(max_length=45, null=True, blank=True)
	street = models.CharField(max_length=45, null=True, blank=True)
	house = models.CharField(max_length=45, null=True, blank=True)
	flat = models.CharField(max_length=45, null=True, blank=True)
	geo = models.CharField(max_length=45, null=True, blank=True)
	tel = models.CharField(max_length=45, null=True, blank=True)
	fio = models.CharField(max_length=45, null=True, blank=True)
	address = models.CharField(max_length=248, null=True, blank=True)
	default = models.IntegerField(null=True, blank=True)

	class Meta:
		verbose_name = 'Адрес доставки'
		verbose_name_plural = 'Адреса доставки'

	def __str__(self):
		return self.address


#! Пробная штука

def post_user_created_signal(sender, instance, created, **kwargs):
	print(instance, created)
	if created:
		UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
#! До сюда

#
# class Users(models.Model):
#     login = models.CharField(max_length=255, null=True)
#     password = models.CharField(max_length=255, default='')
#     password_service = models.CharField(max_length=255, default='')
#     create_date = models.IntegerField(null=True)
#     last_change_date = models.IntegerField(null=True)
#     who_create = models.IntegerField(null=True)
#     who_change = models.IntegerField(null=True)
#     is_juridical = models.BooleanField(default=0, null=True)  # null=True
#     full_name = models.CharField(max_length=255, null=True)
#     juridical_address = models.CharField(max_length=255, null=True)
#     act_address = models.CharField(max_length=255, null=True)
#     work_tel = models.CharField(max_length=56, null=True)
#     home_tel = models.CharField(max_length=56, null=True)
#     mob_tel = models.CharField(max_length=56, null=True)
#     web_page = models.CharField(max_length=250, null=True)
#     icq_number = models.IntegerField(30, null=True)
#     tax_number = models.IntegerField(30, null=True)
#     email = models.EmailField(max_length=255, null=True)
#     passport = models.CharField(max_length=255, null=True)
#     comments = models.TextField(null=True)
#     connect_date = models.DateField(null=True)
#     balance = models.FloatField(default=0, null=True)
#     balance_bonus = models.FloatField(default=0, null=True)
#     pay_nim = models.FloatField(default=0, null=True)
#     id_grp = models.IntegerField(null=True)
#     new_usr_tarif = models.CharField(max_length=56, default='', null=True)
#     rek = models.CharField(max_length=255, null=True)
#     prc_blnc = models.BooleanField(default=0, null=True)
#     now_day_traffic = models.IntegerField(null=True)
#     now_day_traffic_lastdate = models.IntegerField(null=True)
#     sms_accept_code = models.IntegerField(null=True)
#     sms_accepted = models.BooleanField(default=0, null=True)
#     ppp = models.BooleanField(default=0, null=True)
#     our_comments = models.TextField(null=True)
#     debug = models.BooleanField(default=0, null=True)
#     auto_renew = models.BooleanField(default=0, null=True)
#     auto_renew_stage = models.BooleanField(default=0, null=True)
#     last_traffic_notify = models.IntegerField(default=0, null=True)
#     remember_token = models.CharField(max_length=255, null=True)
#     email_verified_at = models.DateField(null=True)
#     user_status = models.BooleanField(null=True)
#
#     class Meta:
#         verbose_name = 'Абонент'
#         verbose_name_plural = 'Абоненты'
#
#     def __str__(self):
#         return self.login
