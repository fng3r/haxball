import datetime
import random
import time

from django.core.management.base import BaseCommand

from ...models import League, TourNumber, Match
from ...templatetags.tournament_extras import sort_teams

class Command(BaseCommand):
    help = 'The Zen of Python'
    tour_dates = {
        1: datetime.date(2024, 3, 13),
        2: datetime.date(2024, 3, 17),
        3: datetime.date(2024, 3, 24),
        4: datetime.date(2024, 3, 27),
        5: datetime.date(2024, 3, 31),
        6: datetime.date(2024, 4, 7),
        7: datetime.date(2024, 4, 10),
        8: datetime.date(2024, 4, 14),
        9: datetime.date(2024, 4, 21),
        10: datetime.date(2024, 4, 28),
        11: datetime.date(2024, 5, 5),
        12: datetime.date(2024, 5, 8),
        13: datetime.date(2024, 5, 12),
        14: datetime.date(2024, 5, 15),
        15: datetime.date(2024, 5, 19),
        16: datetime.date(2024, 5, 22),
        17: datetime.date(2024, 5, 26),
        18: datetime.date(2024, 5, 29),
    }

    def handle(self, *args, **options):
        league = League.objects.get(priority=3, championship__is_active=True, is_cup=False)
        teams = list(league.teams.all())
        half = len(teams) // 2
        n = len(teams)
        date_start = datetime.date(2024, 3, 13)
        # cr_date = date_start
        time_delta = datetime.timedelta(days=2)
        #
        # date_cr_2 = datetime.date(2024, 4, 28)

        print('         Команды участницы:')
        for team in teams:
            print('     {}'.format(team.title))
        print()
        print('     Перемешиваем')
        random.shuffle(teams)
        for team in teams:
            print('     {}'.format(team.title))

        for i in range(1, len(teams)):
            tour_number = i
            cr_date = self.tour_dates[i]
            tour = TourNumber.objects.create(number=tour_number, league=league, date_from=cr_date, date_to=cr_date + time_delta)
            reverse_tour_number = i + n - 1
            date_cr_2 = self.tour_dates[reverse_tour_number]
            tour_reverse = TourNumber.objects.create(number=reverse_tour_number, league=league, date_from=date_cr_2,
                                                     date_to=date_cr_2 + time_delta)
            print('                 Тур {}'.format(tour))
            for j in range(half):
                match = Match.objects.create(team_home=teams[j], team_guest=teams[n - 1 - j], numb_tour=tour,
                                             league=league)
                match_reverse = Match.objects.create(team_guest=teams[j], team_home=teams[n - 1 - j],
                                                     numb_tour=tour_reverse,
                                                     league=league)
                print('          {}  -  {}'.format(match.team_home.title, match.team_guest.title))
            teams.insert(1, teams.pop())

        print()
        print('     Генерация расписания завершена')
        print("           Удачного чемпионата!")
