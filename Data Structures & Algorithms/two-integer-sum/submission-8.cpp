class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < (int)nums.size(); i++) {
            auto it = seen.find(target - nums[i]);          // set iterator
            if (it != seen.end()) {                         // found key
                int idx = it->second;                       // retreive idx
                return {idx, i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
