function FilterTagButton(props) {
  return (
    <button
      class="button-filter"
      onClick={() => props.onClickFilterTagButton(props.tagName)}
    >
      {props.tagName}
    </button>
  );
}
export default FilterTagButton;
