class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        """
        
        output = []
        n = len(nums)

        snums = sorted(nums)

        for iidx in range(n-2):
            
            jidx = iidx + 1
            kidx = n - 1

            if iidx > 0 and snums[iidx] == snums[iidx-1]:
                continue

            while jidx < kidx:

                s = snums[iidx] + snums[jidx] + snums[kidx]
                if  s == 0:
                    output.append([snums[iidx], snums[jidx], snums[kidx]])
                    ogkidx = kidx
                    while jidx < kidx and snums[ogkidx] == snums[kidx]:
                        kidx -= 1
                    ogjidx = jidx
                    while jidx < kidx and snums[ogjidx] == snums[jidx]:
                        jidx += 1
                    
                elif s > 0:   
                    ogkidx = kidx
                    while jidx < kidx and snums[ogkidx] == snums[kidx]:
                        kidx -= 1
                elif s < 0:
                    ogjidx = jidx
                    while jidx < kidx and snums[ogjidx] == snums[jidx]:
                        jidx += 1

        return output