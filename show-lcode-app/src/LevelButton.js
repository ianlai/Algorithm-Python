function LevelButton(props) {
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
      className={classNameLevel}
      onClick={() => props.onClickLevelButton(props.level)}
    >
      {props.id}
    </button>
  );
}
export default LevelButton;
