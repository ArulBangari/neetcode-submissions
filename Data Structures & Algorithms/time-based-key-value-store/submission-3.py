class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        info = self.dictionary[key]

        if len(info) == 0:
            return ""

        l, r = 0 , len(info) - 1
        res = l
        while l <= r:
            m = (l + r) // 2
            if info[m][1] > timestamp:
                r = m - 1
            elif info[m][1] < timestamp:
                res = m
                l = m + 1
            else:
                return info[m][0]
        if info[res][1] <= timestamp:
            return info[res][0]
        return ""