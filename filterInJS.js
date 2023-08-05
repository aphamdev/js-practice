// Please complete the following function that takes an array of values, a lower threshold value, and an upper threshold
// value. The function must return a new array that contains
// entries from the original array that are greater than or equal to the lower
// threshold value and less than or equal to the upper threshold value.

function filterBetween(values, lower, upper) {
  return values.filter(function (v) {
    return v >= lower && v <= upper;
  });
}
