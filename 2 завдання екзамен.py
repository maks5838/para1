# class Piece:
#     def __init__(self, color, position):
#         self.color = color
#         self.position = position
#
#     def move(self, new_position):
#         print(f"Moving {self.__class__.__name__} from {self.position} to {new_position}")
#         self.position = new_position
#
#
# class Pawn(Piece):
#     def move(self, new_position):
#         print(f"{self.color.capitalize()} pawn moving from {self.position} to {new_position}")
#         self.position = new_position
#
#
# class Rook(Piece):
#     def move(self, new_position):
#         print(f"{self.color.capitalize()} rook moving from {self.position} to {new_position}")
#         self.position = new_position
#
#
# class Knight(Piece):
#     def move(self, new_position):
#         print(f"{self.color.capitalize()} knight moving from {self.position} to {new_position}")
#         self.position = new_position
#
#
# class Bishop(Piece):
#     def move(self, new_position):
#         print(f"{self.color.capitalize()} bishop moving from {self.position} to {new_position}")
#         self.position = new_position
#
#
# class Queen(Piece):
#     def move(self, new_position):
#         print(f"{self.color.capitalize()} queen moving from {self.position} to {new_position}")
#         self.position = new_position
#
#
# class King(Piece):
#     def move(self, new_position):
#         print(f"{self.color.capitalize()} king moving from {self.position} to {new_position}")
#         self.position = new_position
# if __name__ == "__main__":
#     pawn = Pawn("білий", "e2")
#     rook = Rook("чорний", "a8")
#     knight = Knight("білий", "g1")
#     bishop = Bishop("чорний", "c8")
#     queen = Queen("білий", "d1")
#     king = King("чорний", "e8")
#
#     pawn.move("e4")
#     knight.move("f3")
#     bishop.move("b7")
#     queen.move("d5")
#     king.move("e7")
