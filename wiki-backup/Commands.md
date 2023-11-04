SWAT makes use of a number of chat commands. Knowledge of these commands
is not necessary to play the game, except for Rank Codes, but they can
make the game much easier to manage and coordinate between players.

## Rank Codes

-   0000 0000 0000 0000 *or* 0000-0000-0000-0000

Rank codes are the only chat command that players will need to know. At
the end of every game, players are given a 16-digit numeric code which
preserves their customisations and rank. Rank codes must be entered at
the beginning of the game, *before* choosing a class.

## Chat Colours

*Several chat commands require a player to be specified. Each player has
a corresponding letter, arranged by their colour.*

-   **<span style="color: #ff0000;">R</span>**ed
-   **<span style="color: #0000ff;">B</span>**lue
-   **<span style="color: #00ffff;">T</span>**eal
-   **<span style="color: #800080;">P</span>**urple
-   **<span style="color: #bbbb00;">Y</span>**ellow
-   **<span style="color: #ec6e0e;">O</span>**range
-   **<span style="color: #00a000;">G</span>**reen
-   pin**<span style="color: #ee9696;">K</span>**
-   gr**<span style="color: #404040;">A</span>**y
-   **<span style="color: #6fa4fd;">L</span>**ight blue\*
-   **<span style="color: #0a5223;">D</span>**ark green\*
-   bro**<span style="color: #613f0c;">W</span>**n\*
-   bla**<span style="color: #000000;">C</span>**k\*

(\*these additional colors apply only to the -key command)

## Standard Commands

-   -dead

Pings the corpses of all dead players. Includes dead Officers and Cadets

-   help

An alternative method of using the Help innate (ZD). Pings the Officer's
location (or corpse) and displays a Help message to the team describing
the player's current predicament. Can be used while the player is dead
to ping their corpse. This command can also request energy from a [Tech
Ops](Tech_Ops "wikilink") CPU, use an Officer's
[Energizer](Traits#Energizer "wikilink") battery, or request health from
a [Watchman's Nurse](Watchman#Paradox "wikilink").

-   -revive

*Only available on Normal Difficulty for ranks 4+.*

This command instantly revives all dead Rank 1 Officers that are at or
under a level determined by rank of the user and they come back to life
with full mana, hitpoints, and no rez sickness. Rank 4's can revive to
level 12's. The level cap goes up by 2 for every rank ending with level
28 at rank 12.

-   -time

Gives the current amount of time the game has gone on. Very helpful in
Perfect Insane and Survival games. Also fixes squad status box if broken
from full shared control.

-   -view \#

Moves the camera back to allow more vision. 1 will set the camera to the
standard WC3 zoom. This is set to 30 after the player loads their
character. Numbers beyond 60 will revert to 60 after a few seconds.
Values are capped at 100. Negative values will use a direct overhead
view, rather than the standard camera angle.

*WARNING: Use of this command may slow game play on slower computers!*

-   -info \[color\]

Displays the Class, Rank, Weapon, Armor, and Trait(s) of the Officer the
command is used on.

-   -kick \[color\]

Command that is used to kick players. The kick system lets you vote to
kick a player out of the game. Your vote weight is determined by your
rank. A rank 11 player's vote has more weight than a rank 1's vote. It
is not a majority vote. Each vote contributes a certain amount of points
to one player's kick status. Once that number reaches a set amount based
on the number of players, then that player is booted from the game.
Killing a player automatically adds some points to your own kick status,
making you much easier to kick. When a player starts a kick, his vote
counts lower in future kicks that occur recently to when he started the
kick. If the killing player is kicked from the game, the killed player
is automatically revived (lower difficulties only).

Kicked players do get a rank code. If a team kicks the last alive person
then he gets a rank code and everyone else doesn't.

-   -perfect

*Only available on Insane difficulty for ranks 7+.*

Initiates a vote that, if passed, enforces perfect conditions in an
insane game. The game will not end until either the team dies, the
objectives are completed perfectly, or the game is beaten normally and
the game time exceeds \~64 minutes.

-   -pool *or* -pool \# \#

*-pool \#* sets the player's own gold minimum balance, the second \#
sets the player's own valor minimum balance. Credits and valor beyond
this amount can be collected by other players using the *-pool* command.
This command is critical in any serious group game.

-   -icons \[color\]

*-icons \[color\]* allows you to add another player's hero icon(s) to
your screen. Can be used to add multiple heroes at a time (i.e., -icons
rbty or -icons r b t y, for red blue teal and yellow hero icons).

-   -default

*-default* issues the commands -pool 0 0 and -view 60 (the most common
view used). Can also be used as the *-icons* command (i.e., -default
rbty).

-   -ms

*-ms* allows you to display the current move speed of your primary
Officer.

-   -nm *or* -ext

*-nm or -ext* allows the team to force Nightmare or Extinction
difficulty when all Rank 12 Officers are loaded in a game. The commands
must be used before Nightmare/Extinction activates.

-   \[space\]

Prefixing chat text with a space will create floating text above the
player's head corresponding to what was typed.

## Debugging Commands

These commands are used by developers for testing purposes but are also
available for use by any player. To use these built commands in a game
of SWAT, players must play the game solo, with no computer or human
assistance. Using any of these commands will prevent players from
gaining any rank experience, and also disables the ending cinematic.
Cheaters get a special message when the game ends.

-   -credits \#

Gives the player \# credits.

-   -valor \#

Gives the player \# valor.

-   -atme

Drops all the A.T.M.E. items at the feet of the Officer except for the
Temporal Avatar (you should have the 3-Charge anyways) and the Solar
Battery because it requires extra triggers that redscull didn't think
needed to be in there for cheats.

-   -advnanites

Sets the Officer's Nanites to a special kind that has no level (leveling
the ability doesn't do anything) and absorbs 100% of damage and costs
0.01 energy per damage. Effectively 1000% more effective than the best
possible Nanites you can get in the game.

*WARNING: Do not turn on Force Field or pick up the Shield Capacitor
item as it will give you two Nanites skills and push out one of your
usable skills.*

-   -level \#

Grants the Officer \# levels (can't go past 54 level-ups). Applies the
level-ups one at a time, over time. You must have the Officer selected
while the level-ups are being applied, and the Officer must be able to
gain experience (not in a shelter, etc). Command only works on the main
Officer.

-   -spawn

*This command did not disable rank experience or the ending cinematic.
It was removed in v1.3 during 2006 as it was only ever intended as a
debugging function. This entry remains here for historical purposes.*

This toggle command allowed players to monitor zombie and boss spawning.
Only one player could access these notifications at any given time.
While activated, messages will regularly update the player every time an
enemy spawns. Mobs refer to Zombies. Minions refer to Grotesques,
Beasts, Dogs and Mutants. The number appended to the notation is a count
of how many non-boss enemies are currently on the map. Queue means there
are already 200 enemies on the map; instead of spawning these new
enemies, the game will wait for players to kill some zombies, and the
number will instead count the zombies in queue. Tyrants will spawn once
the queue exceeds *???* units, and the player will also be notified when
this happens. Boss spawns will have several messages to their spawns.
[Walkers](Terminology#w "wikilink") will also be identified explicitly
in the messages.