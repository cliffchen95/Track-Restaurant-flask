# Track-Restaurant-flask

## Data Structure

### User
name | defination
| ----------- | ----------- |
username | string
email | string
password | string
address/location of interest | string, this will dictate the area to search restaurant
id | key

### Like_Restaurant
name | defination
| ----------- | ----------- |
restaurant_id | restaurant id from zomato api
address | address from zomato api
picture | picture from zomato api
user_id | key to user

### Dislike_Restaurant
name | defination
| ----------- | ----------- |
restaurant_id | restaurant id from zomato api
user_id | key to user

