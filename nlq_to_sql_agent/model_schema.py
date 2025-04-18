schema_description = """
Database: mio

Tables:
1. Category ( categoryId int(10) , name varchar(32) , created datetime , modified timestamp)
2. Customer ( customerId bigint(19), name varchar(32) , country varchar(3), created datetime , modified timestamp )
3. Item ( itemId bigint(19), name varchar(32) , categoryId int(10), price double(8,2) ,created datetime , modified timestamp )
4. ReplenishmentEvent ( transactionId bigint(19) ,itemId bigint(19), quantity int(10), created datetime, modified timestamp )
5. SaleEvent ( transactionId bigint(19), itemId bigint(19), quantity int(10), customerId bigint(19), created datetime, modified timestamp )
6. ReturnEvent ( transactionId bigint(19),itemId bigint(19), quantity int(10), customerId bigint(19), created datetime, modified timestamp )

Relationships:
1. Category.categoryId = Item.categoryId
2. Customer.customerId = SaleEvent.customerId
3. Item.itemId = ReplenishmentEvent.itemId
4. Item.itemId = SaleEvent.itemId
5. Item.itemId = ReturnEvent.itemId
6. Customer.customerId =SaleEvent.customerId
7. Customer.customerId =SaleEvent.ReturnEvent

"""