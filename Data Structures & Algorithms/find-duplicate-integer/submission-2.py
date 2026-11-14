class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]          # 🐢 1 jump
            fast = nums[nums[fast]]    # 🐇 2 jumps
            if slow == fast:           # same ROOM?
                break                  # we're inside the loop, stop

        slow2 = 0                      # 
        while slow != slow2:
            slow = nums[slow]          # 1 jump
            slow2 = nums[slow2]        # 1 jump
        return slow  
        