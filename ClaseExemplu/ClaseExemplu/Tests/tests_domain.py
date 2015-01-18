from Domain.movie import movie
from Domain.client import client

def movie_Tests():
    movie1=movie(1, "Avatar", "Sci-fi", "James Cameron")
    assert movie1.getID() == 1
    assert movie1.getTitle() == "Avatar"
    assert movie1.getGenre() == "Sci-Fi"
    assert movie1.getDirector() == "James Cameron"

    movie2=movie(1, "interstellar", "Sci-Fi", "Christopher Nolan")
    assert movie2.getID() == 1
    assert movie2.getTitle() == "Interstellar"
    assert movie2.getGenre() == "Sci-Fi"
    assert movie2.getDirector() == "Christopher Nolan"



def client_Tests():
    client1 = client(1, "Ilie gabriel-Sorin", "1950315456698")
    client2 = client(2, "Pop Ioan", "1980114963521")
    assert client1.getID() == 1
    assert client1.getName() == "Ilie Gabriel-Sorin"
    assert client1.getCNP() == "1950315456698"
    assert client2.getID() == 2
    assert client2.getName() == "Pop Ioan"
    assert client2.getCNP() == "1980114963521"
    assert client1 != client2



client_Tests()
movie_Tests()