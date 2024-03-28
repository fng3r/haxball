# Register your models here.
from django.contrib import admin
from django.db.models import Q
from django.urls import resolve

from .models import FreeAgent, Player, League, Team, Match, Goal, OtherEvents, Substitution, Season, PlayerTransfer, \
    TourNumber, Nation, Achievements, TeamAchievement, AchievementCategory, Disqualification, Postponement


@admin.register(FreeAgent)
class FreeAgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'position_main', 'description', 'is_active', 'created', 'deleted')


@admin.register(AchievementCategory)
class AchievmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'order')


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_number', 'title', 'description', 'category', 'image', 'mini_image')
    filter_horizontal = ('player',)
    search_fields = ('title__icontains', 'description__icontains',)


@admin.register(TeamAchievement)
class TeamAchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'season', 'title', 'description', 'players_raw_list', 'position_number', 'image')
    filter_horizontal = ('team',)
    search_fields = ('title__icontains', 'description__icontains',)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'team', 'player_nation', 'role',)
    raw_id_fields = ('name',)
    list_filter = ('role', 'team', 'name')
    search_fields = ('nickname', 'name__username',)


@admin.register(PlayerTransfer)
class PlayerTransferAdmin(admin.ModelAdmin):
    list_display = ('trans_player', 'to_team', 'date_join', 'season_join')
    list_filter = ('trans_player', 'to_team',)
    autocomplete_fields = ('trans_player',)


class PlayerInline(admin.StackedInline):
    model = Player

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_title', 'owner',)
    search_fields = ('title',)
    inlines = [PlayerInline]


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created')


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'created')
    filter_horizontal = ('teams',)


@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('country',)


@admin.register(Disqualification)
class DisqualificationAdmin(admin.ModelAdmin):
    list_display = ('match', 'team', 'player', 'reason', 'get_tours', 'get_lifted_tours', 'created')
    filter_horizontal = ('tours', 'lifted_tours')

    def get_tours(self, model):
        return ', '.join(map(lambda t: str(t), model.tours.all()))
    get_tours.short_description = 'Туры'

    def get_lifted_tours(self, model):
        return ', '.join(map(lambda t: str(t), model.lifted_tours.all()))
    get_lifted_tours.short_description = 'Отмененные туры'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'tours' or db_field.name == 'lifted_tours':
            kwargs['queryset'] = TourNumber.objects.filter(league__championship__is_active=True).order_by('number')
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Postponement)
class PostponementAdmin(admin.ModelAdmin):
    list_display = ('match', 'is_emergency', 'get_teams', 'taken_at', 'taken_by', 'cancelled_at', 'cancelled_by')
    filter_horizontal = ('teams',)

    def get_teams(self, model):
        return ', '.join(map(lambda t: str(t), model.teams.all()))
    get_teams.short_description = 'На кого взят перенос'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'match':
            kwargs['queryset'] = Match.objects.filter(league__championship__is_active=True).order_by('numb_tour__number')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'teams':
            kwargs['queryset'] = Team.objects.filter(leagues__championship__is_active=True).distinct()
        return super().formfield_for_manytomany(db_field, request, **kwargs)


class GoalInline(admin.StackedInline):
    model = Goal
    extra = 3

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        resolved = resolve(request.path_info)
        not_found = False
        try:
            match = self.parent_model.objects.get(id=resolved.kwargs['object_id'])
        except:
            not_found = True
        if db_field.name == "team" and not not_found:
            kwargs["queryset"] = Team.objects.filter(Q(home_matches=match) | Q(guest_matches=match)).distinct()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SubstitutionInline(admin.StackedInline):
    model = Substitution
    extra = 3

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        resolved = resolve(request.path_info)
        not_found = False
        try:
            match = self.parent_model.objects.get(id=resolved.kwargs['object_id'])
        except:
            not_found = True
        if db_field.name == "team" and not not_found:
            kwargs["queryset"] = Team.objects.filter(Q(home_matches=match) | Q(guest_matches=match)).distinct()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class DisqualificationInline(admin.StackedInline):
    model = Disqualification
    extra = 1
    filter_horizontal = ('tours',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "team":
            kwargs["queryset"] = Team.objects.filter(leagues__championship__is_active=True).distinct().order_by('title')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "tours":
            kwargs["queryset"] = TourNumber.objects.filter(league__championship__is_active=True).order_by('number')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

class EventInline(admin.StackedInline):
    model = OtherEvents
    extra = 2

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        resolved = resolve(request.path_info)
        not_found = False
        try:
            match = self.parent_model.objects.get(id=resolved.kwargs['object_id'])
        except:
            not_found = True
        if db_field.name == "team" and not not_found:
            kwargs["queryset"] = Team.objects.filter(leagues__championship__is_active=True).distinct().order_by('title')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'league', 'numb_tour', 'team_home', 'score_home', 'team_guest', 'score_guest', 'is_played', 'updated',
        'inspector', 'id',)
    # readonly_fields = ('score_home', 'score_guest',)
    filter_horizontal = ('team_home_start', 'team_guest_start',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Берём из пути id матча
        resolved = resolve(request.path_info)
        
        if db_field.name == 'team_home_start':
            # Игроки команды хозяев
            t = Team.objects.filter(home_matches=resolved.kwargs.get("object_id")).first()
            kwargs["queryset"] = Player.objects.filter(team=t)
        if db_field.name == 'team_guest_start':
            # Игроки команды гостей
            t = Team.objects.filter(guest_matches=resolved.kwargs.get("object_id")).first()
            kwargs["queryset"] = Player.objects.filter(team=t)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    list_filter = ('numb_tour__number', 'league', 'inspector', 'is_played')
    fieldsets = (
        ('Основная инфа', {
            'fields': (('league', 'is_played', 'match_date', 'numb_tour',),)
        }),
        (None, {
            'fields': (('team_home', 'team_guest', 'replay_link',),)
        }),
        (None, {
            'fields': (('score_home', 'score_guest', 'inspector', 'replay_link_second'),)
        }),
        ('Составы', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('team_home_start', 'team_guest_start',)
        }),
        ('Комментарий:', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('comment',)
        })
    )
    # fields = ['is_played', 'league', 'tour_num', 'match_date', ('team_home', 'team_guest'),
    #          ('team_home_start', 'team_guest_start')]
    inlines = [GoalInline, SubstitutionInline, EventInline, DisqualificationInline]


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('match', 'author', 'assistent', 'id')


@admin.register(Substitution)
class SubstitutionAdmin(admin.ModelAdmin):
    list_display = ('match', 'player_out', 'player_in')


@admin.register(OtherEvents)
class OtherEventsAdmin(admin.ModelAdmin):
    list_display = ('event', 'match', 'author',)


@admin.register(TourNumber)
class MatchTourAdmin(admin.ModelAdmin):
    list_display = ('number', 'league', 'is_actual', 'date_from', 'date_to')
    list_editable = ('is_actual',)
    list_filter = ('league', 'number')


"""
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    form = GoalAdminForm
    list_display = ('match', 'author', 'assistent',)
"""
