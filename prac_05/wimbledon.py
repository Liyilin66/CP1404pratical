import csv

dict_champions = {}
info = []


def main():
    """call the functions and print the first sentence"""
    filename = "wimbledon.csv"
    wimbledon_winners = get_file(filename)
    print(wimbledon_winners)
    champion = get_champion(wimbledon_winners)
    dict_count_champions = count_champions(champion)
    print(dict_count_champions)
    display_champions(dict_count_champions)
    win_country = get_country(wimbledon_winners)
    win_times = count_win_times(win_country)
    display_countries(win_country, win_times)


def get_file(filename):
    """read in"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        record = csv.reader(in_file)
        next(record)
        for i in record:
            info.append(i)
    return info


def get_champion(wimbledon_winners):
    champions = []
    for i in wimbledon_winners:
        athlete = i[2]
        champions.append(athlete)
    return champions


def count_champions(champion):
    for name in champion:
        try:
            dict_champions[name] += 1
        except KeyError:
            dict_champions[name] = 1
    return dict_champions


def display_champions(counted_champions):
    for i in counted_champions:
        print(f"{i} {counted_champions[i]}")


def get_country(wimbledon_win_country):
    countries = set()
    for i in wimbledon_win_country:
        country = i[1]
        countries.add(country)
    return sorted(countries)


def display_countries(countries, win_times):
    print(f"These {win_times} countries have won Wimbledon:")
    for i in countries:
        print(i, end=' ')


def count_win_times(countries):
    count_countries = list(countries)
    count = len(count_countries)
    return count


main()
