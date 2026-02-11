#!/Users/thedrub/anaconda3/bin/python


# --------------------------------------------------
def StrCol (base_str, new_str, start_pos):
# --------------------------------------------------
# Place a new string at a certain postion in a base string
#
# Example
# StrCol("-------------------------- ", " New string ", 10)
#
# Produces:
# ---------- New string ---- 
#
# Truncates the new_str if there is insufficient space in base_str
#

    base_str_len = len(base_str)
    new_str_len = len(new_str)
    ret_str = base_str[0:start_pos]
    ret_str_len = len(ret_str)

    if [start_pos < base_str_len]:
        # Only add the postio of the string that will fit in the base_str.
        char_count_to_add = base_str_len - ret_str_len
        #print("++ base_str_len ............." + str(base_str_len)) #debug
        #print("++ new_str_len .............." + str(new_str_len)) #debug
        #print("++ ret_str_len .............." + str(ret_str_len)) #debug
        #print("++ Chars to add ............." + str(char_count_to_add)) #debug
        ret_str = ret_str + new_str[0:char_count_to_add]

    ret_str = ret_str + base_str[(start_pos + new_str_len):base_str_len]

    return(ret_str)

'''
# ----------------------------------------------------------------------
# Unit Tests
# ----------------------------------------------------------------------
print("+" * 70)

str3 = StrCol("-" * 50, " First ", 5)
print(str3)

str4 = StrCol(str3, " Second ", 20)
print(str4)
# Expected results
#----- First -------- Second ----------------------

print("+" * 70)

str5 = "-" * 50
print(str5)

str6 = StrCol(str5, " First ", 5)
print(str6)

str7 = StrCol(str6, " Second ", 20)
print(str7)

str8 = StrCol(str7, " Third ", 47)
print(str8)

# Expected results
#----- First -------- Second ------------------- Th
'''
