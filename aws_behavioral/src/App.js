// import InterviewNotes from "./InterviewNotes";

import { useState } from "react";
import { handle_header_item } from "./helpers";
import { custom_captilize } from "./utils";
import { ToolTip } from "./base";

function App() {
  return (
    <div>
      {/* <InterviewNotes /> */}
      <Header />
    </div>
  );
}

const Header = () => {
  const topics_headers = [
    "about me",
    "data structures and algorithms",
    "system design",
    "leadership principles",
  ];
  const [topnavItems, setTopnavItems] = useState(topics_headers); // List of topnav headers should be retrieved from the DATABASE
  const [newItem, setNewItem] = useState("");

  return (
    <header className="fixed top-0 left-0 z-10 w-56 h-full bg-gray-100">
      <DisplayTopicHeaders topnavItems={topnavItems} />
    </header>
  );
};

const DisplayTopicHeaders = ({ topnavItems }) => {
  // manage heading display type(raw, custom) in user-profile settings
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (event) => {
    setPosition({
      x: event.clientX + 10,
      y: event.clientY + 10,
    });
  };
  return (
    <div className="flex flex-col items-start justify-start w-full h-full p-2 mobile:px-2">
      {topnavItems.map((item, idx) => (
        <div
          onMouseMove={handleMouseMove}
          className="w-full p-1 text-sm rounded-lg cursor-pointer group/item hover:bg-gray-200"
          key={idx}
        >
          <p className="relative overflow-hidden text-ellipsis whitespace-nowrap">
            {custom_captilize(item, "custom")}
          </p>
          <ToolTip text={item} position={position} />
        </div>
      ))}
    </div>
  );
};

export default App;
