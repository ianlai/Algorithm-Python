function test() {
  alert("yo");
}
function TagButton(props) {
  return (
    <button
      className = {(props.isSelected) ? "button-tag-clicked": "button-tag"}
      role="button"
      onClick={() => props.onClickTagButton(props.tagName)}
    >
      {props.tagName}
    </button>
  );
}
export default TagButton;
