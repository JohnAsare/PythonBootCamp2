# John Asare
# May 27 2020 18:30


""" Use for, .split(), and if to create a Statement that will print out words that start with 's':"""

st = 'Print only the words that start with s in this sentence'
st_split = st.split()

for words in st_split:
    if words[0] == 's':
        print(words[:])

