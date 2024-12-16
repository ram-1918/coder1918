export const custom_captilize = (text, type = "custom") => {
  /*
    Title should be customized such that,
    - data structures and algorithms => Data Structures and Algorithms
    Here 'and' is not capitalized, so nouns alone should be capitalized
    */
  if (type === "raw") {
    return text;
  }
  const exceptions = [
    "and",
    "or",
    "nor",
    "but",
    "so",
    "for",
    "yet",
    "to",
    "a",
    "an",
    "the",
    "of",
    "in",
    "on",
    "at",
    "by",
    "with",
  ];

  // Split the text into words
  const words = text.split(" ");

  // Capitalize the first word and any word that is not in the exceptions list
  const customized_text = words
    .map((word, idx) => {
      // Capitalize the first word always
      if (idx === 0 || !exceptions.includes(word.toLowerCase())) {
        return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
      }
      // Keep exceptions in lowercase
      return word.toLowerCase();
    })
    .join(" ");

  return customized_text;
};
