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
        plan="clay",
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
        # if minute == 1:
        #    yield "start"
        #    return
        if self.obs_bots > 0 and minute >= 12:
            yield "geo"
            if minute >= 30:
                return
        if self.clay_bots < self.blueprint.obs_clay and minute <= 30 and self.clay < 40:
            yield "clay"
        # if self.ore_bots <= 4:
        #    yield "ore"
        if (
            self.clay_bots > 0
            and minute >= 4
            and self.obs_bots <= self.blueprint.geo_obs
            and self.obs < 40
        ):
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


def eval_blueprint(time, start_candidate=None, start_time=1):
    print()
    print(start_candidate.blueprint)
    candidates = [start_candidate]
    for minute in range(start_time, time + 1):
        candidates = propagate(candidates, minute)
        bestclay = max([cand.clay for cand in candidates])
        bestobs = max([cand.obs for cand in candidates])
        bestgeo = max([cand.geo for cand in candidates])
        print(
            f"minute: {minute:4}    max_geo: {bestgeo:3}    max_obs: {bestobs:3}    max_clay: {bestclay:3}    candidates: {len(candidates)}"
        )

    return max(cand.geo for cand in candidates)


def solve2(data, time):
    """We start with pre-built ore bots"""
    blueprints = parse(data)[:3]
    # blueprint #1: first actions: ---R-R-
    start = Candidate(
        blueprints[0],
        ore_bots=3,
        ore=5,
    )
    a = eval_blueprint(time, start, start_time=8)
    print(a)

    # blueprint #2: first actions: --R-R
    start = Candidate(
        blueprints[1],
        ore_bots=3,
        ore=3,
    )
    b = eval_blueprint(time, start, start_time=6)
    print(b)

    # blueprint #3: first actions: ----R--R-
    # MORE EFFICIENT THAN BUILDING A 4th ORE BOT
    start = Candidate(
        blueprints[2],
        ore_bots=3,
        ore=6,
    )
    c = eval_blueprint(time, start, start_time=10)
    print(c)

    return a * b * c


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve2(input_data, time=32)
    print(f"Solution part 2: {result}")
