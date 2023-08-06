// Please complete the following function. Given a list of sorted
// values, return true if the searchTerm exists in the list. Otherwise, return false.

function simpleSearch(values, searchTerm) {
  for (let v of values) {
    if (v === searchTerm) {
      return true;
    }
  }
  return false;
}
