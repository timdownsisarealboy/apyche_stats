# Apyche Stats

A simple api to gather stats about the visitors to your apache served site from a separate Django project

## Basic Set-up
- mkvirtualenv --no-site-packages apyche-env
- git clone https://github.com/timdownsisarealboy/apyche_stats.git
- cd apyche_stats/
- pip install -r requirements.pip
- cd apyche_stats/
- python manage.py runserver 0.0.0.0:8000
- http://0.0.0.0:8000/api/stats
- Basic sortable front-end http://${host_name}:8000/media/stats.html

## Default Params
The default /api/stats endpoint will return in order of newest to oldest the last occurence of an IP in the log.

The follow options are available out of the box - default values are bracketed:

```
all : (true|[false]) when true will return all lines in the log
ip_list : (true|[false]) when true returns only an array of ips - useful for bulk lookups
resource : (string) filter the results for a specific resource name
```

### Questions?

Email timothy.j.downs [at] gmail.com
