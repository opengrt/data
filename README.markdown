OpenGRT Data
============

[OpenGRT](http://opengrt.org) aims to make GRT bus routes and stop times accessible to all humans and machines.

Data
----

The html directory contains archives of unprocessed HTML pages scraped from GRT's trip planner website. Each file, when decompressed (~600 MiB) contains the following:

    /<DATE>
    /<DATE>/routes.json
    /<DATE>/<ROUTE>
    /<DATE>/<ROUTE>/stops.json
    /<DATE>/<ROUTE>/<STOP>/arrival.html
    /<DATE>/<ROUTE>/<STOP>/departure.html

for all dates, routes, and stops (which may be found in the routes.json and stops.json files).

### Notes ###

 * Bus stop times for Tuesdays, Wednesdays, and Thursdays are identical. Stop times vary for the other days.
 * All instances of '/' in the route and stop names have been replaced with '|' to preserve proper directory hirearchy.


Contribute
----------

OpenGRT needs developers to parse the raw HTML pages into a machine readable format (such as JSON or XML) and then into [GTFS](http://code.google.com/transit/spec/transit_feed_specification.html). We have a separate [repository](http://github.com/opengrt/gtfs) for the working GTFS files. Please contact us if you would like to be added to either repository as a contributor.

Contact
-------

You can contact us via Twitter ([@OpenGRT](http://twitter.com/OpenGRT)) or by email: admin_AT_opengrt_DOT_org.
