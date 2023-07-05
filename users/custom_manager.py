from django.contrib.auth.base_user import BaseUserManager



class CustomUserManager(BaseUserManager):

    def create_superuser(self, email: str = None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError("is_active must be set to true")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("is_superuser must be set to true")

        if not email:
            raise ValueError("Email is required")


        email = self.normalize_email(email)      
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user


    def create_user(self, email, password, **extra_fileds):
        
        if not email:
            raise ValueError("Email Required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fileds)

        user.set_password(password)
        user.save()
        return user


