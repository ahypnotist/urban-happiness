from pprint import pprint
    #cardjitsu
#club penguin game where its pretty much rock paper scissors but with ice water and fire
#every card has a number, which doesnt matter unless you and the opponent choose the same element. then the higher number wins
#also it hink there are some cards that kinda mess up the rules but shhh
#if you beat an snow/fire/water 3 times you win. also if you get 3 of the same color.
#this might be a good excersice for experience with classes

class card:
  def __init__(self, element, number, color):
    self.element = element #determines whether its fire, snow , or water
    self.number = number #determines the card value
    self.color = color #determines the color of the card
    self.play = play
    self.me = me

while True :
    if card.play == True :
        if card.element == card.element

c1 = card("fire", "5", "green", False, "me")
c2 = card("snow", "7", "yellow", False, "me")
ec1 = card("water", "9", "red", False, "enem")
ec2 = card("fire", "2", "yellow", False, "enem")

while True :
    while True :
        play = input("what card will you play? type SHOW CARDS to show your cards.")
        if play == "SHOW CARDS" :
            pprint(vars(c1))
            pprint(vars(c2))
        elif play == "1" :
            c1.play = True
        
        
