// # Please complete the following function that accepts two parameters: a JSON-formatted string representing a
// # dictionary, and a value. The function should return the key for a matching value
// #  if it exists in the dictionary represented by the JSON, and None otherwise.

// # JSON-formatted string	Property value	Output
// # {}                  	"Noor"	        None
// # '{"age": 23}'       	"Noor"	        None
// # '{"name": "Noor"}'    'Noor"      	"name"

function keyForValue(jsonString, propertyValue) {
  const d = JSON.parse(jsonString);
  for (let key in d) {
    if (d[key] === propertyValue) {
      return key;
    }
  }
  return null;
}
