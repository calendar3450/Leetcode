from collections import deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(set)

        for route_id, stops in enumerate(routes):
            for stop in stops:
                stop_to_routes[stop].add(route_id)

        q = deque([(source, 0)])
        visited_stop = {source}
        visited_routes = set()

        while q:
            stop,buses = q.popleft()

            for route_id in stop_to_routes[stop]:
                if route_id in visited_routes:
                    continue
                visited_routes.add(route_id)

                for nxt_stop in routes[route_id]:
                    if nxt_stop == target:
                        return buses +1

                    if nxt_stop not in visited_stop:
                        visited_stop.add(nxt_stop)
                        q.append((nxt_stop,buses+1))

        return -1