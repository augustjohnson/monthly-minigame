# Game:  Hill Attack (v1).

### Game Description
You and your single opponent are both attacking five hills with your soldiers.  If you attack the hill with more soldiers, then you will win the hill. If you and your opponent attack with the same number of soldiers, you split the points, rounded down. Each hill is worth a different number of points, from 1 to 5.  You have 50 soldiers to allocate.  Hill 1 is worth 1 hill point, Hill 5 is worth 5 hill points.

### Tournament Rules
You may enter only a single soldier allocation strategy, and I will run the following algorithm against your entry, pitting you against each other entrant.  The player whose allocation won them the most hill-points total across all competitions will be declared the winner.

Remember, you a playing against EVERY other player, and your net score for all rounds is what will be added up.  Their strategies are not visible to you and will be unknown to everyone except the game administrator until the game itself is run.

Once the game itself is run, a winner will be declared, and their 

### Example
* Alice allocates her soldiers evenly for all hills.
* Bob allocates his based on hill value, evenly distributing the leftover soldiers.
* Carol is bad at this.

| Hill | Alice       | Bob         |  Carol       |
| ---- |-------------| ------------|  ------------|
|1     | 10 soldiers | 4 soldiers  |  1 soldier   |
|2     | 10 soldiers | 7 soldiers  |  1 soldier   |
|3     | 10 soldiers | 10 soldiers |  1 soldier   |
|4     | 10 soldiers | 13 soldiers |  1 soldier   |
|5     | 10 soldiers | 16 soldiers |  46 soldiers |

#### Results:
**Alice v Bob:** Alice wins hills 1 and 2, netting 3 points. Alice and Bob split hill 3, netting 1 point each. Bob wins hills 4 and 5, netting 9 additional points.

**Alice v Carol:** Alice 10 points, Carol wins 5.

**Bob v Carol:** Bob wins 10 points, Carol wins 5.


#### Final Scores
* Alice: 14
* Bob: 20
* Carol: 10
