class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()          # INDEXES of candidates, their values tallest → shortest
        result = []
        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()                      # 1. kick shorter people from the back
            q.append(right)                  # 2. the newcomer joins at the back

            if q[0] <= right - k:
                q.popleft()                  # 3. the front person slid out of the window

            if right >= k - 1:               # 4. window is full size
                result.append(nums[q[0]])    #    the front is the max
        return result