# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n==0:
            return 0
            
        buf4 = [""] * 4
        n4, n_read, i  = 4, 0, 0
        temp_n = n
        while temp_n > 0 and n4 == 4:
            n4 = read4(buf4)
            buf[i*4:i*4+n4] = buf4
            n_read += n4
            temp_n -= n4
            i += 1

        return min((i-1)*4 + n4, n)
            
        