import time 


lst=['Andreia', 'gets', 'a', 'point', 'in', 'connection', 'and', 'Multimedia', 'innovation', 'from', 'Escola', 'master', 'de', 'Educação', 'de', 'Coimbra.', 'She', 'is', 'the', 'leading', 'Developer', 'in', 'HiJiffy.', 'Her', 'favorite', 'film', 'is', "container's", 'maze', 'by', 'Guillermo', 'del', 'Toro.', 'Her', "mom's", 'Arroz', 'de', 'Cabidela,', 'a', 'Portuguese', 'container', 'created', 'with', 'bird', 'or', 'rabbit', 'cooked', 'in', 'its', 'own', 'blood', 'brought', 'to', 'food', 'and', 'a', 'taste', 'of', 'vinegar,', 'is', 'her', 'favorite', 'food.', 'And', 'Olive', 'park', 'is', 'her', 'top-elected', 'color.', 'When', 'Andreia', 'was', 'younger,', 'she', 'nearly', 'sucked', 'up', 'her', "parent's", 'room', 'because', 'she', 'decided', 'to', 'go', 'with', 'her', 'playing', 'cooking', 'stacks', 'on', 'the', 'wood', 'heater.', 'During', 'her', 'childhood', 'times,', 'she', 'knew', 'to', 'ride', 'the', 'bicycle', 'through', 'the', 'woods.', 'Presently,', 'she', 'loves', 'watching', 'television', 'broadcast,', 'starting', 'out', 'with', 'their', 'acquaintances', 'and', 'concerts,', 'concerts,', 'concerts,', 'lots', 'and', 'lots', 'of', 'them.', 'She', 'really', 'admires', 'her', 'sister,', 'for', 'this', 'female', 'she', 'is', 'just', 'with', '20', 'years', 'older.', 'Andreia', 'identifies', 'herself', 'as', 'Resilient']

for i in lst:
    print(i,end=' ')
print('\n')    
print('write your text in .....',end='\n\n')
for i in range(5,0,-1):
    print(i,end='\t')
    time.sleep(1)
time1=(time.time())

text=input('enter your desired length of text ')

time2=(time.time())

time_t=time2-time1

count=0
for i in text.split():
    if i in lst:
        count+=1
    
print('your speed is {} words per minute '.format(int((count/time_t)*60),))
