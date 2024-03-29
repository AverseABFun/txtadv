"""The command-related stuff in txtadv."""
from txtadv.location import get_loc_from_num, get_num_from_loc
from txtadv.messaging import error, info, setinfomode, no_origin, origin
from txtadv.color import colored
import random
import sys
import pickle
import datetime


class Command:
    """A command, such as 'look' or 'examine'."""

    #pylint: disable-next=too-many-arguments
    def __init__(self, name: str, func, desc: str, ldesc: str, aliases=None):
        self.name = name
        self.func = func
        self.desc = desc
        self.ldesc = ldesc
        if aliases is None:
            aliases = []
        self.aliases = [name] + aliases

    def help(self):
        """Returns the help string for this command"""
        return f"{self.name} - {self.desc}"

    def __str__(self):
        return self.help()

    def __repr__(self):
        return self.help()

    def __call__(self, *args):
        self.func(*args)


#pylint: disable-next=too-many-branches
def look(inp, _world, player):
    """Look around from the perspective of the Player passed in."""
    inp = inp.replace("look", "", 1).strip()
    if inp.split(" ")[0] == "at":
        inp = inp.replace("at", "", 1).strip()
        examine("examine " + inp, _world, player)
        return
    setinfomode(no_origin)
    info(player.loc.name + ": " + player.loc.desc + "\n", player)
    if len(player.loc.items) > 0:
        info("There is ", player)
    for i in player.loc.items:
        info(colored(i.name, 'blue'), player)
    info("\n", player)
    nones = 0
    for i in player.loc.exits:
        nones = nones + int(not i)
    if len(player.loc.exits) == 1 and nones != len(player.loc.exits):
        info("There is an exit ", player)
    elif len(player.loc.exits) > 1 and nones != len(player.loc.exits):
        info("There are exits ", player)
    for index, val in enumerate(player.loc.exits):
        if val:
            loc = get_loc_from_num(index)
            res = ''
            if loc == 'up':
                loc = 'above you'
                loc = colored(loc, 'green')
                res = loc
            elif loc == 'down':
                loc = 'below you'
                loc = colored(loc, 'green')
                res = loc
            else:
                loc = colored(loc, 'green')
                res = 'to the ' + loc
            if index == len(player.loc.exits) - 1:
                res = 'and ' + res + colored('.', 'grey')
            else:
                res = res + colored(', ', 'grey')
            info(res, player)
    info("\n", player)
    setinfomode(origin)


def examine(inp, _world, player):
    """Examine an item."""
    inp = inp.replace("examine ", "", 1)
    item = None
    for i in player.inventory.items:
        if i.name == inp:
            item = i
    for i in player.loc.items:
        if i.name == inp:
            item = i
    if not item:
        error("There's no object with that name!\n", player)
        return
    setinfomode(no_origin)
    info(colored(item.name + ': ' + item.ldesc, 'yellow') + '\n', player)
    setinfomode(origin)


def tahelp(inp, world, player):
    """The help command. Named 'tahelp' so that it won't override the builtin function 'help'"""
    inp = inp.replace("help", "", 1).strip().replace("h", "", 1).strip()
    setinfomode(no_origin)
    if inp != "":
        for i in world.cmds:
            if i.name == inp:
                info(colored(i.name + ": " + i.ldesc + '\n', 'blue'), player)
                setinfomode(origin)
                return
        error(
            "There's no command with that name! Run 'help' to get a list of commands.\n",
            player)
    for index, val in enumerate(world.cmds):
        if index % 2 == 0:
            info(colored(val.help() + '\n', 'yellow'), player)
        elif index % 2 == 1:
            info(colored(val.help() + '\n', 'blue'), player)
    setinfomode(origin)

def about(_inp, world, player):
    info(f"{world.name} by {world.author}\n", player)
    info(f"{world.desc}\n", player)


def move(inp, _world, player):
    """Go in a specific direction"""
    inp = inp.replace("go", "", 1).strip()
    inp = inp.replace("move", "", 1).strip()
    dir = get_num_from_loc(inp)
    if dir == -1:
        error("What direction is that?\n", player)
        return
    player.move(player.loc.exits[dir])
    look("look",_world,player)


def moveCommand(dir):
    """Create a move command for a specific direction"""
    def func(_inp,_world,_player):
        move(f"go {dir}",_world,_player)
    return Command(dir,func,f"Go {dir}","I mean, isn't it obvious?",aliases=[str(dir)[0]])


def say(inp, world, player):
    """Say something in the room you are in"""
    inp = inp.replace("say", "", 1).strip()
    world.chat_event.trigger(inp, player.name, local=player.loc)


def announce(inp, world, player):
    """Announce something to the entire World"""
    inp = inp.replace("announce", "", 1).strip()
    world.chat_event.trigger(inp, player.name, local=None)


def list_chat(_inp, world, player):
    """List all chat messages in this World"""
    setinfomode(no_origin)
    for i in world.chat:
        info(i + "\n", player)
    setinfomode(origin)


