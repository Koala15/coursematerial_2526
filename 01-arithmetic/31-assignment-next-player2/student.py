def next_player2(player, player_count):
    next_p = min(player + 1, (player % player_count) + 1)
    return next_p