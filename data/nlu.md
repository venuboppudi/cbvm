## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thank you

## intent:deny
- no thanks
- not required
- no thnakyou
- nope
- no

## intent:mail_id
- [njsahdjkjsd@ghyo.guk](email)
- my mail id is [dsadjkdfjk@hhdshd.wewd](email)
- please email to [dnsdjh@627hi.twd](email)
- yes , mail me to [sdad3e214@jhdjy5.yte](email)
- mail - [hdgajdmn3@hdueyr.dge](email)
- [meenakshi.behera@gmail.com](email)

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:budget_range
- between [300 to 700]{"entity": "budget", "value": "mid"}
- above [300]{"entity": "budget", "value": "mid"}
- less than [300]{"entity": "budget", "value": "low"}
- less than [700]{"entity": "budget", "value": "mid"}
- more than [300]{"entity": "budget", "value": "mid"}
- more than [700]{"entity": "budget", "value": "high"}
- above [700]{"entity": "budget", "value": "high"}
- under [700]{"entity": "budget", "value": "mid"}
- under [300]{"entity": "budget", "value": "low"}
- under [1000]{"entity": "budget", "value": "high"}
- Rs. 301 - [700]{"entity": "budget", "value": "mid"}

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- find restaurent
- [mumbai](location)
- [Chinese]{"entity": "cuisine", "value": "chinese"}

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:high
- 1000

## synonym:low
- 300

## synonym:mid
- 300 to 700
- 700

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
