def next_player(player, player_count):
    next_p = min(player + 1, (player + 1) % player_count)
    return next_p