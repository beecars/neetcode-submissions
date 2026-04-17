class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        top_k = []
        num_ctr = {}
        for num in nums:
            num_ctr[num] = num_ctr.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in zip(num_ctr.keys(), num_ctr.values()):
            freq[count].append(num)

        print(freq)
        for fbin in reversed(freq):
            if len(top_k) == k:
                break
            for num in fbin:
                top_k.append(num)
                if len(top_k) == k:
                    break 
        
        return top_k