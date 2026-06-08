class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed, sort by position ascending
        pairs = sorted(zip(position, speed), key=lambda x: x[0])
        
        fleets = 0
        cur_max = 0.0  # arrival time of the slowest fleet ahead
        
        # Walk from the car closest to target backward
        for pos, spd in reversed(pairs):
            t = (target - pos) / spd  # time for this car to reach target alone
            if t > cur_max:
                # Can't catch the fleet ahead -> new fleet, new bottleneck
                fleets += 1
                cur_max = t
            # else: catches up and merges, cur_max unchanged
        
        return fleets

            
                

            
            