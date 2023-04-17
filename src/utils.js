const utils = {
  increment_index_in_range: (index, min, max) => {
    if (min === max || index >= max) return min;
    return ++index;
  },
  decrement_index_in_range: (index, min, max) => {
    if (min === max) return min;
    if (index <= min) return max;
    return --index;
  },
};

module.exports = utils;
