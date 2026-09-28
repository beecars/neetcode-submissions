class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (const string& s : strs) {
            string skey(26, 0);
            for (char c : s) {                
                skey[c - 'a']++;
            }
            groups[skey].push_back(s);
        }
        vector<vector<string>> res;
        res.reserve(groups.size());
        for (auto& [k, v] : groups) {
            res.push_back(std::move(v));
        }
        return res;
    }
};
