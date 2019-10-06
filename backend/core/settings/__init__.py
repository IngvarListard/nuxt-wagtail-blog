from backend.core.utils import get_bool_from_env

DEBUG = get_bool_from_env('DEBUG', False)

if DEBUG:
    from .debug import *
else:
    from .production import *

