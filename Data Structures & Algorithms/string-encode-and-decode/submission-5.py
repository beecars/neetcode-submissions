class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        """
        enc_str = ''
        for s in strs:
            enc_str += f'{len(s)}#' + s

        print(enc_str)
        return enc_str

    def decode(self, s: str) -> List[str]:
        """
        """
        strs = []
        i = 0
        while i < len(s):
            j = 1
            while s[i+j] != "#":
                j += 1
            str_len = int(s[i:i+j])
            str_start = i + j + 1
            i = str_start + str_len
            strs.append(s[str_start:i])
        
        return strs
