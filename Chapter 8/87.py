def make_album(artist, title, songs=None):
    """
    Создаёт словарь с информацией об альбоме.
    Если songs не None — добавляет количество песен.
    """
    album = {
        'artist': artist,
        'title': title
    }
    if songs is not None:
        album['songs'] = songs
    return album

# Создаём три альбома (два без числа песен, один с числом)
album1 = make_album("The Beatles", "Abbey Road")
album2 = make_album("Pink Floyd", "The Dark Side of the Moon")
album3 = make_album("Beyoncé", "Lemonade", songs=12)

# Выводим результаты
print(album1)
print(album2)
print(album3)

import sys
print(sys.getrefcount(album1))