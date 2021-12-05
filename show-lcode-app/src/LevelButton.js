function LevelButton(props) {
  return (
    <button
      className = {props.className}
        onClick={() => props.onClickLevelButton(props.level)}
    >
      {props.id}
    </button>
  );
}
export default LevelButton;
