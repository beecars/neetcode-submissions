class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        for num in nums:

            counts[num] = counts.get(num, 0) + 1

        desc_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

        topk = []
        idx = 0
        while len(topk) < k:
            topk.append(desc_counts[idx][0])
            idx += 1

        return topk