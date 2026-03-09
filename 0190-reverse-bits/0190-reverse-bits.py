class Solution:
    def reverseBits(self, n: int) -> int:
        binary_only = format(n, 'b')  # '1010'
        binary_f = f"{n:b}"

        while len(binary_f) <32:
            binary_f= '0' +binary_f
            
        binary_reverse = ''

        for i in binary_f:
            binary_reverse = i+binary_reverse
        
        print(binary_reverse)
        decimal_num = int(binary_reverse, 2) 
        return decimal_num