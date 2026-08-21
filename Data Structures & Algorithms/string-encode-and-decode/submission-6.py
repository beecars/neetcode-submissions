class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        """
        encoded_strs = ""
        for s in strs:
            encoded_strs += f'{len(s)}#' + s

        return encoded_strs

    def decode(self, s: str) -> List[str]:
        """ 
        """
        strs = []
        str_idx = 0

        while str_idx < len(s):
            len_code_idx = s.index('#', str_idx)
            substr_len = int(s[str_idx:len_code_idx])
            str_idx = len_code_idx + 1
            substr = s[str_idx:str_idx+substr_len]
            strs.append(substr)

            str_idx = str_idx + substr_len
        
        return strs

        



