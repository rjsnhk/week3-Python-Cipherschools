# user_info={
#     'name':'raj',
#     'age':19,
#     'movie':['kgf','rrr','mca'],
#     'song':['humnava','let me']
# }
user={}
name=input('what is ur name: ')
age=input('what is ur age: ')
movie=input('what is ur fav_movie: ').split(',')
song=input('what is ur fav_song: ').split(',')

user['name']=name
user['age']=age
user['movie']=movie
user['song']=song
print(user)