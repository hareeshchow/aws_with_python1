import boto3
import json
from decimal import Decimal


def load_movie(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie : ", year, title)
        table.put_item(Item=movie)




if __name__=="__main__":
    with open('moviedata.json') as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)


    load_movie(movie_list)


# movie dataclasses
'''
[

    {
        "year": 2013,
        "title": "Rush",
        "info": {
            "directors": ["Ron Howard"],
            "release_date": "2013-09-02T00:00:00Z",
            "rating": 8.3,
            "genres": [
                "Action",
                "Biography",
                "Drama",
                "Sport"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQyMDE0MTY0OV5BMl5BanBnXkFtZTcwMjI2OTI0OQ@@._V1_SX400_.jpg",
            "plot": "A re-creation of the merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.",
            "rank": 2,
            "running_time_secs": 7380,
            "actors": [
                "Daniel Bruhl",
                "Chris Hemsworth",
                "Olivia Wilde"
            ]
        }
    },
    {
        "year": 2013,
        "title": "Prisoners",
        "info": {
            "directors": ["Denis Villeneuve"],
            "release_date": "2013-08-30T00:00:00Z",
            "rating": 8.2,
            "genres": [
                "Crime",
                "Drama",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTg0NTIzMjQ1NV5BMl5BanBnXkFtZTcwNDc3MzM5OQ@@._V1_SX400_.jpg",
            "plot": "When Keller Dover's daughter and her friend go missing, he takes matters into his own hands as the police pursue multiple leads and the pressure mounts. But just how far will this desperate father go to protect his family?",
            "rank": 3,
            "running_time_secs": 9180,
            "actors": [
                "Hugh Jackman",
                "Jake Gyllenhaal",
                "Viola Davis"
            ]
        }
    },
    {
        "year": 2013,
        "title": "The Hunger Games: Catching Fire",
        "info": {
            "directors": ["Francis Lawrence"],
            "release_date": "2013-11-11T00:00:00Z",
            "genres": [
                "Action",
                "Adventure",
                "Sci-Fi",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTAyMjQ3OTAxMzNeQTJeQWpwZ15BbWU4MDU0NzA1MzAx._V1_SX400_.jpg",
            "plot": "Katniss Everdeen and Peeta Mellark become targets of the Capitol after their victory in the 74th Hunger Games sparks a rebellion in the Districts of Panem.",
            "rank": 4,
            "running_time_secs": 8760,
            "actors": [
                "Jennifer Lawrence",
                "Josh Hutcherson",
                "Liam Hemsworth"
            ]
        }
    },
    {
        "year": 2013,
        "title": "Thor: The Dark World",
        "info": {
            "directors": ["Alan Taylor"],
            "release_date": "2013-10-30T00:00:00Z",
            "genres": [
                "Action",
                "Adventure",
                "Fantasy"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQyNzAwOTUxOF5BMl5BanBnXkFtZTcwMTE0OTc5OQ@@._V1_SX400_.jpg",
            "plot": "Faced with an enemy that even Odin and Asgard cannot withstand, Thor must embark on his most perilous and personal journey yet, one that will reunite him with Jane Foster and force him to sacrifice everything to save us all.",
            "rank": 5,
            "actors": [
                "Chris Hemsworth",
                "Natalie Portman",
                "Tom Hiddleston"
            ]
        }
    },
    {
        "year": 2013,
        "title": "This Is the End",
        "info": {
            "directors": [
                "Evan Goldberg",
                "Seth Rogen"
            ],
            "release_date": "2013-06-03T00:00:00Z",
            "rating": 7.2,
            "genres": [
                "Comedy",
                "Fantasy"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQxODE3NjM1Ml5BMl5BanBnXkFtZTcwMzkzNjc4OA@@._V1_SX400_.jpg",
            "plot": "While attending a party at James Franco's house, Seth Rogen, Jay Baruchel and many other celebrities are faced with the apocalypse.",
            "rank": 6,
            "running_time_secs": 6420,
            "actors": [
                "James Franco",
                "Jonah Hill",
                "Seth Rogen"
            ]
        }
    },
    {
        "year": 2013,
        "title": "Insidious: Chapter 2",
        "info": {
            "directors": ["James Wan"],
            "release_date": "2013-09-13T00:00:00Z",
            "rating": 7.1,
            "genres": [
                "Horror",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTg0OTA5ODIxNF5BMl5BanBnXkFtZTcwNTUzNDg4OQ@@._V1_SX400_.jpg",
            "plot": "The haunted Lambert family seeks to uncover the mysterious childhood secret that has left them dangerously connected to the spirit world.",
            "rank": 7,
            "running_time_secs": 6360,
            "actors": [
                "Patrick Wilson",
                "Rose Byrne",
                "Barbara Hershey"
            ]
        }
    },
    {
        "year": 2013,
        "title": "World War Z",
        "info": {
            "directors": ["Marc Forster"],
            "release_date": "2013-06-02T00:00:00Z",
            "rating": 7.1,
            "genres": [
                "Action",
                "Adventure",
                "Horror",
                "Sci-Fi",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTg0NTgxMjIxOF5BMl5BanBnXkFtZTcwMDM0MDY1OQ@@._V1_SX400_.jpg",
            "plot": "United Nations employee Gerry Lane traverses the world in a race against time to stop the Zombie pandemic that is toppling armies and governments, and threatening to destroy humanity itself.",
            "rank": 8,
            "running_time_secs": 6960,
            "actors": [
                "Brad Pitt",
                "Mireille Enos",
                "Daniella Kertesz"
            ]
        }
    },
    {
        "year": 2014,
        "title": "X-Men: Days of Future Past",
        "info": {
            "directors": ["Bryan Singer"],
            "release_date": "2014-05-21T00:00:00Z",
            "genres": [
                "Action",
                "Adventure",
                "Fantasy",
                "Sci-Fi"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQ0NzIwNTA1MV5BMl5BanBnXkFtZTgwNjY2OTcwMDE@._V1_SX400_.jpg",
            "plot": "The X-Men send Wolverine to the past to change a major historical event that could globally impact man and mutant kind.",
            "rank": 9,
            "actors": [
                "Jennifer Lawrence",
                "Hugh Jackman",
                "Michael Fassbender"
            ]
        }
    },
    {
        "year": 2014,
        "title": "Transformers: Age of Extinction",
        "info": {
            "directors": ["Michael Bay"],
            "release_date": "2014-06-25T00:00:00Z",
            "genres": [
                "Action",
                "Adventure",
                "Sci-Fi"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQyMDA5Nzg0Nl5BMl5BanBnXkFtZTgwNzA4NDcxMDE@._V1_SX400_.jpg",
            "plot": "A mechanic and his daughter make a discovery that brings down Autobots and Decepticons - and a paranoid government official - on them.",
            "rank": 10,
            "actors": [
                "Mark Wahlberg",
                "Nicola Peltz",
                "Jack Reynor"
            ]
        }
    },
    {
        "year": 2013,
        "title": "Now You See Me",
        "info": {
            "directors": ["Louis Leterrier"],
            "release_date": "2013-05-21T00:00:00Z",
            "rating": 7.3,
            "genres": [
                "Crime",
                "Mystery",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTY0NDY3MDMxN15BMl5BanBnXkFtZTcwOTM5NzMzOQ@@._V1_SX400_.jpg",
            "plot": "An FBI agent and an Interpol detective track a team of illusionists who pull off bank heists during their performances and reward their audiences with the money.",
            "rank": 11,
            "running_time_secs": 6900,
            "actors": [
                "Jesse Eisenberg",
                "Common",
                "Mark Ruffalo"
            ]
        }
    },
    {
        "year": 2012,
        "title": "Pitch Perfect",
        "info": {
            "directors": ["Jason Moore"],
            "release_date": "2012-09-28T00:00:00Z",
            "rating": 7.1,
            "genres": [
                "Comedy",
                "Music",
                "Romance"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTcyMTMzNzE5N15BMl5BanBnXkFtZTcwNzg5NjM5Nw@@._V1_SX400_.jpg",
            "plot": "Beca, a freshman at Barden University, is cajoled into joining The Bellas, her school's all-girls singing group. Injecting some much needed energy into their repertoire, The Bellas take on their male rivals in a campus competition.",
            "rank": 46,
            "running_time_secs": 6720,
            "actors": [
                "Anna Kendrick",
                "Brittany Snow",
                "Rebel Wilson"
            ]
        }
    },
    {
        "year": 2012,
        "title": "The Avengers",
        "info": {
            "directors": ["Joss Whedon"],
            "release_date": "2012-04-11T00:00:00Z",
            "rating": 8.2,
            "genres": [
                "Action",
                "Fantasy"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SX400_.jpg",
            "plot": "Nick Fury of S.H.I.E.L.D. assembles a team of superhumans to save the planet from Loki and his army.",
            "rank": 48,
            "running_time_secs": 8580,
            "actors": [
                "Robert Downey Jr.",
                "Chris Evans",
                "Scarlett Johansson"
            ]
        }
    },
    {
        "year": 2012,
        "title": "The Dark Knight Rises",
        "info": {
            "directors": ["Christopher Nolan"],
            "release_date": "2012-07-16T00:00:00Z",
            "rating": 8.6,
            "genres": [
                "Action",
                "Crime",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_SX400_.jpg",
            "plot": "Eight years on, a new evil rises from where the Batman and Commissioner Gordon tried to bury it, causing the Batman to resurface and fight to protect Gotham City... the very city which brands him an enemy.",
            "rank": 63,
            "running_time_secs": 9900,
            "actors": [
                "Christian Bale",
                "Tom Hardy",
                "Anne Hathaway"
            ]
        }
    },
    {
        "year": 2012,
        "title": "The Place Beyond the Pines",
        "info": {
            "directors": ["Derek Cianfrance"],
            "release_date": "2012-09-07T00:00:00Z",
            "rating": 7.4,
            "genres": [
                "Crime",
                "Drama"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMjc1OTEwNjU4N15BMl5BanBnXkFtZTcwNzUzNDIwOQ@@._V1_SX400_.jpg",
            "plot": "A motorcycle stunt rider turns to robbing banks as a way to provide for his lover and their newborn child, a decision that puts him on a collision course with an ambitious rookie cop navigating a department ruled by a corrupt detective.",
            "rank": 64,
            "running_time_secs": 8400,
            "actors": [
                "Ryan Gosling",
                "Bradley Cooper",
                "Eva Mendes"
            ]
        }
    },
    {
        "year": 2014,
        "title": "Fast & Furious 7",
        "info": {
            "directors": ["James Wan"],
            "release_date": "2014-07-10T00:00:00Z",
            "genres": [
                "Action",
                "Crime",
                "Thriller"
            ],
            "plot": "After Dominic Toretto and his crew helped take down Owen Shaw, his brother Ian Shaw now wants revenge.",
            "rank": 65,
            "actors": [
                "Vin Diesel",
                "Paul Walker",
                "Dwayne Johnson"
            ]
        }
    },
     {
        "year": 2011,
        "title": "Bridesmaids",
        "info": {
            "directors": ["Paul Feig"],
            "release_date": "2011-04-28T00:00:00Z",
            "rating": 6.8,
            "genres": [
                "Comedy",
                "Romance"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMjAyOTMyMzUxNl5BMl5BanBnXkFtZTcwODI4MzE0NA@@._V1_SX400_.jpg",
            "plot": "Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef.",
            "rank": 68,
            "running_time_secs": 7500,
            "actors": [
                "Kristen Wiig",
                "Maya Rudolph",
                "Rose Byrne"
            ]
        }
    },
     {
        "year": 1994,
        "title": "The Shawshank Redemption",
        "info": {
            "directors": ["Frank Darabont"],
            "release_date": "1994-09-10T00:00:00Z",
            "rating": 9.3,
            "genres": [
                "Crime",
                "Drama"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX400_.jpg",
            "plot": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
            "rank": 80,
            "running_time_secs": 8520,
            "actors": [
                "Tim Robbins",
                "Morgan Freeman",
                "Bob Gunton"
            ]
        }
    },
    {
        "year": 2011,
        "title": "X-Men: First Class",
        "info": {
            "directors": ["Matthew Vaughn"],
            "release_date": "2011-05-25T00:00:00Z",
            "rating": 7.8,
            "genres": [
                "Action",
                "Adventure",
                "Sci-Fi"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTg5OTMxNzk4Nl5BMl5BanBnXkFtZTcwOTk1MjAwNQ@@._V1_SX400_.jpg",
            "plot": "In 1962, the United States government enlists the help of Mutants with superhuman abilities to stop a malicious dictator who is determined to start world war III.",
            "rank": 87,
            "running_time_secs": 7920,
            "actors": [
                "James McAvoy",
                "Michael Fassbender",
                "Jennifer Lawrence"
            ]
        }
    },
    {
        "year": 1993,
        "title": "Hocus Pocus",
        "info": {
            "directors": ["Kenny Ortega"],
            "release_date": "1993-07-16T00:00:00Z",
            "rating": 6.2,
            "genres": [
                "Comedy",
                "Family",
                "Fantasy",
                "Horror"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTI3MDI2NDc3Ml5BMl5BanBnXkFtZTcwNDQ2MzQyMQ@@._V1_SX400_.jpg",
            "plot": "After 300 years, three sister witches are resurrected in Salem Massachusetts on Halloween night, and it us up to two teenagers, a young girl, and an immortal cat to put an end to the witches reign of terror once and for all.",
            "rank": 88,
            "running_time_secs": 5760,
            "actors": [
                "Bette Midler",
                "Sarah Jessica Parker",
                "Kathy Najimy"
            ]
        }
    },
    {
        "year": 2010,
        "title": "The Last Song",
        "info": {
            "directors": ["Julie Anne Robinson"],
            "release_date": "2010-03-31T00:00:00Z",
            "rating": 5.2,
            "genres": [
                "Drama",
                "Romance"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMjA5NjM5MDA0M15BMl5BanBnXkFtZTcwMjg2NzQwMw@@._V1_SX400_.jpg",
            "plot": "A drama centered on a rebellious girl who is sent to a Southern beach town for the summer to stay with her father. Through their mutual love of music, the estranged duo learn to reconnect.",
            "rank": 551,
            "running_time_secs": 6420,
            "actors": [
                "Miley Cyrus",
                "Liam Hemsworth",
                "Greg Kinnear"
            ]
        }
    },
    {
        "year": 1986,
        "title": "Aliens",
        "info": {
            "directors": ["James Cameron"],
            "release_date": "1986-07-18T00:00:00Z",
            "rating": 8.5,
            "genres": [
                "Action",
                "Adventure",
                "Sci-Fi",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTYzNzU5MzQ4OV5BMl5BanBnXkFtZTcwMDcxNDg3OA@@._V1_SX400_.jpg",
            "plot": "The planet from [link=tt0078748] has been colonized, but contact is lost. This time, the rescue team has impressive firepower, but will it be enough?",
            "rank": 552,
            "running_time_secs": 8220,
            "actors": [
                "Sigourney Weaver",
                "Michael Biehn",
                "Carrie Henn"
            ]
        }
    },
    {
        "year": 2011,
        "title": "Source Code",
        "info": {
            "directors": ["Duncan Jones"],
            "release_date": "2011-03-11T00:00:00Z",
            "rating": 7.4,
            "genres": [
                "Mystery",
                "Sci-Fi",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTY0MTc3MzMzNV5BMl5BanBnXkFtZTcwNDE4MjE0NA@@._V1_SX400_.jpg",
            "plot": "An action thriller centered on a soldier who wakes up in the body of an unknown man and discovers he's part of a mission to find the bomber of a Chicago commuter train.",
            "rank": 553,
            "running_time_secs": 5580,
            "actors": [
                "Jake Gyllenhaal",
                "Michelle Monaghan",
                "Vera Farmiga"
            ]
        }
    },
    {
        "year": 2007,
        "title": "Stardust",
        "info": {
            "directors": ["Matthew Vaughn"],
            "release_date": "2007-08-09T00:00:00Z",
            "rating": 7.7,
            "genres": [
                "Adventure",
                "Family",
                "Fantasy",
                "Romance"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMjkyMTE1OTYwNF5BMl5BanBnXkFtZTcwMDIxODYzMw@@._V1_SX400_.jpg",
            "plot": "In a countryside town bordering on a magical land, a young man makes a promise to his beloved that he'll retrieve a fallen star by venturing into the magical realm.",
            "rank": 554,
            "running_time_secs": 7620,
            "actors": [
                "Charlie Cox",
                "Claire Danes",
                "Sienna Miller"
            ]
        }
    },
    {
        "year": 2003,
        "title": "Dumb and Dumberer: When Harry Met Lloyd",
        "info": {
            "directors": ["Troy Miller"],
            "release_date": "2003-06-13T00:00:00Z",
            "rating": 3.3,
            "genres": ["Comedy"],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTc4MzQ4NzE4M15BMl5BanBnXkFtZTYwMjg5NDk5._V1_SX400_.jpg",
            "plot": "Set back in the 80s when Harry met Lloyd in high school where they cross paths with a mean principal and a bunch of other outcasts much like themselves.",
            "rank": 555,
            "running_time_secs": 5100,
            "actors": [
                "Derek Richardson",
                "Eric Christian Olsen",
                "Eugene Levy"
            ]
        }
    },
    {
        "year": 2010,
        "title": "The Expendables",
        "info": {
            "directors": ["Sylvester Stallone"],
            "release_date": "2010-08-03T00:00:00Z",
            "rating": 6.4,
            "genres": [
                "Action",
                "Adventure",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BNTUwODQyNjM0NF5BMl5BanBnXkFtZTcwNDMwMTU1Mw@@._V1_SX400_.jpg",
            "plot": "A CIA operative hires a team of mercenaries to eliminate a Latin dictator and a renegade CIA agent.",
            "rank": 556,
            "running_time_secs": 6180,
            "actors": [
                "Sylvester Stallone",
                "Jason Statham",
                "Jet Li"
            ]
        }
    },
     {
        "year": 1997,
        "title": "Hercules",
        "info": {
            "directors": [
                "Ron Clements",
                "John Musker"
            ],
            "release_date": "1997-06-14T00:00:00Z",
            "rating": 7,
            "genres": [
                "Animation",
                "Adventure",
                "Family",
                "Fantasy",
                "Musical",
                "Romance"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTI5NTI3OTAyOV5BMl5BanBnXkFtZTcwMTg3ODkxMQ@@._V1_SX400_.jpg",
            "plot": "The son of the Greek Gods Zeus and Hera is stripped of his immortality as an infant and must become a true hero in order to reclaim it.",
            "rank": 558,
            "running_time_secs": 5580,
            "actors": [
                "Tate Donovan",
                "Susan Egan",
                "James Woods"
            ]
        }
    },
    {
        "year": 1990,
        "title": "Home Alone",
        "info": {
            "directors": ["Chris Columbus"],
            "release_date": "1990-11-10T00:00:00Z",
            "rating": 7.3,
            "genres": [
                "Comedy",
                "Family"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTUzMzg4MTg2M15BMl5BanBnXkFtZTYwNDM4OTk4._V1_SX400_.jpg",
            "plot": "An 8-year-old boy, who is accidentally left behind while his family flies to France for Christmas, has to defend his home against idiotic burglars.",
            "rank": 559,
            "running_time_secs": 6180,
            "actors": [
                "Macaulay Culkin",
                "Joe Pesci",
                "Daniel Stern"
            ]
        }
    },
    {
        "year": 1999,
        "title": "The Boondock Saints",
        "info": {
            "directors": ["Troy Duffy"],
            "release_date": "1999-08-04T00:00:00Z",
            "rating": 7.8,
            "genres": [
                "Action",
                "Crime",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTIzODA2NTUyM15BMl5BanBnXkFtZTYwODQ2Mjk4._V1_SX400_.jpg",
            "plot": "Fraternal twins set out to rid Boston of the evil men operating there while being tracked down by an FBI agent.",
            "rank": 564,
            "running_time_secs": 6480,
            "actors": [
                "Willem Dafoe",
                "Sean Patrick Flanery",
                "Norman Reedus"
            ]
        }
    },
    {
        "year": 2009,
        "title": "Up",
        "info": {
            "directors": [
                "Pete Docter",
                "Bob Peterson"
            ],
            "release_date": "2009-05-13T00:00:00Z",
            "rating": 8.3,
            "genres": [
                "Animation",
                "Adventure",
                "Comedy",
                "Drama",
                "Family",
                "Fantasy"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTMwODg0NDY1Nl5BMl5BanBnXkFtZTcwMjkwNTgyMg@@._V1_SX400_.jpg",
            "plot": "By tying thousands of balloons to his home, 78-year-old Carl sets out to fulfill his lifelong dream to see the wilds of South America. Russell, a wilderness explorer 70 years younger, inadvertently becomes a stowaway.",
            "rank": 565,
            "running_time_secs": 5760,
            "actors": [
                "Edward Asner",
                "Jordan Nagai",
                "John Ratzenberger"
            ]
        }
    },
    {
        "year": 2008,
        "title": "Quantum of Solace",
        "info": {
            "directors": ["Marc Forster"],
            "release_date": "2008-10-29T00:00:00Z",
            "rating": 6.7,
            "genres": [
                "Action",
                "Adventure",
                "Crime",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTY0MjI4MDI5MF5BMl5BanBnXkFtZTcwODkwNjk3MQ@@._V1_SX400_.jpg",
            "plot": "James Bond descends into mystery as he tries to stop a mysterious organization from eliminating a country's most valuable resource. All the while, he still tries to seek revenge over the death of his love.",
            "rank": 566,
            "running_time_secs": 6360,
            "actors": [
                "Daniel Craig",
                "Olga Kurylenko",
                "Mathieu Amalric"
            ]
        }
    },
    {
        "year": 2011,
        "title": "We Bought a Zoo",
        "info": {
            "directors": ["Cameron Crowe"],
            "release_date": "2011-11-26T00:00:00Z",
            "rating": 7.1,
            "genres": [
                "Drama",
                "Family"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQ0MTE3OTUwMl5BMl5BanBnXkFtZTcwODg5NjgwNw@@._V1_SX400_.jpg",
            "plot": "Set in Southern California, a father moves his young family to the countryside to renovate and re-open a struggling zoo.",
            "rank": 567,
            "running_time_secs": 7440,
            "actors": [
                "Matt Damon",
                "Scarlett Johansson",
                "Thomas Haden Church"
            ]
        }
    },
    {
        "year": 2010,
        "title": "The Fighter",
        "info": {
            "directors": ["David O. Russell"],
            "release_date": "2010-12-10T00:00:00Z",
            "rating": 7.9,
            "genres": [
                "Biography",
                "Drama",
                "Sport"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTM0ODk3MjM1MV5BMl5BanBnXkFtZTcwNzc1MDIwNA@@._V1_SX400_.jpg",
            "plot": "A look at the early years of boxer \"Irish\" Micky Ward and his brother who helped train him before going pro in the mid 1980s.",
            "rank": 571,
            "running_time_secs": 6960,
            "actors": [
                "Mark Wahlberg",
                "Christian Bale",
                "Amy Adams"
            ]
        }
    },
     {
        "year": 2009,
        "title": "Sherlock Holmes",
        "info": {
            "directors": ["Guy Ritchie"],
            "release_date": "2009-12-24T00:00:00Z",
            "rating": 7.5,
            "genres": [
                "Action",
                "Adventure",
                "Crime",
                "Mystery",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTg0NjEwNjUxM15BMl5BanBnXkFtZTcwMzk0MjQ5Mg@@._V1_SX400_.jpg",
            "plot": "Detective Sherlock Holmes and his stalwart partner Watson engage in a battle of wits and brawn with a nemesis whose plot is a threat to all of England.",
            "rank": 573,
            "running_time_secs": 7680,
            "actors": [
                "Robert Downey Jr.",
                "Jude Law",
                "Rachel McAdams"
            ]
        }
    },
    {
        "year": 2005,
        "title": "Charlie and the Chocolate Factory",
        "info": {
            "directors": ["Tim Burton"],
            "release_date": "2005-07-10T00:00:00Z",
            "rating": 6.7,
            "genres": [
                "Adventure",
                "Comedy",
                "Family",
                "Fantasy"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BNjcxMjg1Njg2NF5BMl5BanBnXkFtZTcwMjQ4NzMzMw@@._V1_SX400_.jpg",
            "plot": "A young boy wins a tour through the most magnificent chocolate factory in the world, led by the world's most unusual candy maker.",
            "rank": 578,
            "running_time_secs": 6900,
            "actors": [
                "Johnny Depp",
                "Freddie Highmore",
                "David Kelly"
            ]
        }
    },
    {
        "year": 2005,
        "title": "The Adventures of Sharkboy and Lavagirl 3-D",
        "info": {
            "directors": ["Robert Rodriguez"],
            "release_date": "2005-06-10T00:00:00Z",
            "rating": 3.4,
            "genres": [
                "Action",
                "Adventure",
                "Family",
                "Fantasy"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTM1NzI3OTAwMl5BMl5BanBnXkFtZTcwMTI3ODkyMQ@@._V1_SX400_.jpg",
            "plot": "A boy dreams up shark-boy and lava-girl and the horror that lies within their planet.",
            "rank": 579,
            "running_time_secs": 5580,
            "actors": [
                "Cayden Boyd",
                "George Lopez",
                "Kristin Davis"
            ]
        }
    },
    {
        "year": 2005,
        "title": "Serenity",
        "info": {
            "directors": ["Joss Whedon"],
            "release_date": "2005-08-22T00:00:00Z",
            "rating": 7.9,
            "genres": [
                "Action",
                "Adventure",
                "Sci-Fi",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTI0NTY1MzY4NV5BMl5BanBnXkFtZTcwNTczODAzMQ@@._V1_SX400_.jpg",
            "plot": "The crew of the ship Serenity tries to evade an assassin sent to recapture one of their number who is telepathic.",
            "rank": 581,
            "running_time_secs": 7140,
            "actors": [
                "Nathan Fillion",
                "Gina Torres",
                "Chiwetel Ejiofor"
            ]
        }
    },
    {
        "year": 1987,
        "title": "Full Metal Jacket",
        "info": {
            "directors": ["Stanley Kubrick"],
            "release_date": "1987-06-17T00:00:00Z",
            "rating": 8.4,
            "genres": [
                "Drama",
                "War"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BNDAzMjU3NzE0Nl5BMl5BanBnXkFtZTcwNTk1ODg3OA@@._V1_SX400_.jpg",
            "plot": "A pragmatic U.S. Marine observes the dehumanizing effects the Vietnam War has on his fellow Marine recruits from their brutal boot camp training to the bloody street fighting set in 1968 in Hue, Vietnam.",
            "rank": 582,
            "running_time_secs": 6960,
            "actors": [
                "Matthew Modine",
                "R. Lee Ermey",
                "Vincent D'Onofrio"
            ]
        }
    },
    {
        "year": 2002,
        "title": "Gangs of New York",
        "info": {
            "directors": ["Martin Scorsese"],
            "release_date": "2002-12-09T00:00:00Z",
            "rating": 7.5,
            "genres": [
                "Crime",
                "Drama",
                "History"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTI4NTM0Mzg2NV5BMl5BanBnXkFtZTcwNjQxMDAwMQ@@._V1_SX400_.jpg",
            "plot": "In 1863, Amsterdam Vallon returns to the Five Points area of New York City seeking revenge against Bill the Butcher, his father's killer.",
            "rank": 583,
            "running_time_secs": 10020,
            "actors": [
                "Leonardo DiCaprio",
                "Cameron Diaz",
                "Daniel Day-Lewis"
            ]
        }
    },
    {
        "year": 2004,
        "title": "Dawn of the Dead",
        "info": {
            "directors": ["Zack Snyder"],
            "release_date": "2004-03-10T00:00:00Z",
            "rating": 7.4,
            "genres": [
                "Action",
                "Horror",
                "Sci-Fi",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTI4OTU2NjY5OF5BMl5BanBnXkFtZTYwOTQ2Mzg3._V1_SX400_.jpg",
            "plot": "A nurse, a policeman, a young married couple, a salesman, and other survivors of a worldwide plague that is producing aggressive, flesh-eating zombies, take refuge in a mega Midwestern shopping mall.",
            "rank": 584,
            "running_time_secs": 6060,
            "actors": [
                "Sarah Polley",
                "Ving Rhames",
                "Mekhi Phifer"
            ]
        }
    },
    {
        "year": 2001,
        "title": "A Knight's Tale",
        "info": {
            "directors": ["Brian Helgeland"],
            "release_date": "2001-03-08T00:00:00Z",
            "rating": 6.7,
            "genres": [
                "Action",
                "Adventure",
                "Drama",
                "Romance"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTE5OTE4OTE2Nl5BMl5BanBnXkFtZTYwMDkzMTQ3._V1_SX400_.jpg",
            "plot": "After his master dies, a peasant squire, fueled by his desire for food and glory, creates a new identity for himself as a knight.",
            "rank": 585,
            "running_time_secs": 7920,
            "actors": [
                "Heath Ledger",
                "Mark Addy",
                "Rufus Sewell"
            ]
        }
    },
    {
        "year": 1979,
        "title": "The Warriors",
        "info": {
            "directors": ["Walter Hill"],
            "release_date": "1979-02-01T00:00:00Z",
            "rating": 7.6,
            "genres": [
                "Action",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTYzMjE2MzE3MF5BMl5BanBnXkFtZTYwMzUyNDQ5._V1_SX400_.jpg",
            "plot": "In 1979 a charismatic leader summons the street gangs of New York City in a bid to take it over. When he is killed, The Warriors are falsely blamed and now must fight their way home while every other gang is hunting them down to kill them.",
            "rank": 586,
            "running_time_secs": 5520,
            "actors": [
                "Michael Beck",
                "James Remar",
                "Dorsey Wright"
            ]
        }
    }
]
'''