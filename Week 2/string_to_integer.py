class Solution:
    def myAtoi(self, s: str) -> int:
        # find sign in the first run
        total = 0  # Changed from '0' to 0
        changed = False
        sign = 1  # Changed to integer for sign handling
        
        # Existing sign detection code
        for i in s:
            if i.isalpha() or i.isdigit():
                break
            elif i == '-':
                sign = -1
                break
            elif i == '+':
                sign = 1
                break
                
        if s.strip() and s.strip()[0] == '.':
            return 0  # Return 0 for ".1"
            
        # Existing number parsing code
        for i in s:
            if i == ' ':
                continue
            else:
                if i.isalpha():
                    if total == 0 and not changed:
                        return 0
                    break
                elif i.isdigit():
                    changed = True
                    total = total * 10 + int(i)  # Directly updating total as integer
                else:
                    if changed:
                        break
                    
        total *= sign  # Apply the sign directly

        # Overflow checks
        if total < -2**31:
            return -2**31
        if total > 2**31 - 1:
            return 2**31 - 1
        else:
            return total  # Directly return total
