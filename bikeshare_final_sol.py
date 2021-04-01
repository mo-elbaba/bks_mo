import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
  
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please Select a city (chicago, new york city, washington): ').lower()
        
    while city not in CITY_DATA.keys():
        print('Invalid city name')
        city = input('Please Select a city (chicago, new york city, washington): ').lower()
                    
    months = ['all','january','february', 'march', 'april', 'may', 'june']
    month = input('Please Select a month whether all or from january to june:\n').lower()
    while month not in months:
        print('invalid month')
        month = input('Please Select a month whether all or from january to june:\n').lower()
        
    days = ['Sunday','Monday','Tuesday','Wednsday','Thursday','Friday','Saturday','All']
    day = input('Please select a day of a week: ').title()
    while day not in days:
        print('Sorry, you have entered an invalid day')
        day = input('Please select a day of a week: ').title()
    
    print('-'*40)
    return city, month, day
    
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is {}.'.format(common_month))
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('the common day of week is {}.'.format(common_day))
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common Start Hour is {}.'.format(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station = df['Start Station'].mode()[0]
    station_dep_count = df['Start Station'].nunique()
    print('Number of unique Start Stations in use: {}'.format(station_dep_count))
    print('The most common start station is {}.'.format(common_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    station_end_count = df['End Station'].nunique()
    print('Number of unique End Stations in use: {}'.format(station_end_count))
    print('The most common end station is {}.'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_union = df['Combination'].mode()[0]
    print('The most frequent combination of two stations is {}.'.format(common_union))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    trips_count = df['Trip Duration'].count()
    print('Total Number of Trips among the selected month and day is {}'.format(trips_count))
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time is {}.'.format(total_time))
    
    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print('The Average of travel time is {}.'.format(travel_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('The users type count is:\n{}'.format(user_count))
    while True:
        try:     
    # TO DO: Display counts of gender
            gender_counts = df['Gender'].value_counts()
            print('Counts of genders is:\n{}.'.format(gender_counts))
            
        except KeyError:
            print('Gender information is not available for the selected city')
        try:
    # TO DO: Display earliest, most recent, and most common year of birth
            common_birth = df['Birth Year'].mode()[0]
            recent_birth = df['Birth Year'].max()
            print('The most recent year of birth is {}, and the most common is {}.'.format(recent_birth, common_birth))
            break
        except KeyError:
            print('Birth Year information is not available for the selected city')
        break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_more(df):
    raw = 0
    see_more = input('Would you like to see raw data? Enter yes or no.\n')
    while see_more.lower() == 'yes':
        print(df[raw:raw + 5])
        see_more = input('Would you like to see more data? Enter yes or no.\n')
        raw += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_more(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()