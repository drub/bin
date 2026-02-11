
'''
Source:
https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5

Mentioned in a Python Weekly newsletter: 2020-01-09
'''

if not sys.version_info > (2, 7):
   # berate your user for running a 10 year
   # python version
elif not sys.version_info >= (3, 5):
   # Kindly tell your user (s)he needs to upgrade
   # because you're using 3.5 features
