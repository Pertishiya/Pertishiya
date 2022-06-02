def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print("Anagram")
    else:
        print("Not Anagram")

anagram("vikes","lives")