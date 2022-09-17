from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, \
    BaseUserManager
from Products.models import Product


class MyUserManager(BaseUserManager):
    def create_user(self, email, full_name, phone_number, password):
        if not email:
            raise ValueError('users must have Email')
        if not full_name:
            raise ValueError('users must have Full Name')

        user = self.model(email=self.normalize_email(email),
                          phone_number=phone_number, full_name=full_name)
        user.set_password(password)
        # user.save(using=self._db)
        user.save()
        return user

    def create_superuser(self, email, full_name, phone_number, password,
                         **other_fields):
        user = self.create_user(email, full_name, phone_number, password)
        user.is_admin = True
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        user.save(using=self._db)
        return


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_superuser(self):
        """Is the user a member of is_superuser?"""
        # Simplest possible answer: All admins are is_superuser
        return self.is_admin


class Wallet(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    wallet_balance = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )


class Cart(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    # products = models.ManyToOneRel(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Shop(models.Model):
    seller_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(
        default=False,
        null=False,
        blank=False,
        max_length=150,
    )
    shop_id = models.IntegerField(
        default=False,
        null=False,
        blank=False,
        unique=True
    )
    logo = models.ImageField(
        upload_to='seller/logo_shop'
    )
