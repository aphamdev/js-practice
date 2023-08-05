// same as dictList python

function propertyInObject(values, propertyName) {
  return values.map(function (value) {
    return propertyName in value;
  });
}
