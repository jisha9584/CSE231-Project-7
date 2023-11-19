###########################################################
#  Computer Project #7
#
#  Print MENU 
#    define functions
#       1. open file
#       2. read users
#       3. read reviews
#       4. read movies
#       5. year movies
#       6. genre movies
#       7. gen users 
#       8. occ users 
#       9. highest rated by movie
#       10. highest rated by reviewer 
#    define main
#       read the files
#       create the main 3 lists of lists by calling (read_users, read_reviews, and read_movies)
#       Display the menu (MENU) and prompt to choose from the 5 options
#       prompt for an option input until 5 is entered:
#           1. Year based
#           2. Genre based 
#           3. Gender based
#           4. Occubaption based
#           5. Quits the program
###########################################################

GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker',\
                   'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', \
                   'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, \
                                              list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''
def open_file(s):
    '''
    Open the promted file.
    s: string to incorporate into prompt.
    Return: file_pointer.
    '''
    file_pointer = input(("\nInput {} filename: ").format(s))
    while True:
        try:
            file_pointer = open(file_pointer, "r", encoding ="windows-1252")
            return file_pointer
        except FileNotFoundError:
            print("\nError: No such file; please try again.")
            file_pointer = input("\nInput {} filename: ".format(s))

def read_reviews(N,fp):
    ''' 
    Reads the reviews.txt file using the file pointer.
    N: is an int, is the number of users, allows us to initialize a list of\
        N+1 empty lists.
    fp: file pointer.
    Returns: list of sorted lists of tuples of ints.
    '''

    L_reviews = []

    for line in range(N+1):
       L_reviews.append([])

    for line in fp:
        line = line.split()
        userID = int(line[0])
        movieID = int(line[1])
        rating = int(line[2])
        my_tuple = (movieID, rating)
        L_reviews[userID].append(my_tuple)
    
    for line in L_reviews:
        line.sort()
    return L_reviews

def read_users(fp):
    ''' 
    Reads the user.txt file using file pointer.
    fp: file pointer.
    Returns: list of tuples.
    '''
    master_list = [[]]
    for line in fp:
        line = line.split("|")
        reviwer_id = int(line[0]) 
        age = int(line[1])
        gender = line[2]
        occupation = line[3]
        my_tuple = (age, gender, occupation)
        master_list.append(my_tuple)
    return master_list

def read_movies(fp):
    ''' 
    Reads the movies.txt file using file pointer.
    fp: file pointer.
    Returns: list of lists.
    '''
    master_list = [[]]
    for line in fp:
        line = line.strip()
        line = line.split("|")
        movieID_movie = line[0]
        title_movie = line[1]
        date_movie = line[2]
        url_movie = line[4]
        genre_movie = line[5:]  
        
        movie_new_list = []
        for i, var in enumerate(genre_movie):
            if var == "1":
                movie_new_list.append(GENRES[i])
        my_tuple = (title_movie, date_movie, movie_new_list)
        master_list.append(my_tuple)
    return master_list

def year_movies(year,L_movies):
    ''' 
    Filters the main movie list to find movies for a specific year to find \
        movies for a specific year and returns their ids movieID.
    year: the prompted value entered by the user.
    L_movies: list of movies.
    Returns: sorted list of ints.
    '''
    master_list = []
    for i, line in enumerate(L_movies[1:], 1):
        try:
            date_movie = line[1]        
            date_movie = date_movie.split("-")
            year_movie = int(date_movie[2])
            if year_movie == year:
                master_list.append(i)
        except:
            None 
    return master_list

def genre_movies(genre,L_movies):
    ''' 
    Filters the main movie list to find movies for a specific genre.
    genre: the prompted genre entered by the user.
    L_movies: list of movies.
    Return: sorted list of ints.
    '''
    master_list = []
    for i, line in enumerate(L_movies[1:], 1):
            genre_movie = line[2]        
            if genre in genre_movie:
                master_list.append(i)
    master_list.sort()
    return master_list

def gen_users (gender, L_users, L_reviews):
    ''' 
    Filters the main reviews list to find reviews for a specific gender of\
        users.
    gender: the prompted gender entered by the user.
    L_users: list of users.
    L_reviews: list of reviews.
    Return: list of list of tuples.
    '''
    master_list = []
    for i, line in enumerate(L_users[1:], 1):
        gender_user = line[1]
        if gender_user == gender:
            master_list.append(L_reviews[i])
    return master_list
          
def occ_users (occupation, L_users, L_reviews):
    ''' 
    Filters the main reviews list to find records for a specific occupational\
        group of users.
    occupation: the prompted occupation entered by the user.
    L_users: list of users.
    L_reviews: list of reviews.
    Return: list of list of tuples.
    '''
    master_list = []
    for i, line in enumerate(L_users[1:], 1):
        occupation_user = line[2]
        if occupation_user == occupation:
            master_list.append(L_reviews[i])
    return master_list

def highest_rated_by_movie(L_in,L_reviews,N_movies): #took help from a TA (group) in helproom on 10/28 
    ''' 
    Calculates the average rating for the reviews in L_reviews list of the \
        movies in L_in list.
    L_in: list of ints.
    L_reviews: list of lists of tuples.
    N_movies: int.
    Return: list of floats, float.
    '''
    list_of_averages = [0]*len(L_in)
    list_of_totals = [0]*len(L_in)
    list_of_number = [0]*len(L_in)

    for line in range(len(L_in)):
        for i in L_reviews:
            if i != []:
                for ch in i:
                    if ch[0] == L_in[line]:
                        list_of_number[line] += 1
                        list_of_totals[line] += ch[1]
    for line in range(len(L_in)):
        list_of_averages[line] = round(list_of_totals[line] / list_of_number\
                                       [line],2)
       
    max_list = []
    max_num = -1
    for i in range(len(L_in)):
        if list_of_averages[i] > max_num:
            max_num = list_of_averages[i]
            max_list = []
            max_list.append(L_in[i])
        elif list_of_averages[i] == max_num:
            max_list.append(L_in[i])
    return max_list, max_num
             
