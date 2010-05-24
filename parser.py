#!/usr/bin/env python

r'''
Parser for GRT's route schedules. Outputs .csv

Paul Butler / May 2010 / MIT license
'''

from sys import stdin, argv, stderr
from BeautifulSoup import BeautifulSoup
from itertools import chain
from time import strptime, strftime

TIMETABLE_TYPES = {
        'Arrival times':   'ARRIVE',
        'Departure times': 'DEPART',
}

def format_time(time):
    time = strptime(time, '%I:%M %p')
    return strftime('%H:%M', time)

def format_date(date):
    date = strptime(date, '%B %d, %Y')
    return strftime('%Y-%m-%d', date)

def scrape_route(soup):
    timetable_type = soup.find('span', id='ViewStopTimetableControl_TimetableTitleLabel').string
    timetable_type = TIMETABLE_TYPES[timetable_type]
    date = soup.find('span', id='StopTimetableInfoControl_DateOutputLabel').string
    date = format_date(date)
    route = soup.find('span', id='StopTimetableInfoControl_RouteOutputLabel').string
    stop = soup.find('span', id='StopTimetableInfoControl_StopOutputLabel').string
    routes_dict = {}
    route_notes = chain(soup.findAll('tr', 'NoteRow'), soup.findAll('tr', 'NoteAlternatingRow'))
    for route_note in route_notes:
        code = route_note.find('td', 'NoteCode').string.strip()
        #routes = route_note.find('td', 'NoteRoutes').string.strip()
        desc = route_note.find('td', 'NoteDescription').string.strip()
        #print 'Code: [%s], description: %s' % (code, desc)
        routes_dict['[%s]' % code] = desc

    #print 'Timetable: %s' % timetable_type
    #print 'Date: %s' % date
    #print 'Route: %s' % route
    #print 'Stop: %s' % stop
    stop_times = soup.findAll('td', 'TimetableCell')
    for stop_time in stop_times:
        time = stop_time.find('span', 'TimetableTime').string
        note = stop_time.find('span', 'TimetableNote').string
        if note:
            r_note = routes_dict[note]
        else:
            r_note = ''
        if time:
            time = format_time(time)
            #print 'Time: %s, note: %s' % (time, note)
            print ','.join((
                timetable_type,
                date,
                route,
                stop,
                time,
                r_note,
            ))



if __name__ == '__main__':
    if len(argv) > 1:
        filename = argv[1]
        f = file(filename)
    else:
        filename = 'stdin'
        f = stdin
    print >> stderr, "Parsing %s" % filename
    soup = BeautifulSoup(f.read())
    scrape_route(soup)

