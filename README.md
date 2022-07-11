# Minimal example of Dpytest

I found it really difficult to use this library orignially, so I hope this may help someone get
started with it

# How to use
To run tests run the command "pipenv run test"


# Possibly other helpful things
Pytest is an extremely flexible library, parameters such as -lf (last fail) and -ff (failed first)
may prove useful.

Info logging outputs can be seen via passing the argument --log-cli-level=INFO

For example: `pipenv run test -v -W ignore:DeprecationWarning --log-cli-level=INFO`
is the command that I will generally use.
