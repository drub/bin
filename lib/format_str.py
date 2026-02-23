#!/usr/bin/env python3

# ----------------------------------------------------------------------
# Library Config
# ----------------------------------------------------------------------
__version__ = "2.0"


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



# --------------------------------------------------
def DotCol (prefix, label_col, label, value_col, value):
# --------------------------------------------------
# Format a label-value pair with dot padding for columnar alignment.
#
# prefix    : leading string, e.g. "** "
# label_col : column where label begins (0-indexed); normally len(prefix)
# label     : left-hand side label text
# value_col : column where value text begins (0-indexed)
#             " ." separator occupies value_col-2 and value_col-1
#             dot field fills from end of (label + " ") to value_col-3
#             minimum 3 dots enforced; label truncated with "*" if too long
# value     : right-hand side value text
#
# Output:  prefix + label + " " + "."*n + " ." + value + "."
#
# Example:
# DotCol("** ", 3, "progName", 31, "contact")
# DotCol("** ", 3, "File search list", 31, "/tmp/contacts.txt")
#
# Produces:
# ** progName ................. .contact.
# ** File search list ......... ./tmp/contacts.txt.
#

    out_prefix = (prefix + " " * label_col)[:label_col]
    max_label_len = value_col - label_col - 6  # 6 = 1 space + 3 min dots + " ."
    if len(label) > max_label_len:
        label = label[:max_label_len - 1] + "*"
    dot_count = value_col - label_col - len(label) - 3  # 3 = 1 space + " ."
    if label:
        return f"{out_prefix}{label} {'.' * dot_count} .{value}."
    else:
        return f"{out_prefix}{'.' * (dot_count + 1)} .{value}."


# --------------------------------------------------
def Test_DotCol ():
# --------------------------------------------------
# Run unit tests on DotCol.
# Compares actual output to expected output.
# Reports pass/fail for each test and a summary.

    pass_count = 0
    fail_count = 0

    tests = [
        # (prefix, label_col, label, value_col, value, expected)

        # --- Baseline ---
        ("** ", 3, "0",                31, "$0",                "** 0 ........................ .$0."),
        ("** ", 3, "1",                31, "$1",                "** 1 ........................ .$1."),
        ("** ", 3, "progName",         31, "contact",           "** progName ................. .contact."),
        ("** ", 3, "progVer",          31, "8.0",               "** progVer .................. .8.0."),
        ("** ", 3, "File search list", 31, "/tmp/contacts.txt", "** File search list ......... ./tmp/contacts.txt."),

        # --- Edge case: label too long, truncated with "*", minimum 3 dots ---
        ("** ", 3, "A very long label that exceeds the column", 31, "val",
         "** A very long label tha* ... .val."),

        # --- Different prefix sizes ---
        ("* ",   2, "progName", 31, "contact", "* progName .................. .contact."),
        ("** ",  3, "progName", 31, "contact", "** progName ................. .contact."),
        ("*** ", 4, "progName", 31, "contact", "*** progName ................ .contact."),

        # --- Different values ---
        ("** ", 3, "progName", 31, "",                         "** progName ................. .."),
        ("** ", 3, "progName", 31, "42",                       "** progName ................. .42."),
        ("** ", 3, "progName", 31, "a very long value string", "** progName ................. .a very long value string."),

        # --- value_col group A: value_col=31 ---
        ("** ", 3, "label", 31, "x",                     "** label .................... .x."),
        ("** ", 3, "label", 31, "medium value",           "** label .................... .medium value."),
        ("** ", 3, "label", 31, "a longer value string",  "** label .................... .a longer value string."),

        # --- value_col group B: value_col=40 ---
        ("** ", 3, "label", 40, "x",                     "** label ............................. .x."),
        ("** ", 3, "label", 40, "medium value",           "** label ............................. .medium value."),
        ("** ", 3, "label", 40, "a longer value string",  "** label ............................. .a longer value string."),

        # --- No prefix ---
        ("", 0, "progName", 31, "contact", "progName .................... .contact."),
        ("", 0, "progName", 31, "",        "progName .................... .."),
        ("", 0, "",          31, "contact", "............................. .contact."),

        # --- Prefix "=" ---
        ("=",   1, "progName", 31, "contact", "=progName ................... .contact."),
        ("=",   1, "",          31, "contact", "=............................ .contact."),
        ("=",   1, "progName", 31, "",         "=progName ................... .."),

        # --- Prefix "==" ---
        ("==",  2, "progName", 31, "contact", "==progName .................. .contact."),
        ("==",  2, "",          31, "contact", "==........................... .contact."),
        ("==",  2, "progName", 31, "",         "==progName .................. .."),

        # --- Prefix "-->" ---
        ("-->", 3, "progName", 31, "contact", "-->progName ................. .contact."),
        ("-->", 3, "",          31, "contact", "-->.......................... .contact."),
        ("-->", 3, "progName", 31, "",         "-->progName ................. .."),

        # --- No label ---
        ("** ", 3, "", 31, "contact", "** .......................... .contact."),
        ("* ",  2, "", 31, "contact", "* ........................... .contact."),
        ("",    0, "", 31, "contact", "............................. .contact."),

        # --- No value ---
        ("** ", 3, "progName", 31, "", "** progName ................. .."),
        ("** ", 3, "",          31, "", "** .......................... .."),
        ("",    0, "progName", 31, "", "progName .................... .."),

        # --- Combinations: no prefix + no label + no value ---
        ("", 0, "", 31, "contact", "............................. .contact."),
        ("", 0, "", 31, "val",     "............................. .val."),
        ("", 0, "", 31, "",        "............................. .."),

        # --- value_col group C: value_col=20 ---
        ("** ", 3, "label", 20, "x",                     "** label ......... .x."),
        ("** ", 3, "label", 20, "medium value",           "** label ......... .medium value."),
        ("** ", 3, "label", 20, "a longer value string",  "** label ......... .a longer value string."),

        # --- value_col group D: value_col=50 ---
        ("** ", 3, "label", 50, "x",                     "** label ....................................... .x."),
        ("** ", 3, "label", 50, "medium value",           "** label ....................................... .medium value."),
        ("** ", 3, "label", 50, "a longer value string",  "** label ....................................... .a longer value string."),

        # --- value_col group E: value_col=60 ---
        ("** ", 3, "label", 60, "x",                     "** label ................................................. .x."),
        ("** ", 3, "label", 60, "medium value",           "** label ................................................. .medium value."),
        ("** ", 3, "label", 60, "a longer value string",  "** label ................................................. .a longer value string."),

        # --- value_col group F: value_col=70 ---
        ("** ", 3, "label", 70, "x",                     "** label ........................................................... .x."),
        ("** ", 3, "label", 70, "medium value",           "** label ........................................................... .medium value."),
        ("** ", 3, "label", 70, "a longer value string",  "** label ........................................................... .a longer value string."),

        # --- prefix "-----", label_col 2,3,4,5,6,7,8 ---
        ("-----", 2, "label", 31, "val", "--label ..................... .val."),
        ("-----", 3, "label", 31, "val", "---label .................... .val."),
        ("-----", 4, "label", 31, "val", "----label ................... .val."),
        ("-----", 5, "label", 31, "val", "-----label .................. .val."),
        ("-----", 6, "label", 31, "val", "----- label ................. .val."),
        ("-----", 7, "label", 31, "val", "-----  label ................ .val."),
        ("-----", 8, "label", 31, "val", "-----   label ............... .val."),
    ]

    print("-" * 60)
    print("Test_DotCol")
    print("-" * 60)

    test_num = 0
    for prefix, label_col, label, value_col, value, expected in tests:
        test_num += 1
        result = DotCol(prefix, label_col, label, value_col, value)
        counter = f"[{test_num:02d}] "
        if result == expected:
            pass_count += 1
            print(f"  {counter}PASS: {result}")
        else:
            fail_count += 1
            print(f"  {counter}FAIL:")
            print(f"    expected: {expected}")
            print(f"    actual:   {result}")

    print("-" * 60)
    print(f"  {pass_count} passed, {fail_count} failed")
    print("-" * 60)


