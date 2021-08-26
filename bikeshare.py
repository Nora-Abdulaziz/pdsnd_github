import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('\nWhich city do you want data for? chicago, new york city or washington?\n').lower()
    while True:

        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print('Wrong input please choose again')
            city=input('\nWhich city do you want data for? chicago, new york city or washington?\n').lower()
            


        # TO DO: get user input for month (all, january, february, ... , june)
    month=input('\nWhich month you want data for? january, february, march, april, may, june or all?\n').lower()
    while True:

        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print('Wrong input please choose again')
            month=input('\nWhich month you want data for? january, february, march, april, may, june or all?\n').lower()
            

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('\nwhich day? monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n').lower()
    while True:

        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break
        else:
            print('Wrong input please choose again')
            day=input('\nwhich day? monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n').lower()
            
       

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
                                  

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month is:', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('Most common day of week is:', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('Most common start hour is:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station is:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station is:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df['Start Station'] + ' to ' + df['End Station']
    print('Most frequent combination of start station and end station trip is:', most_frequent_combination.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is:', df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('Mean travel time is:', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types is:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city =='chicago' or city =='new york city':
        print('Counts of gender is:')
        print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if city =='chicago' or city =='new york city':
        print('Earliest year of birth is:', df['Birth Year'].min())
        print('Most recent year of birth is:', df['Birth Year'].max())
        print('Most common year of birth is:', df['Birth Year'].mode()[0])


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def raw_data_input(df):
      
    raw_data=input('Would you like to see raw data? Enter yes or no?').lower()
    row = 0
    while True:        
        if raw_data=='no':
            break
        elif raw_data=='yes':
            print(df.iloc[row: row + 5])
            row += 5
            more_data=input('Would you like to see next 5 rows?').lower()
            if more_data=='no':
                break

               
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data_input(df)

        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
