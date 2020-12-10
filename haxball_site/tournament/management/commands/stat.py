from django.core.management.base import BaseCommand

from ...models import League, TourNumber, Match, Team


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        try:
            league = League.objects.get(championship__is_active=True, is_cup=False)
        except:
            print('Ошибка выбора лиги')
        matches = Match.objects.filter(league=league, is_played=True)
        teams = league.teams.all()
        # print(matches)
        norm_matches = []
        tp_matches = []
        for m in matches:
            all_goals = m.score_home + m.score_guest

            goals_scored = m.match_goal.count() + m.match_event.filter(event='OG').count()

            if goals_scored == all_goals:
                norm_matches.append(m)
            else:
                tp_matches.append(m)
        print('norm', len(norm_matches))
        print('TP', len(tp_matches))
        # Scores red/blue
        score_red = 0
        score_blue = 0
        win_red = 0
        win_blue = 0
        draws = 0
        goals = [0 for _ in range(16)]
        # goals - og count
        goals_not_og = 0
        goals_with_assist = 0
        og = 0
        for m in norm_matches:

            goals_not_og += m.match_goal.count()
            for g in m.match_goal.all():
                if g.assistent:
                    goals_with_assist += 1
            og += m.match_event.filter(event='OG').count()

            score_red += m.score_home
            score_blue += m.score_guest
            if m.score_home > m.score_guest:
                win_red += 1
            elif m.score_home < m.score_guest:
                win_blue += 1
            else:
                draws += 1

            for goal in m.match_goal.all():
                goals[goal.time_min] += 1

        print('stata')
        print(score_red, score_blue)
        print(win_red, draws, win_blue)
        print('OG', og)
        print('Goals not og', goals_not_og)
        print('Goals with assits', goals_with_assist)
        print('Goals in timeline')
        print(goals)
        print(league)
        #Stat for each team

        for t in teams:
            score_red = 0
            score_blue = 0
            win_red = 0
            win_blue = 0
            draws = 0
            goals = [0 for _ in range(16)]
            # goals - og count
            goals_not_og = 0
            goals_with_assist = 0
            og = 0
            og_opp = 0
            matches_played = 0
            for m in norm_matches:
                if m.team_home == t or m.team_guest == t:
                    matches_played += 1
                    goals_not_og += m.match_goal.filter(team=t).count()
                    for g in m.match_goal.all():
                        if g.assistent and g.team == t:
                            goals_with_assist += 1
                    og += m.match_event.filter(event='OG', team=t).count()
                    og_opp = og_opp + (m.match_event.filter(event='OG').count() - m.match_event.filter(event='OG', team=t).count())

                    if t == m.team_home:
                        score_red += m.score_home
                    else:
                        score_blue += m.score_guest
                    if m.score_home > m.score_guest and m.team_home == t:
                        win_red += 1
                    elif m.score_home < m.score_guest and m.team_guest == t:
                        win_blue += 1
                    else:
                        draws += 1

                    for goal in m.match_goal.all():
                        if goal.team == t:
                            goals[goal.time_min] += 1
                    for own_goal in m.match_event.filter(event='OG').all():
                        if own_goal.team != t:
                            goals[goal.time_min] += 1

            if score_blue+score_red != 0:
                og_opp_percent = (og_opp/(score_red+score_blue))*100

            print('Статистика ', t)
            print('Матчей сыграно', matches_played)
            print('Голов забито(с АГ сопов)', score_blue+score_red)
            print('Голов красными - синими', score_red, score_blue)
            print('Побед красными, побед синими', win_red, win_blue)
            print('Автоголов в матче(своих)', og)
            print('Автоголов в матче(соперника)', og_opp)
            print('Процент Автоголов в матче (соперника)', round(og_opp_percent, 2))
            print('Голы, не автоголы ', goals_not_og)
            print('Голы с ассистированием', goals_with_assist)
            print('Процент голов с ассистами', round(goals_with_assist/goals_not_og, 2))
            print('Распределение голов по ходу матча')
            print(goals)
            print('')



        print('The End')
