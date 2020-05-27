# John Asare
# May 27 2020


""" Go through the string below and if the length of a word is even print "even!" """

st = 'Print every word in this sentence that has an even number of letters'
split_st = st.split()

for word in split_st:
    if len(word) % 2 == 0:
        print(f'{word} is even')
