function test() {
  alert("yo");
}
function TagButton(props) {
  return (
    <button
      class="button-tag"
      role="button"
      onClick={() => props.onClickTagButton(props.tagName)}
    >
      {props.tagName}
    </button>
  );
}
export default TagButton;
