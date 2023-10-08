# Generated by Django 3.2 on 2023-10-08 14:20

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(help_text='Укажите никнейм пользователя', max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+\\Z', 'Поддерживаемые знаки.'), django.core.validators.RegexValidator('[^m][^e]', 'Имя пользователя не может быть "me".')], verbose_name='Никнейм пользователя')),
                ('email', models.EmailField(help_text='Укажите e-mail пользователя', max_length=254, unique=True, verbose_name='E-mail пользователя')),
                ('role', models.CharField(blank=True, choices=[('user', 'user'), ('admin', 'admin'), ('moderator', 'moderator')], default='user', help_text='Укажите роль пользователя', max_length=64, verbose_name='Роль пользователя')),
                ('bio', models.TextField(blank=True, help_text='Укажите биографию пользователя', verbose_name='Биография пользователя')),
                ('first_name', models.CharField(blank=True, help_text='Укажите имя пользователя', max_length=150, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(blank=True, help_text='Укажите фамилия пользователя', max_length=150, verbose_name='Фамилия пользователя')),
                ('confirmation_code', models.CharField(default='XXXX', help_text='Укажите код подтверждения пользователя', max_length=64, null=True, verbose_name='Код подтверждения пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('id',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Укажите тип произведения', max_length=256, verbose_name='Тип произведения')),
                ('slug', models.SlugField(help_text='Укажите Тег категории', unique=True, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Укажите жанр произведения', max_length=256, verbose_name='Жанр произведения')),
                ('slug', models.SlugField(help_text='Укажите Тег жанра', unique=True, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Укажите название произведения', max_length=256, verbose_name='Название произведения')),
                ('year', models.IntegerField(help_text='Укажите год выпуска произведения', verbose_name='Год издания')),
                ('description', models.TextField(blank=True, help_text='Добавьте описание к произведению', verbose_name='Описание произведения')),
                ('category', models.ForeignKey(help_text='Укажите тип произведения', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.category', verbose_name='Тип произведения')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='TitleGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(help_text='Укажите жанр к произведению', on_delete=django.db.models.deletion.CASCADE, related_name='titlegenres', to='reviews.genre', verbose_name='Жанр произведения')),
                ('title', models.ForeignKey(help_text='Укажите название произведения', on_delete=django.db.models.deletion.CASCADE, related_name='titlegenres', to='reviews.title', verbose_name='Название произведения')),
            ],
            options={
                'verbose_name': 'Произведение - Жанр',
                'verbose_name_plural': 'Произведение - Жанр',
            },
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='titles', through='reviews.TitleGenre', to='reviews.Genre', verbose_name='Жанр произведения'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Добавьте описание отзыва', verbose_name='Текст отзыва')),
                ('score', models.PositiveSmallIntegerField(help_text='Оцените произведение, в диапазоне от 1 до 10', validators=[django.core.validators.MaxValueValidator(limit_value=10, message='Оценка больше 10.'), django.core.validators.MinValueValidator(limit_value=1, message='Оценка меньше 1.')], verbose_name='Оценка')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(help_text='Укажите автора', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('title', models.ForeignKey(help_text='Укажите произведение', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.title', verbose_name='Произведение')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Добавьте описание комментария', verbose_name='Текст комментария')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(help_text='Укажите автора', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('review', models.ForeignKey(help_text='Укажите отзыв', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.review', verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_review'),
        ),
    ]
