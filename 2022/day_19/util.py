import re

from pydantic import BaseModel


class Blueprint(BaseModel):
    number: int
    ore_ore: int
    clay_ore: int
    obs_ore: int
    obs_clay: int
    geo_ore: int
    geo_obs: int


def parse(data):
    # Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 3 ore and 19 obsidian.
    blueprints = []
    for bp in data.split("Blueprint")[1:]:
        number, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = map(
            int, re.findall(r"\d+", bp)
        )
        blueprints.append(
            Blueprint(
                number=number,
                ore_ore=ore_ore,
                clay_ore=clay_ore,
                obs_ore=obs_ore,
                obs_clay=obs_clay,
                geo_ore=geo_ore,
                geo_obs=geo_obs,
            )
        )
    return blueprints
