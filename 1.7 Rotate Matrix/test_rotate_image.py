from rotate_image import rotate_image, Pixel
import pytest


p1 = Pixel(1, 1, 1, 1)
p2 = Pixel(2, 2, 2, 2)
p3 = Pixel(3, 3, 3, 3)
p4 = Pixel(4, 4, 4, 4)
p5 = Pixel(5, 5, 5, 5)
p6 = Pixel(6, 6, 6, 6)
p7 = Pixel(7, 7, 7, 7)
p8 = Pixel(8, 8, 8, 8)
p9 = Pixel(9, 9, 9, 9)


@pytest.fixture(params=[
    # 3x3 image
    ([[p1, p2, p3],
      [p4, p5, p6],
      [p7, p8, p9]],
     [[p7, p4, p1],
      [p8, p5, p2],
      [p9, p6, p3]]),
])
def test_case(request: pytest.FixtureRequest):
    return request.param


def test_rotate_image(test_case):
    image, expected = test_case
    assert expected == rotate_image(image)
