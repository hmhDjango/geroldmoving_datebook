from django.shortcuts import render, render_to_response, get_object_or_404
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from .models import Move
from .forms import MoveForm

from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

from django.conf import settings

from django.template import RequestContext

# method used at website root
# displays calendar for current month
@login_required
def move_calendar_default(request):
    year = timezone.now().year
    month = timezone.now().month
    moves = Move.objects.order_by('created_date').filter(
      move_date__year=year, move_date__month=month
    )
    cal = MoveCalendar(moves).formatmonth(year, month)
    return render_to_response('datebook/move_calendar.html', {'calendar': mark_safe(cal)}, context_instance=RequestContext(request)) 

# method used to display calendar for specific year/month
@login_required
def move_calendar(request, year, month):
    moves = Move.objects.order_by('created_date').filter(
      move_date__year=year, move_date__month=month
    )
    cal = MoveCalendar(moves).formatmonth(int(year), int(month))
    return render_to_response('datebook/move_calendar.html', {'calendar': mark_safe(cal)}, context_instance=RequestContext(request)) 

# displays all moves for a specific day
@login_required
def move_list(request, year, month, day):
    move_date = timezone.datetime(int(year), int(month), int(day))
    moves = Move.objects.filter(move_date=move_date).order_by('created_date')
    move_date = move_date.strftime('%a, %b %d, %Y')
    back_url = settings.SITE_URL + '/' + year + '/' + month
    return render(request, 'datebook/move_list.html', {'moves': moves, 'move_date': move_date, 'year': year, 'month': month, 'day': day, 'back_url': back_url})

# displays all the details for a specific move
@login_required
def move_detail(request, pk):
    move = get_object_or_404(Move, pk=pk)
    move_date = move.move_date.strftime('%a, %b %d, %Y')
    year = str(move.move_date.year)
    month = str(move.move_date.month)
    day = str(move.move_date.day)
    back_url = settings.SITE_URL + '/' + year + '/' + month + '/' + day + '/moves'
    return render(request, 'datebook/move_detail.html', {'move': move, 'move_date': move_date, 'back_url': back_url})

# allows the user to edit info for a specific move
@login_required
def move_edit(request, pk):
    move = get_object_or_404(Move, pk=pk)
    if request.method == "POST":
        form = MoveForm(request.POST, instance=move)
        if form.is_valid():
            move = form.save()
            return redirect('move_detail', pk=move.pk)
    else:
        form = MoveForm(instance=move)
    # get information needed to create the back_url
    # (all the moves for a specific day)
    year = str(move.move_date.year)
    month = str(move.move_date.month)
    day = str(move.move_date.day)
    back_url = settings.SITE_URL + '/' + year + '/' + month + '/' + day + '/moves'
    return render(request, 'datebook/move_edit.html', {'form': form, 'back_url': back_url, 'year': year, 'month': month, 'day':day})

# displays blank move form for a new move
@login_required
def move_new(request, year, month, day):
    if request.method == "POST":
        form = MoveForm(request.POST)
        if form.is_valid():
            move = form.save(commit=False)
            move.author = request.user
            move.move_date = timezone.datetime(year=int(year), month=int(month), day=int(day))
            move.created_date = timezone.now()
            move.save()
            return redirect('move_detail', pk=move.pk)
    else:
        form = MoveForm()
    # create the back_url
    # (all the moves for a specific day)
    back_url = settings.SITE_URL + '/' + year + '/' + month + '/' + day + '/moves'
    return render(request, 'datebook/move_edit.html', {'form': form, 'back_url': back_url, 'year': year, 'month': month, 'day': day})



# custom calendar for the datebook
# each day links to the list of moves for that day
# colors today green
# colors a day which already has a move blue
class MoveCalendar(HTMLCalendar):

    def __init__(self, moves):
        super(MoveCalendar, self).__init__()
        self.moves = self.group_by_day(moves)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                # calendar day is today, so
                # set 'today' class tag to color it green
                cssclass += ' today'
            if day in self.moves:
                # calendar day has moves, so
                # set 'filled' class to color the day green
                cssclass += ' filled'
            # create link for each calendar day
            # uses year/month/day to link for list of moves for day
            body = ['<a href="']
            body.append(settings.SITE_URL)
            body.append("/")
            body.append(str(self.year))
            body.append("/")
            body.append(str(self.month))
            body.append("/")
            body.append(str(day))
            body.append('/moves">')
            body.append(str(day))
            body.append('</a>')
            return self.day_cell(cssclass, '%s' % (''.join(body)))
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(MoveCalendar, self).formatmonth(year, month)

    def group_by_day(self, moves):
        field = lambda move: move.move_date.day
        # get all moves and groop by move_date
        return dict(
            [(day, list(items)) for day, items in groupby(moves, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)


