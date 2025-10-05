def cake2(eggs, flour):
    enough_eggs = eggs // 5
    enough_flour = flour // 250
    return min(enough_eggs, enough_flour)