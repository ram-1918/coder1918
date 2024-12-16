export const handle_header_item = (
  category,
  type,
  setFunc,
  item = "",
  new_item = ""
) => {
  /*
  This is a helper function for Topic, section headers (expects more in the future)
  - dynamically adds new headers
  - rename capability
  - delete header along with its contents
  
  Arguments:
  category - header type (topic, section,...)
  type - function type (add, edit, remove)
  setFunc - useState's function, which maintains the current state
  item - represents the current item (add, update, remove)
  new_item - represents the new item (when type is update, 'item' is replaced by 'new_item')
  */
  switch (type) {
    case "add":
      const reg_ex_mapper = {
        topic: new RegExp(/^topic\s\d+/),
        section: new RegExp(/^section\s\d+/),
      };
      setFunc((prev) => {
        let curr_topic_number = 1;
        const reg_ex = reg_ex_mapper[category];
        // Keep track of the current topic number
        for (let item of prev) {
          if (reg_ex.test(item)) {
            curr_topic_number += 1;
          }
        }
        return [...prev, `${category} ${curr_topic_number}`];
      });
      break;
    case "update":
      setFunc((prev) => {
        const idx = prev.findIndex((curr_item) => curr_item === item);
        prev[idx] = new_item;
        return prev;
      });
      break;
    case "delete":
      setFunc((prev) => {
        const new_items = prev.filter((curr_item) => curr_item !== item);
        return new_items;
      });
      break;
    default:
        console.log('Raise error message!');
}
};