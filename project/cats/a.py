def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    i = 0
    def dif(start,goal,i):
        if i > limit:
            return i
        elif len(goal) == 0:
            return i + len(start) - len(goal)
        elif len(start) == 0:
            return i + len(goal) - len(start)
        elif start[0] != goal[0]:
            add_diff = shifty_shifts(goal[0] + start, goal, limit)
            remove_diff = shifty_shifts(start[1:], goal, limit)
            substitute_diff = shifty_shifts(goal[0] + start[1:], goal, limit)
            all = min(add_diff, remove_diff, substitute_diff)
            if(all == 0):
                return i
            else:
                i += 1
                return dif(start[1:],goal[1:],i)
        else:
            return dif(start[1:],goal[1:],i)
        
    if start == goal:
        return 0
    elif len(start) == 0:
        return len(goal)
    elif len(goal) == 0:
        return len(start)
    else:
        return dif(start=start, goal=goal,i=i)