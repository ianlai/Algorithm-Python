function LevelButtonV2(props) {
  let classNameLevel = "button ";
  if (props.level === 1) {
    classNameLevel += "button-easy ";
  } else if (props.level === 2) {
    classNameLevel += "button-medium ";
  } else if (props.level === 3) {
    classNameLevel += "button-hard ";
  }
  classNameLevel += props.isSelected ? "clicked" : "";

  const handleClickLevelButton = (levelId) => () => {
    let selectedLevelIds = props.selectedLevelIds;
    let setSelectedLevelIds = props.setSelectedLevelIds;
    const updated = selectedLevelIds.find((id) => id === levelId)
      ? selectedLevelIds.filter((id) => id !== levelId)
      : [...selectedLevelIds, levelId];
    setSelectedLevelIds(updated);
  };
  return (
    <button
      className={classNameLevel}
      onClick={handleClickLevelButton(props.level)}
    >
      {props.name}
    </button>
  );
}
export default LevelButtonV2;
