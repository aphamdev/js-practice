// Implement the function shorterThan5(strings), which returns an
// array that contains all of the strings from the strings input that have a length less than 5.

const shorterThan5 = function (strings) {
  const results = [];
  for (let string of strings) {
    if (string.length < 5) {
      results.push(string);
    }
  }

  // your code here

  return results;
};
