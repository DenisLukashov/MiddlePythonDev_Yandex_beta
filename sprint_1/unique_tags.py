def unique_tags(payload: dict) -> list:

    tags = {(tag, type(tag)) for tag in payload.get('tags')}
    return [tag[0] for tag in tags]


input_data = {
    "title": "Звездные войны 1: Империя приносит баги",
    "description":
        "Эпичная сага по поиску багов в старом легаси проекте Империи",
    "tags": [
        2, "семейное кино", "космос", 1.0, "сага", "эпик", "добро против зла",
        True, "челмедведосвин", "debug", "ipdb", "PyCharm", "боевик", "боевик",
        "эникей", "дарт багус", 5, 6, 4, "блокбастер", "кино 2020",
        7, 3, 9, 12, "каникулы в космосе", "коварство"
    ],
    "version": 17
}

result = unique_tags(input_data)
print('Результат', result)
