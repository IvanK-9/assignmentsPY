def city_country(city, country, population=None):
    """Возвращает строку вида 'City, Country – population N' или 'City, Country'."""
    if population:
        return f"{city}, {country} – population {population}"
    else:
        return f"{city}, {country}"
