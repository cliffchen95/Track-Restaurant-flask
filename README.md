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
1. /register POST, register account
2. /update PATCH, update acount
3. /login POST, login
4. /logout GET, logout

### Like_Restaurant
name | defination
| ----------- | ----------- |
restaurant_id | restaurant id from zomato api
address | address from zomato api
picture | picture from zomato api
user_id | key to user
1. / GET, get info of liked restaurants of the current user
2. / POST, create a like_restaurant for current user with restaurant info
3. / DELETE, remove liked restaurant of the current user

### Dislike_Restaurant
name | defination
| ----------- | ----------- |
restaurant_id | restaurant id from zomato api
user_id | key to user
1. / GET, get info of liked restaurants of the current user
2. / POST, create a like_restaurant for current user with restaurant info

### Friend
name | defination
| ----------- | ----------- |
user_id1 | key to user
user_id2 | key to user
1. / POST, create a relationship between current user and user2
2. / DELETE, remove a relationship
