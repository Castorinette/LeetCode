-- Challenge 1757 : Recyclable and Low Fat Products

select product_id 
from Products
where low_fats='Y' AND recyclable='Y'

-- Challenge 584 : Find Custom Referee


select name
from Customer 
where  referee_id is null or referee_id <> 2 

-- Challenge 595 : Big Country

select name,population,area
from World
where area >= 3000000 or population >= 25000000

-- Challenge 1683 : Invalid Tweets

select tweet_id
from Tweets
where length(content) > 15

-- Challenge 1378 : Replace Employee ID with the Unique Identifier
