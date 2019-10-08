import pytest
from triangle import triangle_type

many_triangles = [
    (100, 40, 40, "obtuse"),
    ( 60, 60, 60, "acute"),
    ( 90, 60, 30, "right"),
    (  0,  0,  0, "invalid"),
]

def idfn(a_triangle):
    a, b, c, expected = a_triangle
    return f'{a}_{b}_{c}_{expected}'

@pytest.fixture(params=many_triangles, ids=idfn)
def a_triangle(request):
    return request.param

def test_type(a_triangle):
    a, b, c, expected = a_triangle
    assert triangle_type(a, b, c) == expected
