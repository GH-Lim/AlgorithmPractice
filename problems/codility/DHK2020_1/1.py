from typing import List, Text


class NoAgentFoundException(Exception):
    def __init__(self):
        super().__init__('NoAgentFoundException')


class Agent(object):
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load
        self.skills_cnt = len(skills)

    def __str__(self):
        return "<Agent: {}>".format(self.name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        agents = sorted(agents, key=lambda x: (x.skills_cnt, x.load))
        return agents

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        agents = self._filter_loaded_agents(agents)
        if not agents:
            raise NoAgentFoundException
        for agent in agents:
            return agent


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        agents = sorted(agents, key=lambda x: x.load)
        if not agents:
            raise NoAgentFoundException
        if agents[0].load < 3:
            return agents[0]
        else:
            raise NoAgentFoundException


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        agents = self._filter_loaded_agents(agents)
        if not agents:
            raise NoAgentFoundException
        for agent in agents:
            for res in ticket.restrictions
