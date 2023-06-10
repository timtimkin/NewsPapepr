# Создать двух пользователей (с помощью метода User.objects.create_user).

user1 = User.objects.create(username='Tim', first_name='Tim')
user2 = User.objects.create(username='Den', first_name='Den')

# Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(authorUser=user1)
Author.objects.create(authorUser=user2)

# Добавить 4 категории в модель Category.
Category.objects.create(nameNews='IT')
Category.objects.create(nameNews='SPORT')
Category.objects.create(nameNews='BUSINESS')
Category.objects.create(nameNews='AUTO')

#Добавить 2 статьи и 1 новость.
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Tim')), newsType='NW',
                    header='header', textPublication='mnogo bukv')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Tim')), newsType='AR',
                    header='header2', textPublication='mnogo bukv')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Den')), newsType='AR',
                    header='header3', textPublication='o4enb mnogo bukv')

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)

c1 = Category.objects.get(nameNews='IT')
c2 = Category.objects.get(nameNews='AR')

p1.category.add(c1)
p2.category.add(c1, c2)
p3.category.add(c2)

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
Comment.objects.create(commentUser=User.objects.get(username='Tim'), commentPost=Post.objects.get(pk=1), textComment='mnogo bukv')
Comment.objects.create(commentUser=User.objects.get(username='Tim'), commentPost=Post.objects.get(pk=2), textComment='NORM')
Comment.objects.create(commentUser=User.objects.get(username='Den'), commentPost=Post.objects.get(pk=3), textComment='plohoy post dislike')
Comment.objects.create(commentUser=User.objects.get(username='Den'), commentPost=Post.objects.get(pk=2), textComment='HOROSHIY post like')

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).dislike()

Comment.objects.get(pk=1).dislike()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).like()

# Обновить рейтинги пользователей.
Author.objects.get(authorUser=User.objects.get(username='Den')).update_rating()
Author.objects.get(authorUser=User.objects.get(username='Tim')).update_rating()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
a = Author.objects.get(authorUser=User.objects.get(username='Tim'))
b = Author.objects.get(authorUser=User.objects.get(username='Den'))

a.rating
b.rating

best = Author.objects.all().order_by('rating').values('authorUser', 'rating')[0]
print(best)

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
Post.objects.annotate(likes-F('like') - F('dislike)).order_by('likes').first()

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
comments = Comment.objects.filter(article=article)
for comment in comments:
print('datePublication', comment.datePublication)
print('User', comment.user.username)
print('Rating', comment.rating)
print('textComment'. comment.textComment)