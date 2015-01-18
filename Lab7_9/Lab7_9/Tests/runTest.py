from Tests.tests_domain import *
from Tests.tests_repository import *
from Tests.tests_controller import *

test_client()
test_movie()
test_rent()

test_client_repository()
test_movie_repository()
test_rent_repository()

test_client_controller()
test_movie_controller()
test_rent_controller()