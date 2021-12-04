function FilterButton(props) {
  return (
    <button
      class="button-filter"
      role="button"
      onClick={() => props.onClickFilterTagButton(props.tagName)}
    >
      {props.tagName}
    </button>
  );
}
export default FilterButton;
