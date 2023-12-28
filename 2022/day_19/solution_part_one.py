"""
Not Enough Minerals

https://adventofcode.com/2022/day/19
"""
from collections import defaultdict
from pprint import pprint
from util import parse


class Candidate:
    """A candidate solution or part thereof"""

    def __init__(
        self,
        blueprint,
        ore_bots=1,
        clay_bots=0,
        obs_bots=0,
        geo_bots=0,
        ore=0,
        clay=0,
        obs=0,
        geo=0,
        plan="start",
    ):
        self.blueprint = blueprint
        self.ore_bots = ore_bots
        self.clay_bots = clay_bots
        self.obs_bots = obs_bots
        self.geo_bots = geo_bots
        self.ore = ore
        self.clay = clay
        self.obs = obs
        self.geo = geo
        self.plan = plan
        self._build = None

    def __repr__(self):
        return (
            f"plan: {self.plan:<6}"
            f" orb: {self.ore_bots} clb: {self.clay_bots} obsb: {self.obs_bots}, gb: {self.geo_bots}"
            f" ore: {self.ore} clay: {self.clay} obs: {self.obs} geo: {self.geo}"
        )

    @property
    def data(self):
        return (
            self.ore_bots,
            self.clay_bots,
            self.obs_bots,
            self.geo_bots,
            self.ore,
            self.clay,
            self.obs,
            self.geo,
            self.plan,
        )

    def copy(self):
        return Candidate(self.blueprint, *self.data)

    def mine(self):
        self.ore += self.ore_bots
        self.clay += self.clay_bots
        self.obs += self.obs_bots
        self.geo += self.geo_bots
        if self._build:
            self.__setattr__(self._build, self.__getattribute__(self._build) + 1)
            self._build = None

    def build_ore_bot(self):
        if self.ore >= self.blueprint.ore_ore:
            self.ore -= self.blueprint.ore_ore
            self._build = "ore_bots"
            return True

    def build_clay_bot(self):
        if self.ore >= self.blueprint.clay_ore:
            self.ore -= self.blueprint.clay_ore
            self._build = "clay_bots"
            return True

    def build_obs_bot(self):
        if self.ore >= self.blueprint.obs_ore and self.clay >= self.blueprint.obs_clay:
            self.ore -= self.blueprint.obs_ore
            self.clay -= self.blueprint.obs_clay
            self._build = "obs_bots"
            return True

    def build_geo_bot(self):
        if self.ore >= self.blueprint.geo_ore and self.obs >= self.blueprint.geo_obs:
            self.ore -= self.blueprint.geo_ore
            self.obs -= self.blueprint.geo_obs
            self._build = "geo_bots"
            return True

    def build_bot(self):
        return {
            "ore": self.build_ore_bot,
            "clay": self.build_clay_bot,
            "obs": self.build_obs_bot,
            "geo": self.build_geo_bot,
        }[self.plan]()

    def get_new_plans(self, minute):
        if minute == 1:
            yield "start"
            return
        if self.obs_bots > 0 and minute >= 9:
            yield "geo"
            if minute >= 22:
                return
        if self.clay_bots <= 8 and minute <= 20:
            yield "clay"
        if self.ore_bots <= 4:
            yield "ore"
        if self.clay_bots > 0 and minute >= 4 and self.obs_bots <= 6:
            yield "obs"

    def create_candidate(self, plan):
        cand = self.copy()
        cand._build = self._build
        cand.mine()
        cand.plan = plan
        return cand

    def get_moves(self, minute):
        if self.plan == "start":
            for plan in self.get_new_plans(minute):
                yield self.create_candidate(plan)
            return

        # build bot if possible
        cand = self.copy()
        if cand.build_bot():
            for plan in cand.get_new_plans(minute):
                yield cand.create_candidate(plan)
        else:
            # wait
            cand.mine()
            yield cand


def propagate(candidates, minute):
    new = []
    for c in candidates:
        for cc in c.get_moves(minute):
            new.append(cc)
    return new


def eval_blueprint(blueprint, time):
    candidates = [Candidate(blueprint)]
    print(blueprint)
    for minute in range(1, time + 1):
        candidates = propagate(candidates, minute)
        bestgeo = max([cand.geo for cand in candidates])
        print("minute:", minute, "best_geo:", bestgeo, "candidates:", len(candidates))

    return max(cand.geo for cand in candidates) * blueprint.number


def solve(data, time=24, cutoff=None):
    blueprints = parse(data)
    if cutoff:
        blueprints = blueprints[:cutoff]
    score = sum(eval_blueprint(bp, time) for bp in blueprints)
    return score


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data, time=24)
    print(f"Solution part 1: {result}")
    assert result == 1127
