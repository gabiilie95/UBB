import unittest
from Domain.client import client
from Domain.movie import movie
from Domain.rent import rent

def test_client():
    
    '''Teste Get'''

    client1 = client('1', 'gabi', '1234567890')
    assert client1.getID() == '1'
    assert client1.getName() == 'Gabi'
    assert client1.getCNP() == '1234567890'
    
    client2 = client('2', 'dan ioan', '0987654321')
    assert client2.getID() == '2'
    assert client2.getName() == 'Dan Ioan'
    assert client2.getCNP() == '0987654321'

    assert client1 != client2

    '''Teste Set'''
    
    client1.setID('3')
    client1.setName('Gabi ilie')
    client1.setCNP('0987654321')
    assert client1.getID() == '3'
    assert client1.getName() == 'Gabi Ilie'
    assert client1.getCNP() == '0987654321'

    client2.setID('4')
    client2.setName('dan')
    client2.setCNP('1234567890')
    assert client2.getID() == '4'
    assert client2.getName() == 'Dan'
    assert client2.getCNP() == '1234567890'

    assert client1 != client2

def test_movie():

    '''Teste Get'''

    movie1 = movie('1', 'avatar', 'James cameron', 'sci-fi')
    assert movie1.getID() == '1'
    assert movie1.getTitle() == 'Avatar'
    assert movie1.getDirector() == 'James Cameron'
    assert movie1.getGenre() == 'Sci-Fi'

    movie2 = movie('2', 'goodfellas', 'martin Scorsese', 'Drama')
    assert movie2.getID() == '2'
    assert movie2.getTitle() == 'Goodfellas'
    assert movie2.getDirector() == 'Martin Scorsese'
    assert movie2.getGenre() == 'Drama'

    assert movie1 != movie2

    '''Teste Set'''

    movie1.setID('3')
    movie1.setTitle('Casino')
    movie1.setDirector('Martin Scorsese')
    movie1.setGenre('Drama')
    assert movie1.getID() == '3'
    assert movie1.getTitle() == 'Casino'
    assert movie1.getDirector() == 'Martin Scorsese'
    assert movie1.getGenre() == 'Drama'

    movie2.setID('4')
    movie2.setTitle('star wars ep. 7')
    movie2.setDirector('j.j. abrams')
    movie2.setGenre('Sci-fi')
    assert movie2.getID() == '4'
    assert movie2.getTitle() == 'Star Wars Ep. 7'
    assert movie2.getDirector() == 'J.J. Abrams'
    assert movie2.getGenre() == 'Sci-Fi'

    assert movie1 != movie2

def test_rent():

    '''Teste Get'''

    rent1 = rent(1, 2)
    assert rent1.getIDC() == 1
    assert rent1.getIDM() == 2
    assert rent1.getIsRented() == True

    rent2 = rent(3, 4)
    assert rent2.getIDC() == 3
    assert rent2.getIDM() == 4
    assert rent2.getIsRented() == True

    '''Teste Set'''

    rent1.setIDC(5)
    rent1.setIDM(6)
    rent1.setIsNotRented()
    assert rent1.getIDC() == 5
    assert rent1.getIDM() == 6
    assert rent1.getIsRented() == False

    rent2.setIDC(7)
    rent2.setIDM(8)
    rent2.setIsNotRented()
    assert rent2.getIDC() == 7
    assert rent2.getIDM() == 8
    assert rent2.getIsRented() == False
