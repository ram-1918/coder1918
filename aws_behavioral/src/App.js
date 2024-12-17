// import InterviewNotes from "./InterviewNotes";

import { useState } from "react";
import { handle_header_item, handleMouseMove } from "./helpers";
import { custom_captilize } from "./utils";
import { ToolTip } from "./base";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faAdd,
  faBars,
  faBook,
  faCog,
  faEdit,
  faPen,
  faSignOut,
  faUser,
  faUserCog,
} from "@fortawesome/free-solid-svg-icons";
import { icon } from "@fortawesome/fontawesome-svg-core";

const icon_style = "text-gray-600 opacity-80 cursor-pointer";

function App() {
  const [visibleSideBar, setSideBarVisible] = useState(true);
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  return (
    <div>
      {/* <InterviewNotes /> */}

      {/* To close opened dropdown */}
      {isDropdownOpen && <CloseOpenedDropdown setIsDropdownOpen={setIsDropdownOpen} />}
      <Header
        visibleSideBar={visibleSideBar}
        setSideBarVisible={setSideBarVisible}
        isDropdownOpen={isDropdownOpen} 
        setIsDropdownOpen={setIsDropdownOpen} 
      />
    </div>
  );
}

const Header = ({ visibleSideBar, setSideBarVisible, ...isdropdown }) => {
  const topics_headers = [
    "about me",
    "data structures and algorithms",
    "system design",
    "leadership principles",
  ];
  const [topnavItems, setTopnavItems] = useState(topics_headers); // List of topnav headers should be retrieved from the DATABASE
  const [newItem, setNewItem] = useState("");

  return (
    <header
      style={{ width: visibleSideBar ? "15rem" : "3rem" }}
      className="fixed top-0 left-0 z-10 h-full transition-all ease-linear bg-gray-100 text-md"
    >
      {/* To close opened dropdown */}
      {isdropdown.isDropdownOpen && <CloseOpenedDropdown setIsDropdownOpen={isdropdown.setIsDropdownOpen} />}
      {visibleSideBar ? (
        <div className="flex flex-col items-start justify-between h-full p-2 space-y-4">
          <HeaderOptions
            setTopnavItems={setTopnavItems}
            setSideBarVisible={setSideBarVisible}/>
          <DisplayTopicHeaders topnavItems={topnavItems}setTopnavItems={setTopnavItems} />
          <UserProfile {...isdropdown} />
        </div>
      ) : (
        <div className="flex flex-col items-center justify-between h-full py-2">
          <span
            onClick={() => setSideBarVisible((prev) => !prev)}
            className={icon_style}>
            <FontAwesomeIcon icon={faBars} />
          </span>
          <FontAwesomeIcon icon={faUserCog} />
        </div>
      )}
    </header>
  );
};

const CloseOpenedDropdown = ({setIsDropdownOpen}) => <div onClick={() => setIsDropdownOpen(false)} className="absolute w-full h-full"></div>;

const HeaderOptions = ({ setTopnavItems, setSideBarVisible }) => {
  return (
    <div className="flex items-center justify-between w-full">
      <span
        onClick={() => setSideBarVisible((prev) => !prev)}
        className={icon_style}>
        <FontAwesomeIcon icon={faBars} />
      </span>
      <span
        className={icon_style}
        onClick={() => handle_header_item("topic", "add", setTopnavItems)}>
        New Topic <FontAwesomeIcon icon={faAdd} />
      </span>
    </div>
  );
};

const DisplayTopicHeaders = ({ topnavItems, setTopnavItems }) => {
  // manage heading display type(raw, custom) in user-profile settings
  const [position, setPosition] = useState({ x: 0, y: 0 });

  return (
    <div className="flex flex-col items-start justify-start w-full h-full overflow-scroll ">
      {topnavItems.map((item, idx) => (
        <div
          onMouseMove={(e) => handleMouseMove(e, setPosition)}
          className="flex items-center justify-between w-full p-1 rounded-lg cursor-pointer group/item hover:bg-gray-200"
          key={idx}>
          <p className="relative space-x-1 overflow-hidden text-ellipsis whitespace-nowrap">
            <FontAwesomeIcon icon={faBook} className={icon_style} />
            <span>{custom_captilize(item, "custom")}</span>
          </p>
          <span onClick={() => handle_header_item('topic', 'update', setTopnavItems, item, 'new topic')} className="invisible px-2 group/edit group-hover/item:visible">
            <FontAwesomeIcon icon={faPen} className={`${icon_style} hover:text-slate-900`} />
            <ToolTip text={item} position={position} />
          </span>
        </div>
      ))}
    </div>
  );
};

const UserProfile = ({isDropdownOpen, setIsDropdownOpen}) => {
  return (
    <div className="relative w-full p-2 font-medium bg-gray-200 rounded-lg select-none">
      <span onClick={() => setIsDropdownOpen(prev => !prev)} className="space-x-4 cursor-pointer">
        <FontAwesomeIcon icon={faUserCog} className={icon_style} />
        <span>Ram Chandra B</span>
        {
          isDropdownOpen && <UserProfileOptions />
        }
      </span>
    </div>
  );
};

const UserProfileOptions = () => {
  return (
    <div className="absolute w-48 mb-2 bg-gray-100 border border-gray-200 rounded shadow-lg bottom-full">
      <ul className="font-light">
        <li className="px-4 py-2 cursor-pointer hover:bg-gray-200"><FontAwesomeIcon icon={faUser} className={icon_style} /> View Profile</li>
        <li className="px-4 py-2 cursor-pointer hover:bg-gray-200"><FontAwesomeIcon icon={faCog} className={icon_style} /> Settings</li>
        <li className="px-4 py-2 text-white bg-red-500 cursor-pointer hover:opacity-80"><FontAwesomeIcon icon={faSignOut} className="text-white" /> Logout</li>
      </ul>
    </div>
  )
}
export default App;
