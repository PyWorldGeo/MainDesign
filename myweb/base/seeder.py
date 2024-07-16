from .models import Author, Genre


def seeder_func():
    authors = ['Arthur Conan Doyle', 'Franz Kafka', 'Mark Twain', 'William Faulkner', 'F. Scott Fitzgerald']
    genres = ['Drama', 'Fantasy', "Fiction", 'Folklore', 'Horror', 'Fairy Tale']

    for author in authors:
        if not Author.objects.filter(name=author):
            new_author = Author(name=author)
            new_author.save()

    for genre in genres:
        if not Genre.objects.filter(name=genre):
            new_genre = Genre(name=genre)
            new_genre.save()

