from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError

def data_processing(data):
    valid_years = [
        1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978,
        1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022
    ]
    
    if data.get("titles", 0) < 0:
        raise NegativeTitlesError()

    first_cup = data.get("first_cup")
    if first_cup:
        try:
            year = int(first_cup.split("-")[0])
            if year not in valid_years:
                raise InvalidYearCupError()
        except ValueError:
            raise InvalidYearCupError("Formato inválido para o ano da Copa do Mundo.")

    titles = data.get("titles", 0)
    cups_disputed = len([y for y in valid_years if y >= int(first_cup.split("-")[0])])
    if titles > cups_disputed:
        raise ImpossibleTitlesError()

    return {
        "name": data.get("name"),
        "titles": data.get("titles"),
        "top_scorer": data.get("top_scorer"),
        "fifa_code": data.get("fifa_code"),
        "first_cup": data.get("first_cup"),
    }
 
  
  