"""def taif(inp, world, player):
    #pylint: disable-next=line-too-long
    \"""For Entities, this command is useful for shops or other similar things, because you can test if the player says or does something.\"""
    inp = inp.replace("if", "", 1).strip()
    try:
        result = player.exec(inp.replace("}", "", 1).strip(), world)
    except AttributeError:
        error("Sorry, the 'if' command only works for Entities.", player)
        return
    if result:
        player.context += 1
    else:
        player.prevcontext = player.context
        player.context = "skip"


def said(inp, world, player):
    \"""Test if something has been said(for entities only)\"""
    inp = inp.replace("said", "", 1).strip()
    try:
        player.exec("look", world)
    except AttributeError:
        error("Sorry, the 'said' command only works for Entities.", player)
    for i in world.chat:
        ali = i.replace("says: ","")
        tmp = ali.split(" ")[0]
        ali = ali.replace(tmp,"").strip()
        if inp in (i, ali):
            return True
    return False"""

def get(inp, _world, player):
    """Get an item"""
    inp = inp.replace("get", "", 1).strip().replace("take", "", 1).strip()
    for i in player.loc.items:
        if i.name == inp:
            player.pickup(i)
            return
    error("There's no item with that name in the room!\n", player)


def drop(inp, _world, player):
    """Drop an item"""
    inp = inp.replace("drop", "", 1).strip()
    for i in player.inventory.items:
        if i.name == inp:
            i.move(player.loc)
            return
    error("There's no item with that name in your inventory!\n", player)

def inventory(_inp, _world, player):
    if len(player.inventory.items)==0:
        info("You have nothing.\n", player)
        return
    for i in player.inventory.items:
        info(f"{i.name}: {i.sdesc}\n", player)

def wait(_inp, _world, player):
    info("Time passes.\n", player)

def again(inp, world, player):
    """Perform a command again"""
    inp = player.commands[-2]
    cmd_count = 0
    found = False
    for cmd in world.cmds:
        for alias in cmd.aliases:
            if inp.lower().startswith(alias.lower()):
                setinfomode(origin)
                cmd(inp, world, player)
                found = True
                break
        if not found:
            cmd_count += 1
        else:
            break
    if not found:
        error(
            f"{random.choice(world.invalid_text)}\n",
        player)

#def undo(_inp, world, player):
#    state = world.states[-2]
#    world.__dict__ = state.__dict__

def quit(_inp, world, _player):
    """Quit the game"""
    sys.exit(0)

def save(inp, world, player):
    inp = inp.replace("save", "", 1).strip()
    game = {"player": {"inventory": player.inventory, "loc": player.loc}}
    pickle.dump(game, open(f"txtadv/saves/{inp or datetime.datetime.now().ctime()}.tasave","wb"))
    info("Saved.\n", player)

def load(inp, world, player):
    inp = inp.replace("load", "", 1).strip().replace("restore", "", 1).strip()
    for key, value in enumerate(pickle.load(open(f"txtadv/saves/{inp}.tasave", "rb"))["player"]):
        world.players[0].__dict__[key] = value
    info("Loaded.\n", player)


globalcmds = [
    Command("save", save, "Save the game", "Good idea before doing something risky."),
    Command("load", load, "Load a save", "Restore a save.", aliases=["restore"]),
    Command("quit", quit, "Quit the game", "Chicken!",aliases=["q"]),
    Command("help", about, "Get help on the commands",
            "It's the help command", aliases=["about"]),
    Command("look", look, "Look around the room",
            "Look at the room that the current player is in", aliases=["l"]),
    Command("examine", examine, "Examine an item",
            "Examine an item closely to get more info", aliases=["x"]),
    Command("go", move, "Go in a direction", "Go in a certain direction",
            ["move"]),
    #Command("undo", undo, "Undo a command", "Undo a command"),
    moveCommand("north"),
    moveCommand("south"),
    moveCommand("east"),
    moveCommand("west"),
    moveCommand("up"),
    moveCommand("down"),
    Command(
        "say", say, "Say something to the room you are currently in",
        "Unlike 'announce', it will only say something to the room you are currently in"
    ),
    Command("announce", announce, "Announce something to the entire World",
            "Unlike 'say', this command says something to the entire World"),
    Command("chat", list_chat, "List the chat messages",
            "That's pretty much it", ["list chat"]),
    Command("get", get, "Get an item", "You monster!"),
    Command("take", get, "Take an item", "Good. I can trust you."),
    Command("drop", drop, "Drop an item", "That's it."),
    Command("inventory", inventory, "Show your inventory", "See the items you have", aliases=["i"]),
    Command("wait", wait, "Wait a turn", "Might be useful, might not. Who knows.", aliases=["z"]),
    Command("again", again, "Perform a command again", "Nice if you need to do something a bunch of times", aliases=["g"])
]
