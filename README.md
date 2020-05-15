# Track-Restaurant-flask

## Data Structure

### User
name | defination
| ----------- | ----------- |
username | string
email | string
password | string
city | city id from zomato API
id | key
1. /register POST, register account
2. /update PATCH, update acount
3. /login POST, login
4. /logout GET, logout
5. /search GET, search user by username
6. /send/id POST, send request to user with id
7. /requests GET, get request to current user


### Like_Restaurant
name | defination
| ----------- | ----------- |
restaurant_id | restaurant id from zomato api
address | address from zomato api
city | city id from zomato api
cuisine | list of cuisines
picture | picture from zomato api
user_id | key to user
name | name of restaurant
url | zomato url link
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
