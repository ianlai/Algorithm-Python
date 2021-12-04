function test() {
  alert("yo");
}
function TagButton(props) {
  return (
    <button
      class="button-1"
      role="button"
      onClick={() => props.onClickTagButton(props.tagName)}
    >
      {props.tagName}
    </button>
  );
}
export default TagButton;
