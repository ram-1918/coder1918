export const ToolTip = ({ text, position }) => {
  /*
    when hovered on text(titles especially), this will display complete title
    */
   console.log(text, position);
  return (
    <div
    style={{
      left: `${position.x}px`,
      top: `${position.y}px`,
      padding: '5px',
      borderRadius: '5px',
      fontSize: '0.65rem',
      whiteSpace: 'nowrap',
      zIndex: 1000,
    }}
    className="absolute invisible bg-gray-300 top-1 group-hover/item:visible"
    >
      {text}
    </div>
  );
};
