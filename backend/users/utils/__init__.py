import os
from hashlib import sha1

def avatar_directory_path(instance, filename):
    # Хешируем входной файл
    instance.avatar.open()
    contents = instance.avatar.read()
    hasher = sha1()
    hasher.update(contents)
    # Используем хеш в качестве имени файла
    path = 'avatars/{}{}'.format(hasher.hexdigest(), os.path.splitext(filename)[1])
    return path


