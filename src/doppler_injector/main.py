# -*- coding: utf-8 -*-
"""
Main function.
"""
import os

from box import Box
from doppler_env import load_dotenv


def doppler_inject():
    """
    Wrapper for doppler_env.load_dotenv.

    First must activate Doppler and export
    to Environments:
    $ export DOPPLER_ENV=1
    Set DOPPLER LOGs as well:
    $ export DOPPLER_ENV_LOGGING=1
    Then run:
    $ doppler setup

    """
    load_dotenv()
    return Box(os.environ)


def reasearch():
    """
    Learned techniques from: https://betterdatascience.com/python-dotenv/.
    Will learn more and maybe make this a package...
    Such as having the ability to load DOPPLER automatically and
    check for login.
    """
    pass
