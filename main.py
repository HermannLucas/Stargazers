import neighbours

auth_token = "Bearer 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"
f = neighbours.get_neighbours("HermannLucas", "AdeventOfCode", auth_token)
print(f)
