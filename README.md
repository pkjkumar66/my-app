# my-app

### home-page
curl --location 'http://127.0.0.1:5000/'

### add-items
curl --location 'http://127.0.0.1:5000//add_item' \
--header 'Content-Type: application/json' \
--data '{
    "username" : "Pankaj",
    "item" : "take devops session"
}'


### view-item
curl --location 'http://127.0.0.1:5000/view_items/Pankaj'

### delete-items
curl --location --request DELETE 'http://127.0.0.1:5000/delete_item/Pankaj/3'