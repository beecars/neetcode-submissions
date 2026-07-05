class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        for num in nums:

            counts[num] = counts.get(num, 0) + 1

        most_frequent = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        return [count[0] for count in most_frequent[:k]]