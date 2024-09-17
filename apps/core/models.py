from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия", blank=True, null=True)
    email = models.EmailField(verbose_name="Почта", blank=True, null=True)
    phone_number = models.CharField(max_length=255, verbose_name="Номер телефона", unique=True)
    password = models.CharField(max_length=255, verbose_name="Пароль")
    profile_photo = models.ImageField(upload_to="Фото профиля", verbose_name="Фото профиля", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Аддрес доставки товаров", blank=True, null=True)
    type_of_customer = models.BooleanField(verbose_name="Вид покупателя оптом", default=False)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    is_staff = models.BooleanField(default=False, verbose_name="Админ")

    groups = models.ManyToManyField(
        Group,
        verbose_name="Группы",
        blank=True,
        related_name="customuser_set"  # Уникальное имя для предотвращения конфликта
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="Разрешения",
        blank=True,
        related_name="customuser_permissions_set"  # Уникальное имя для предотвращения конфликта
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return f'{self.name} {self.phone_number} {self.address}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class TypeOfPrice(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип цены')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Тип цены"
        verbose_name_plural = "Типы цен"
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Наименование')
    articul = models.CharField(max_length=255, verbose_name='Артикул', unique=True)
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Кол-во')
    type_of_price = models.ForeignKey(TypeOfPrice, on_delete=models.CASCADE, verbose_name='Тип цены')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='ProductsImages', verbose_name='Изображение продукта')

    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продукта'