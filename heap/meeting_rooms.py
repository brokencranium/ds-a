from typing import List, Tuple, Optional
import heapq


# setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
# Can use the schedule object instead of tuple. Heapq supports the first
# value of tuple for comparisons
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        filled_count = 0
        max_count = 0

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        schedules = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        for start_time, end_time in intervals:
            if not schedules:
                heapq.heappush(schedules, end_time)
                filled_count = max_count = 1
                continue

            if start_time >= schedules[0]:
                while schedules and start_time >= schedules[0]:
                    heapq.heappop(schedules)
                    filled_count -= 1

                heapq.heappush(schedules, end_time)
                filled_count += 1
            else:
                heapq.heappush(schedules, end_time)
                filled_count += 1
                max_count = max_count if filled_count < max_count else filled_count

        return max_count


if __name__ == '__main__':
    schedules = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 20]]
    sol = Solution()
    print(sol.minMeetingRooms(schedules))

    # meetings = [[0, 30], [5, 10], [15, 20]]
    # sol = Solution()
    # print(sol.minMeetingRooms(meetings))
