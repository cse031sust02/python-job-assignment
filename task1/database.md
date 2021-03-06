## Database Design

We will use PostgreSQL as our database server. We will also use the PostGIS extension to query the nearest restaurants od a customer.

#### users :
```
id, email, phone, password, user_type(customer/manager), last_login, created_at, updated_at
```
> note : this table will be used for authentication

#### customers :
```
id, user_id, address, created_at, updated_at
```
> note : customer profile

#### managers :
```
id, user_id, address, created_at, updated_at
```
> note : restaurant manager profile

#### delivery_boys :
```
id, user_id, address, created_at, updated_at
```
> note : delivery boy profile

#### restaurants :
```
id, name, desc, image, address, lat, lon, created_at, updated_at
```

#### restaurant_mangers :
```
id, user_id, restaurant_id, created_at, updated_at
```
> note : I am assuming that one restaurant will have multiple managers.

#### restaurant_delivery_boys :
```
id, user_id, restaurant_id, created_at, updated_at
```

#### commission :
```
id, restaurant_id, commission_rate_percent
```

### discounts :
```
id, discount_code, discount_type(percent/flat), amount
```

#### food_categories :
```
id, title
```

#### items :
```
id, restaurant_id, food_category_id, title, description, image, created_at, updated_at
```

#### orders :
```
id, customer_id, restaurant_id, total_price, discount_id, discount_amount, final_price, current_status(ordered/ready/delivered/rejected), delivery_boy_id, delivery_address, created_at, updated_at
```
> note : final_price = total_price - discount_amount

#### order_status_log :
```
id, order_id, status, datetime
```

#### order_items :
```
id, order_id, item_id, quantity, unit_price, total_price
```

**Note that, this is just a minimal database design to start. It will evolve after discussion/new requriements.**
