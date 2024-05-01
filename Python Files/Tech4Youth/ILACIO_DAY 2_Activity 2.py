print("Castle on the hill chorus by Ed Sheeran")
song = ("""
I'm on my way
Driving at 90 down those country lanes
Singing to tiny dancer
And I miss the way you make me feel, and it's real
When we watched the sunset over the castle on the hill
Over the castle on the hill
Over the castle on the hill
One friend left to sell clothes
One works down by the coast
One had two kids, but lives alone
One's brother overdosed
One's already on his second wife
One's just barely getting by, but
These people raised me
And I can't wait to go home
""")
print(song)

noun1 = input("Enter 1st noun: ")
noun2 = input("Enter 2nd noun: ")
noun3 = input("Enter 3rd noun: ")
adj1 = input("Enter 1st adjective: ")
adj2 = input("Enter 2nd adjective: ")
adj3 = input("Enter 3rd adjective: ")

revise = song.replace('lanes', noun1.upper()).replace('dancer', noun2.upper()).replace('castle', noun3.upper()).replace('tiny', adj1.upper()).replace('two', adj2.upper()).replace('second', adj3.upper())

print("\n====RESULTS====\n" + revise)