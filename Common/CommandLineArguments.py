
from typing import *

class CommandLineArguments:
    def __init__(self,*args):
        self.Arguments = args
        self.FlagArguments = [False for x in args]
        self.UsedArguments = [False for x in args]
        self.ArgumentToFirstIndex :Dict[str,int] = dict()
        for i in range(0,len(args)):
            arg:str = str(args[i])
            if arg == "--":
                pass
            elif arg.startswith("-"):
                if "=" in arg or ":" in arg:
                    if "=" in arg:
                        prefix = arg[:arg.index("=") + 1]
                    else:
                        prefix = arg[:arg.index(":") + 1]
                    if prefix in self.ArgumentToFirstIndex:

                    pass
                else:
                    if arg in self.ArgumentToFirstIndex:
                        self.UsedArguments[i] = True
                    else:
                        self.ArgumentToFirstIndex[arg] = i

                    self.FlagArguments[i] = True

    def Count(self):
        return len(self.Arguments)
    def __getitem__(self, item):
        if isinstance(item,int):
            return self.Arguments[item]
        else:
            raise Exception("operator [],item type (%s) is mismatch int" % type(item))