from enum import Enum
class Color(Enum):
    RED = "red"
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter choice : "))

match color:
    case Color.RED:
        print("its red")
    case Color.GREEN:
        print("no its green")
    case Color.BLUE:
        print('thats is blue')





# class Point:
#     __match_args__ = ('x', 'y')
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# match Point(0,2), Point(0,3):
#     case[]:
#         print("no points")
#     case [Point(x, y)]:
#         print(f"single point {x}, {y}")
#     case [Point(0, y1), Point(0, y2)]:
#         print(f"2 on the T axis at {y1}, {y2}")
#     case _:
#         print("Something else")
# #2 on the T axis at 2, 3

# # def where_is(point):
# #     match point:
# #         case Point(x = 0, y = 0):
# #             print("Origin")
# #         case Point(x = 0, y = y):
# #             print(f"Y={y}")
# #         case Point(x = x, y = 0):
# #             print(f"X={x}")
# #         case Point():
# #             print("somewhere else")
# #         case _:
# #             print("not a point")
            
# # where_is(Point(2,3))
# # # somewhere else