# Meeting Rooms II


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        used_rooms = 0

        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])
        l = len(intervals)

        end_pointers = 0
        start_pointers = 0

        while start_pointers < l:
            if start_timings[start_pointers] >= end_timings[end_pointers]:
                used_rooms -= 1
                end_pointers += 1
            used_rooms += 1
            start_pointers += 1
        return used_rooms