'''
# ----------------------------------------------------------------------
# Usage - importing this library from another program
# ----------------------------------------------------------------------
#
# import os, sys
# lib_path = os.environ['HOME'] + "/bin/lib"
# sys.path.append(lib_path)
# import format_str
# from format_str import StrCol, DotCol
#
# Query the library version:
# print(format_str.__version__)
#
# ----------------------------------------------------------------------
# History HISTORY history
# ----------------------------------------------------------------------

# --------------------------------------------------
# Ver: 2.0
# 2026-02-22
# --------------------------------------------------
- Add DotCol() function for dot-padded columnar label/value formatting
    prefix, label_col, label, value_col, value
    label starts at label_col, overwriting or padding prefix
    dots fill from end of label to value_col
    minimum 3 dots enforced; label truncated with "*" if too long
    empty label: dots start at column 0 (no leading space)
    value wrapped in dots: .value.
- Add Test_DotCol() unit test function for DotCol
    58 test cases covering baselines, edge cases, prefix sizes,
    empty label/value/prefix, value_col groups, prefix overwrite
    numbered output: [nn] PASS/FAIL
- Add __version__ = "2.0" (standard Python convention)
- Add usage guidance for importing this library

# --------------------------------------------------
# Ver: 1.0
# --------------------------------------------------
- Original StrCol() function

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

print("+" * 70)
print("DotCol tests")
print("+" * 70)

print(DotCol("** ", 3, "0",                31, "$0"))
print(DotCol("** ", 3, "1",                31, "$1"))
print(DotCol("** ", 3, "progName",         31, "contact"))
print(DotCol("** ", 3, "progVer",          31, "8.0"))
print(DotCol("** ", 3, "File search list", 31, "/tmp/contacts.txt"))

# Expected results:
# ** 0 ........................ .$0.
# ** 1 ........................ .$1.
# ** progName ................. .contact.
# ** progVer .................. .8.0.
# ** File search list ......... ./tmp/contacts.txt.
'''
