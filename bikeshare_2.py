import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA =['all','january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA =['all', 'sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday']
RESTART =['yes', 'no']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('Which city do you want to show chicago, new york or washington? \n> ').lower()
       if city in CITY_DATA:
           break
       else :
           print("please selecte one of the mentioned city\'s")

    # get user input for month (all, january, february, ... , june)
    while True:
             month =input(" please select the Month January, February, March, April, May, June , or All: \n").lower()
             if month in MONTH_DATA :
                 break
             else:
                 print("please select one of the mentioned month\'s")
                 
                
      
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("please select the week Day  Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday , or All : \n").lower()
        if day in DAY_DATA:
            break
        else :
            print("please select one of the mentioned day's")
        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df_file =pd.read_csv(CITY_DATA[city])
    df = pd.DataFrame(df_file).fillna(0)
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    
    
    df['month'] =df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    
    
    
    if month != 'all' :
        month = MONTH_DATA.index(month)+1
        df = df.loc[df['month']== month]
        
    if day != 'all' :
        day = DAY_DATA.index(day)
        df = df.loc[df['day'] == day]    
  

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    print("the most common Month is \n "  , df['month'].value_counts())

    # display the most common day of week
    print("the most common Day is \n", df['day'].value_counts())

    # display the most common start hour
    print("the most common Hour is \n ", df['hour'].value_counts())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("the most common Start Station is \n",df['Start Station'].value_counts())

    # display most commonly used end station
    print("the most common end Station is \n ", df['End Station'].value_counts())

    # display most frequent combination of start station and end station trip
    print('the most frequent combination of start station and end station trip is :\n ', df['Start Station'].value_counts(), df['End Station'].value_counts())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Trip Duration by mintets is : \n", df['Trip Duration'].sum()/60)

    # display mean travel time
    print("Average Trip Duration by mintets  is : \n",df['Trip Duration'].mean()/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count of User Type is : \n", df['User Type'].value_counts())

    # Display counts of gender
    print("Count of User Gendar is : \n", df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print("the earliest user year of birth is : \n", df['Birth Year'].min())
    
    print("the most resent user year of birth is : \n", df['Birth Year'].max())
    
    print("the most common  user year of birth is : \n", df['Birth Year'].value_counts())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """Displays raw data on user request.
    """
    print(df.head())
    next = 0
    
    while True:    
        view_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n').lower()
        if view_data not in RESTART : # use the same list for restart as it's the same needed answer 
            print('please enter yes or no \n ')
        elif view_data == 'no' :
            return
        elif view_data == 'yes':
            next = next + 5
            print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart not in RESTART :
            print('plese enter yes or no \n ')  
        elif restart != 'yes' :
            break


if __name__ == "__main__":
	main()
