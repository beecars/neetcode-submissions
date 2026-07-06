class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        freq_to_num = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            freq_to_num[count].append(num)

        top_nums = []
        for bucket in reversed(freq_to_num):
            while bucket:
                top_nums.append(bucket.pop())
            if len(top_nums) == k:
                return top_nums 