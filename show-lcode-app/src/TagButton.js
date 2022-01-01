function getClassName(props){
    let className = ""
    if (props.isSelected){
        className += "button-tag-clicked";
    }else {
        className += "button-tag";
    }
    if (props.isAllTag){
        className = "button-tag-all";
    }
    return className;
}

function TagButton(props) {
  return (
    <button
      className = {getClassName(props)}
      onClick={() => props.onClickTagButton(props.tagName)}
    >
      {/* {props.tagName} */}
      {props.showName}
    </button>
  );
}
export default TagButton;
