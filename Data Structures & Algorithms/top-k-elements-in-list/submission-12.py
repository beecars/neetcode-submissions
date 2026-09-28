class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in num_count.items():
            buckets[count].append(num)

        top_k = []
        for bucket in reversed(buckets):
            for num in bucket:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k




