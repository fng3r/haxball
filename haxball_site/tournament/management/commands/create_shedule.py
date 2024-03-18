import datetime
import random
import time

from django.core.management.base import BaseCommand

from ...models import League, TourNumber, Match
from ...templatetags.tournament_extras import sort_teams

class Command(BaseCommand):
    help = 'The Zen of Python'
    tour_dates = {
        1: datetime.date(2024, 3, 20),
        2: datetime.date(2024, 4, 3),
        3: datetime.date(2024, 4, 7),
        4: datetime.date(2024, 4, 17),
        5: datetime.date(2024, 5, 1),
        # 5: datetime.date(2024, 3, 31),
        # 6: datetime.date(2024, 4, 7),
        # 7: datetime.date(2024, 4, 10),
        # 8: datetime.date(2024, 4, 14),
        # 9: datetime.date(2024, 4, 21),
        # 10: datetime.date(2024, 4, 28),
        # 11: datetime.date(2024, 5, 5),
        # 12: datetime.date(2024, 5, 8),
        # 13: datetime.date(2024, 5, 12),
        # 14: datetime.date(2024, 5, 15),
        # 15: datetime.date(2024, 5, 19),
        # 16: datetime.date(2024, 5, 22),
        # 17: datetime.date(2024, 5, 26),
        # 18: datetime.date(2024, 5, 29),
    }

    def handle(self, *args, **options):
        has_return_matches = False
        league = League.objects.get(priority=4, championship__is_active=True, is_cup=False)
        teams = list(league.teams.all())
        half = len(teams) // 2
        n = len(teams)
        time_delta = datetime.timedelta(days=2)

        print('         Команды участницы:')
        for team in teams:
            print('     {}'.format(team.title))
        print()
        print('     Перемешиваем')
        random.shuffle(teams)
        for team in teams:
            print('     {}'.format(team.title))

        for i in range(1, n):
            tour_number = i
            cr_date = self.tour_dates[i]
            tour = TourNumber.objects.create(number=tour_number, league=league,
                                             date_from=cr_date, date_to=cr_date + time_delta)
            if has_return_matches:
                reverse_tour_number = n + i - 1
                date_cr_2 = self.tour_dates[reverse_tour_number]
                tour_reverse = TourNumber.objects.create(number=reverse_tour_number, league=league,
                                                         date_from=date_cr_2, date_to=date_cr_2 + time_delta)
            print('                 Тур {}'.format(tour))
            for j in range(half):
                team_home = teams[j]
                team_guest = teams[n - j - 1]
                # switch home/away for fixed (first) team
                if j == 0 and i % 2 == 1:
                    (team_home, team_guest) = (team_guest, team_home)
                match = Match.objects.create(team_home=team_home, team_guest=team_guest, numb_tour=tour, league=league)
                if has_return_matches:
                    match_reverse = Match.objects.create(team_guest=team_home, team_home=team_guest,
                                                         numb_tour=tour_reverse, league=league)
                print('          {}  -  {}'.format(match.team_home.title, match.team_guest.title))
            # rotate teams n // 2 times
            for j in range(half):
                teams.insert(1, teams.pop())
            print(teams)

        print()
        print('     Генерация расписания завершена')
        print("           Удачного чемпионата!")
