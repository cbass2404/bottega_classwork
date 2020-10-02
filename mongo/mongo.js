// swaps to that database
use mongoCourse

// gets a list of all users
db.getUsers()

// drops the specified user
db.dropUser('jon')

// creates a collection in the database
db.createCollection('books')

//shows you the collections
show collections

// does magical mystifying stuff
system.indexes

// syntax to create a user
db.createUser({
    user: 'jon',
    pwd: 'I@maMari|\|e19',
    customData: { startDate: new Date() },
    roles: [
        { role: 'clusterAdmin', db: 'admin' },
        { role: 'readAnyDatabase', db: 'admin' },
        'readWrite'
    ]
})

// inserts an object into a collection
db.books.insert({
    "name": "OOP Programming",
    "publishedDate": new Date(),
    "authors": [
        { "name": "Jon Snow" },
        { "name": "Ned Stark" }
    ]
})

// insert many objects into a collection
db.books.insertMany([
    {
        "name": "Confident Ruby",
        "publishedDate": new Date(),
        "authors": [
            {"name": "Avdi Grimm"}
        ]
    },
    {
        "name": "The War of Art",
        "publishedDate": new Date(),
        "authors": [
            {"name": "Steven Pressfield"}
        ]
    },
    {
        "name": "Blink",
        "publishedDate": new Date(),
        "authors": [
            {"name": "Malcolm Gladwell"}
        ]
    }
])

// query all objects in a mongodb, do find().pretty() to make the return easier to read in the terminal
db.books.find()
or
db.books.find().pretty()

// query for a specific object in mongodb, .pretty() is optional for terminal readability

db.books.find({ name: "The war of Art"}).pretty()

// mongodb projections are the second argument in the find() function
db.books.find(
    {
        name: "Confident Ruby",
    },
    {
        _id: 0,
        name: 1,
        authors: 1
    }
).pretty()

// querying for a portion of a string in mongodb / means you are entering into regular expressions .* means look for anything in begining middle or end i means not case sensitive
db.books.findOne({name: /.*deep work.*/i})

// deleting documents in mongodb
db.books.remove({name: "OOP Programming"}) // removes all the items with that name
db.books.remove({name: "OOP Programming", 1 }) //removes one of them

// querying nested fields in find query *string together search with .embeddedName.embeddedName etc....
db.books.insert({
    "name": "Blink",
    "publishedDate": new Date(),
    "authors": [
        { "name": "Malcolm Gladwell", "active": "true" },
        { "name": "Ghost Writer", "active": "true" }
    ]
});

db.books.find(
    {
        name: "Blink"
    },
    {
        name: 1,
        publishedDate: 1,
        "authors.name": 1
    }
).pretty()

// use findOne() method to query for a single document
db.books.find({name: "Blink"}) // returns all documents with the name blink
db.books.find({name: "Blink"}).length() // returns how many documents have the called value
db.books.findOne({name: "Blink"}) // returns only the one object with that name

// check db to see if a field exists
db.books.find({ reviews: { $exists: false}})