def highest_rated_by_reviewer(L_in,N_movies): #took help from a TA (group) in helproom on 10/28 
    ''' 
    Calculates the average rating for movies by a specific group of users \
        (L_in).
    L_in: list of list of tuples.
    N_movies: int.
    Return: list of floats, float.
    '''
    list_of_averages = []
    for line in range(N_movies+1):
        master_list = [0,0]
        list_of_averages.append(master_list)
    for line in L_in:
        for var in line:
            movieID = var[0]
            rating = var[1]
            list_of_averages[movieID][1] += 1
            list_of_averages[movieID][0] += rating
        
    average_list = []
    for line in list_of_averages:
        amount_of_numbers = line[1] 
        total = line[0]
        try:
            average = total/amount_of_numbers
            average_list.append(average)
        except ZeroDivisionError:
            average = 0
            average_list.append(average)
            
    max_average = -1
    for num in average_list:
        if num > max_average:
            max_average = num

    movie_average = []
    for line in range (len(average_list)):
        if average_list[line] == max_average:
            movie_average.append(line)
    return(movie_average, max_average)

def main():
    #read the files (call the open_file function 3 times to open 3 different files.
    userPT = open_file("users")
    reviewsPT = open_file("reviews")
    moviesPT = open_file("movies")
    
    #create the main 3 lists of lists by calling (read_users, read_reviews, and read_movies).
    users = read_users(userPT)
    N = len(users)-1
    reviews = read_reviews(N, reviewsPT)
    movies = read_movies(moviesPT)

    N_movies = len(movies)-1

    print(MENU)
    option = int(input("\nSelect an option (1-5): "))

    while option != 5:
        if option == 1:
            prompt = input("\nInput a year: ")
            while True: 
                if prompt.isdigit() and (1930 < int(prompt) < 1998): 
                    prompt = int(prompt)
                    break
                else: #re-prompt if the year is less than 1930 or greater than 1998 
                    print("\nError in year.")
                    prompt = input('\nInput a year: ')

            #Then display the maximum average followed by the movies names that have that average. 
            L_in = year_movies(prompt, movies)
            movies_with_average, max_avg = highest_rated_by_movie(L_in, \
                                                                  reviews, \
                                                                      N_movies)
            print("\nAvg max rating for the year is:" , max_avg)
            for IDs in movies_with_average:
                print(movies[IDs][0])
   
        elif option == 2:
            print("\nValid Genres are: ", GENRES) #Display all valid genres.
            prompt = input("Input a genre: ")
            prompt = prompt.lower().capitalize()
            while True: 
                if prompt in GENRES:
                    break
                else: # re-prompt if the genre is not a valid genre
                    print("\nError in genre.")
                    prompt = input("Input a genre: ").lower().capitalize()
            #Call genre_movies and then call highest_rated_by_movie. Then display the maximum average followed by the movies names that have that average        
            L_in = genre_movies(prompt, movies)
            movies_with_average, max_avg = highest_rated_by_movie(L_in, \
                                                                  reviews, \
                                                                      N_movies)
            print("\nAvg max rating for the Genre is:" , max_avg)
            for IDs in movies_with_average:
                print(movies[IDs][0])
            
        elif option == 3:
            prompt = input("\nInput a gender (M,F): ")
            prompt = prompt.upper()
            while True: 
                if prompt == "M" or prompt == "F":
                    break 
                else: #re-prompt if the gender is not valid
                    print("\nError in gender.")
                    prompt = (input("\nInput a gender (M,F): ")).upper()
            #Call gen_users (note that the gender in the file is upper case) and then call highest_rated_by_reviewer . Then display the maximum average followed by the movies names that have that average (print one movie in a separate line).
            L_in = gen_users (prompt, users, reviews)
            reviewer_with_average, max_avg = highest_rated_by_reviewer(L_in, \
                                                                      N_movies)
            print("\nAvg max rating for the Gender is:" , max_avg)
            
            for IDs in reviewer_with_average:
                print(movies[IDs][0])
            
        elif option == 4: 
            print("\nValid Occupatipns are: ", OCCUPATIONS) #Display all valid occupations.
            prompt = input("Input an occupation: ").lower()
            while True: 
                if prompt in OCCUPATIONS:
                    break       
                else: #re-prompt if the occupation is not valid.
                    print("\nError in occupation.")
                    prompt = input("Input an occupation: ").lower()
            #Call occ_users and then call highest_rated_by_reviewer. Then display the maximum average followed by the movie names that have that average.
            L_in = occ_users(prompt, users, reviews)
            reviewer_with_average, max_avg = highest_rated_by_reviewer(L_in,\
                                                                      N_movies)
            print("\nAvg max rating for the occupation is:" , max_avg)
            for IDs in reviewer_with_average:
                print(movies[IDs][0])
            
        elif option == 5: #If option is 5 --> quit the program
            break

        else:
            print("\nError: not a valid option.")

        option = int(input("\nSelect an option (1-5): "))       


if __name__ == "__main__":
    main()
    pass                                       
