# Multiple Inheritance 

class Game():
    def Playing(self):
        print("\t\t\t\t\t\tAnime Fight")
class OnePiece(Game):
    def OnePieceinfo(self):
        print("\n\t One Piece. The Famous Anime that familiar game Street Fighter  is played like this: at the same time, two players(one user, one computer) displays Some character in a Certain Anime. All characters have differents abilities and specialties.")
class Naruto(Game):
    def Narutoinfo(self):
        print("\n\tNaruto. Lets you pick a charactes of another famous anime Naruto Shippuden. Play the game between that computer action and the user,  true randomness abilities of Characters and the luck factor you may win the games.")
        
op = OnePiece ()
op.Playing()
op.OnePieceinfo()
n = Naruto()
n.Playing()
n.Narutoinfo()
