function FilterLevelButton(props) {
    let classNameLevel;
    if (props.level === 1) {
      classNameLevel = "button-easy";
    } else if (props.level === 2) {
      classNameLevel = "button-medium";
    } else if (props.level === 3) {
      classNameLevel = "button-hard";
    }
  return (
    <button
      class="button-filter"
      className={classNameLevel}
      onClick={() => props.onClickFilterLevelButton(props.level)}
    >
      {props.name}
    </button>
  );
}
export default FilterLevelButton;
