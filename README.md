
# Blogit

This is a blog for posting all your latest ideas, thoughts and discoveries. Post anything and everything, there is no limit!

Use your gmail credentials to login and create your posts!

This is hosted at: https://davidmoss-blogit.appspot.com and a simple API is accessible at https://davidmoss-blogit.appspot.com/blog/api.

## Development

Run:

	$ ./install_deps
	$ python manage.py runserver

## Deployment

Run:

    $ python manage.py collectstatic
    $ appcfg.py update ./

## Test

Run:

    $ python manage.py test blog

## Credit

This was created from the barebones Django project configured for use on App Engine using [Djangae](https://github.com/potatolondon/djangae)

## TODO

* Fix the eventual consitency of the data back from the datastore