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
    while True:
        city = input ('please enter the city name from {}\n'.format(list(CITY_DATA.keys()))).lower()
        if city not in CITY_DATA :
            print('please enter a correct city name\n')
        else:
             break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        months =['january','february','march','april','may','june']
        month =input("please choose a month from {}, or type 'all' to all months: \n".format(months)).lower()
        if month != 'all' and month not in months :
                print('please enter a correct month name \n')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        days =['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        day =input('please enter a day from {}, or type "all" to all days : \n'.format(days)).lower()
        if day != 'all' and day not in days :
            print ('please choose a valid day name ')
        else:
            break
  

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
    column_names = ['id', 'start_time', 'end_time',
                  'trip_duration', 'start_station',
                  'end_station', 'user_type', 
                  'gender','birth_year']
    
    df = pd.read_csv(CITY_DATA[city])

    if city == 'washington':
        df.columns = column_names[:-2]
    else:
        df.columns = column_names
    
    
    df['start_time']=pd.to_datetime(df['start_time'])
    df['month']=df['start_time'].dt.month_name().str.lower()
    df['day_of_week']=df['start_time'].dt.day_name().str.lower()
    if month != 'all':
        df=df[df['month'] == month]
    if day != 'all':
        df=df[df['day_of_week'] == day]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is : %s" % df.month.mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week is : %s" % df.day_of_week.mode()[0])


    # TO DO: display the most common start hour
    print("The most common start hour is : %s" % df['start_time'].dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start=df['start_station'].mode()[0]
    print('the most common start station used: ',common_start)


    # TO DO: display most commonly used end station
    common_end=df['end_station'].mode()[0]
    print('the most common end station used: ',common_end)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_end=(df['start_station'] + ' - '+ df['end_station']).mode()[0]
    print(' the most frequent combination of start station and end station trip : ',common_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['trip_duration'].sum()
    print('total travel time is: ',total_time,'second')


    # TO DO: display mean travel time
    avg_time=df['trip_duration'].mean()
    print('the mean travel time is: ',avg_time,'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['user_type'].value_counts()
    print(' counts of user types: ',user_types)


    # TO DO: Display counts of gender
    if 'gender' in df :
        print('counts of gender',df['gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'birth_year' in df:
        earliest_birth_year = int(df['birth_year'].min())
        print('earlist birth year:',earliest_birth_year)
        most_recent_birth_year = int(df['birth_year'].max())
        print('recent birth year:',most_recent_birth_year)
        most_common_birth_year=int(df['birth_year'].mode()[0])
        print('common birth year:',most_common_birth_year)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data_rows(df):
    
    i =0
    input_user =input('would you like to display 5 rows of raw data? [yes\\no]: \n').lower()
    while input_user =='yes' :
        print(df[i:i+5])
        input_user =  input('would you like to display more 5 rows? [yes\\no]: \n').lower()
        i += 5  

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data_rows(df)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
