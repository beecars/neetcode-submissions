class Solution:

    def encode(self, strs: List[str]) -> str:
        
        enc_str = ''
        for s in strs:
            len_s = len(s)
            enc_str += f'{len_s}#{s}'
        
        return enc_str

    def decode(self, s: str) -> List[str]:
        
        dec_strs = []
        sidx = 0
        while sidx < len(s):
            substr_begin = s.find('#', sidx) + 1
            substr_len = int(s[sidx:substr_begin - 1])
            substr = s[substr_begin:substr_begin + substr_len]
            sidx = substr_begin + substr_len
            dec_strs.append(substr)

        return dec_strs
