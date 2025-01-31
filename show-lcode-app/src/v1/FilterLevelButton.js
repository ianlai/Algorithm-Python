function FilterLevelButton(props) {
    let classNameLevel = "button ";
    if (props.level === 1) {
      classNameLevel += "button-easy ";
    } else if (props.level === 2) {
      classNameLevel += "button-medium ";
    } else if (props.level === 3) {
      classNameLevel += "button-hard ";
    }
    classNameLevel += props.isSelected ? 'clicked' : '' 
    console.log("classNameLevel:", classNameLevel)

  return (
    <button
    //   class="button-filter"
      className = {classNameLevel}
    //   style={{ border: props.isSelected ? '5px solid black' : ''}}
      onClick={() => props.onClickFilterLevelButton(props.level)}
    >
      {props.name}
    </button>
  );
}
export default FilterLevelButton;
