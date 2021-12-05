function TagButton(props) {
  return (
    <button
      className = {(props.isSelected) ? "button-tag-clicked": "button-tag"}
      onClick={() => props.onClickTagButton(props.tagName)}
    >
      {props.tagName}
    </button>
  );
}
export default TagButton;
