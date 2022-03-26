Django Rest Api application Overview
We will build a Django Rest Apis Application that can create, retrieve, update, delete and find BookInventorys by title or published status.

The following table shows overview of the Rest APIs that will be exported:

Methods			Urls					Actions

GET			api/bookInventorys		get all BookInventorys
GET			api/bookInventorys/:id		get BookInventory by id
POST			api/bookInventorys		add new BookInventory
PUT			api/bookInventorys/:id		update BookInventory by id
DELETE		api/bookInventorys/:id		remove BookInventory by id
DELETE		api/bookInventorys		remove all BookInventorys
GET		api/bookInventorys/published		find all published BookInventorys
GET		api/bookInventorys?title=[kw]	find all BookInventorys which title contains 'kw'






